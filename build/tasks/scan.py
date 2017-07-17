import os
from multiprocessing import Process, Queue, Pool
from Queue import Empty
import subprocess
import time

def condor_submit(fname,spool=True):
   if spool==True:
     cmd="condor_submit -spool %s"%fname
   else:
     cmd="condor_submit %s"%fname
   stdoutfn='%s.stdout'%fname
   stderrfn='%s.stderr'%fname
   res=1
   trials=0
   while res!=0:
     print "Try %d: %s"%(trials, cmd)
     sub=subprocess.Popen(cmd.split() ,
           stdout=open(stdoutfn,'w'),
           stderr=open(stderrfn,'w')  )
     res=sub.wait()
     stderr=open(stderrfn).read()
     stdout=open(stdoutfn).read()
     print(stdout)
     if stderr:
       print "Exit code:", res
       print stderr
     else:
       for line in stdout.split('\n'):
         if 'submitted to cluster' in line:
             jobs=int(line.split()[0])
             clusterid=int(line.split()[-1][:-1])
     trials+=1
     time.sleep(30)
   return jobs,clusterid

class Scan(object):
    def __init__(self,mask,studydir,**params):
        self.mask=mask
        self.studydir=studydir
        self.params=params.items()
        self.param_names=list(params)
    def get_cases(self):
        return zip(*[v for k,v in self.params])
#    def get_cases(self):
#        out=[[]]
#        for k,vals in self.params:
#            old=out[:]; out=[]
#            for vv in old:
#              for nn in vals:
#                out.append(vv+[nn])
#        return out
    def get_case_dir(self,case):
        return os.path.join(self.studydir,"_".join(map(str,case)))
    def mk_cases(self):
        if not os.path.isdir(self.studydir):
            os.mkdir(self.studydir)
        tmp=open(self.mask).read()
        for case in self.get_cases():
            casedir=self.get_case_dir(case)
            if not os.path.isdir(casedir):
                os.mkdir(casedir)
            res=tmp
            for k,vals in zip(self.param_names,case):
                res=res.replace('%%%s'%(k.upper()),str(vals))
            fn=os.path.join(casedir,self.mask)
            print "Writing: %s"%fn
            open(fn,'w').write(res)
        return self
    def exe_condor(self,runtime=60*20,out=None):
        data=self.__dict__.copy()
        data['runtime']=runtime
        if out is None:
            outline=''
        else:
           outline='transfer_output_files   = %s'%out
        data['outline']=outline
        tmp="""\
        executable              = madx_wrapper.sh
        arguments               = {mask}
        output                  = std.$(ClusterId).$(ProcId).out
        error                   = std.$(ClusterId).$(ProcId).err
        log                     = condor.$(ClusterId).log
        initial_dir             = $(dirname)
        transfer_input_files    = {mask}
        {outline}
        +MaxRuntime = {runtime}
        queue dirname matching ({studydir}/*)
        """.format(**data)
        fn="%s.condor"%self.studydir
        open(fn,'w').write(tmp)
        ret=condor_submit(fn)
        if ret is not None:
            self.condor_jobs,self.condor_id=ret
        return self
    def exe_local(self,processes=8):
        cmd="madx %s"%self.mask
        def worker(q):
            while True:
                try:
                    cmd,cwd=q.get(False)
                    print "Executing %s in %s"%(cmd,cwd)
                except Empty:
                    return
                stdout=open(os.path.join(cwd,'stdout'),'w')
                stderr=open(os.path.join(cwd,'stderr'),'w')
                sub=subprocess.Popen(cmd.split(),
                          stdout=stdout, stderr=stderr, cwd=cwd)
                sub.wait()
        q=Queue()
        for case in self.get_cases():
            q.put([cmd,self.get_case_dir(case)])
        for nn in range(processes):
          p = Process(target=worker, args=(q,))
          p.start()
        for nn in range(processes):
          p.join()
        return self
    def get_file(self,case,filename):
        return os.path.join(self.get_case_dir(case),filename)



import os

from scan import Scan


sc=Scan('job_mksqueeze.madx','squeeze',
        bbb=list(range(500,140,-10)))

sc.mk_cases()
minute=60
sc.exe_condor(runtime=40*minute,out='result.tgz')

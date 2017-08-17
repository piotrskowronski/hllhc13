import os

from scan import Scan


sc=Scan('job_mksqueeze_thin.madx','squeeze_thin',
        bbb=list(range(500,140,-10)))

sc.mk_cases()
sc.exe_condor(runtime=40*60,out='result.tgz')

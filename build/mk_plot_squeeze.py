from pyoptics import *
from matplotlib.pyplot import *
from matplotlib.axes import *
import scipy
#close('all')
#--- compare new/old squeeze
def plot_squeeze_diff(ir='2468',opt='round'):
  for i in ir:
    ds=StrTable.open('ir%s_%s.tfs'%(i,opt))
    ds.plot_squeeze_diff(fn='ir%s_log_str.tfs'%i,title='comp squeeze IR%s'%i)
    dsnew=StrTable.open('ir%s_log_str.tfs'%i)
    print i,max(dsnew['tarir%sb1'%i]),max(dsnew['tarir%sb2'%i])


def plot_squeeze(ir='2468',opt='round'):
  close('all')
  for i in ir:
    fname='ir%s_%s.tfs'%(i,opt)
    print fname
    ds=StrTable.open(fname)
    ds.plot_squeeze() # title='squeeze IR%s'%i
    print i,max(ds['tarir%sb1'%i]),max(ds['tarir%sb2'%i])
    savefig('ir%s_%s.png'%(i,opt))

#for opt in 'round','flat','flathv':
opt='flat'
fig=figure(opt)
ds=StrTable.open('ir6_%s.tfs'%opt)
plot(ds.betxtcdsb1,'k',label='betx TCDS.A*.B1')
plot(ds.betytcdsb1,'r',label='bety TCDS.A*.B1')
plot(ds.betxtcdsb2,'b',label='betx TCDS.A*.B2')
plot(ds.betytcdsb2,'m',label='bety TCDS.A*.B2')
xlabel(r'squeeze step (squeeze -> presqueeze)')
ylabel(r'$\beta_{x/y,\rm TCDS.A}$ [m]')
title('%s squeeze'%opt)
legend(loc='best')
savefig('ir6_%s_beta_tcsg.png'%(opt))

close('all')
plot(ds.betxtcdsb1,'k',marker='.',label='betx TCDS.A*.B1')

xs = np.arange(0.0, len(ds.betxtcdsb1), 1)

fill_between(xs, 150, 160, hatch='/',facecolor='white',edgecolor='red')

xlabel(r'squeeze step (squeeze -> presqueeze)')
ylabel(r'$\beta_{x,b1,\rm TCDS.A}$ [m]')
title('betxtcdsb1 %s squeeze '%opt)
savefig('ir6_%s_betxtcdsb1.png'%(opt))

close('all')
plot(ds.betytcdsb1,'k',marker='.',label='bety TCDS.A*.B1')
xlabel(r'squeeze step (squeeze -> presqueeze)')
ylabel(r'$\beta_{y,b1,\rm TCDS.A}$ [m]')
title('betytcdsb1 %s squeeze '%opt)
savefig('ir6_%s_betytcdsb1.png'%(opt))

close('all')
plot(ds.betxtcdsb2,'k',marker='.',label='betx TCDS.A*.B2')
xlabel(r'squeeze step (squeeze -> presqueeze)')
ylabel(r'$\beta_{x,b2,\rm TCDS.A}$ [m]')
title('betxtcdsb2 %s squeeze '%opt)
savefig('ir6_%s_betxtcdsb2.png'%(opt))

close('all')
plot(ds.betytcdsb2,'k',marker='.',label='bety TCDS.A*.B2')
xlabel(r'squeeze step (squeeze -> presqueeze)')
ylabel(r'$\beta_{y,b2,\rm TCDS.A}$ [m]')
title('betytcdsb2 %s squeeze '%opt)
savefig('ir6_%s_betytcdsb2.png'%(opt))




#plot_squeeze_diff(opt='round')
#plot_squeeze_diff(opt='flat')
#plot_squeeze_diff(opt='flathv')
#plot_squeeze(opt='round')

sys.exit();
plot_squeeze(opt=opt)
#plot_squeeze(opt='flathv')

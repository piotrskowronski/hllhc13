import pyoptics as pop
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import matplotlib.ticker as ticker
import scipy as sp
import numpy as np
import sys
#close('all')
#--- compare new/old squeeze
def plot_squeeze_diff(ir='2468',opt='round'):
  for i in ir:
    ds=StrTable.open('ir%s_%s.tfs'%(i,opt))
    ds.plot_squeeze_diff(fn='ir%s_log_str.tfs'%i,title='comp squeeze IR%s'%i)
    dsnew=StrTable.open('ir%s_log_str.tfs'%i)
    print i,max(dsnew['tarir%sb1'%i]),max(dsnew['tarir%sb2'%i])


def plot_squeeze_all(ir='2468',opt='round'):
#  close('all')
  for i in ir:
    fname='ir%s_%s.tfs'%(i,opt)
    print fname
    ds=pop.StrTable.open(fname)
    ds.plot_squeeze() # title='squeeze IR%s'%i
    print i,max(ds['tarir%sb1'%i]),max(ds['tarir%sb2'%i])
    plt.savefig('ir%s_%s.png'%(i,opt))

###########################################################################
## PLOT_SQ_VARCONSTR
## -1 var need to be bigger then constrval
##  0 var need to be eqaul
## +1 var need to be smaller then constrval
## +2 var need to be in range
def plot_sq(ds,varname,title=None,ylab=None,log=False):
  var = ds[varname]
  if title is None:
     title = varname
  if ylab is None:
     ylab = varname
     
  plt.close('all') 
  plt.figure(title)
  if log:
    plt.semilogy(var,'k',marker='.',label=title)
  else:
    plt.plot(var,'k',marker='.',label=title)
    
  y_formatter = ticker.ScalarFormatter(useOffset=False)
  ax1 = plt.gca()
  ax1.yaxis.set_major_formatter(y_formatter)
 
  plt.xlabel(r'squeeze step ')
  plt.ylabel(ylab)
  plt.title(title)
#  plt.show()
  plt.savefig('%s.png'%varname)

###########################################################################
## PLOT_SQ_VARCONSTR
## -1 var need to be bigger then constrval
##  0 var need to be eqaul
## +1 var need to be smaller then constrval
## +2 var need to be in range
def plot_sq_varconstr(var,varname,title,ylab,constrval,constrtype, constrval2=np.NaN ):
  plt.close('all') 
  plt.plot(var,'k',marker='.',label=title)
  xs = np.arange(0.0, len(var), 1)
  
  if (constrtype == -1):
    xmin = constrval*0.9
    datamin = min(var)
    if ( datamin < xmin):
      xmin = 0.9*datamin
    plt.fill_between(xs, xmin, constrval, hatch='/',facecolor='white',edgecolor='red')


  if (constrtype == 2):
    xmin = constrval   - 50
    xmax = constrval2  + 50

    datamin = min(var)
    if ( datamin < xmin):
      xmin = 0.9*datamin

    datamax = max(var)
    if ( datamax > xmax):
      xmax = 1.1*datamax
    
    print xmin, constrval
    plt.fill_between(xs, xmin, constrval, hatch='/',facecolor='white',edgecolor='red')
    
    print constrval2, xmax
    plt.fill_between(xs, constrval2, xmax, hatch='/',facecolor='white',edgecolor='red')
    
  plt.xlabel(r'squeeze step ')
  plt.ylabel(ylab)
  plt.title(title)
#  plt.show()
  plt.savefig('%s.png'%varname)
  
###############################################################
###############################################################
###############################################################

opt='flat' 

###############################################################
# betx TCDS.A*.B1

#plot_sq_varconstr(ds.betxtcdsb1,'betxtcdsb1','betx TCDS.A*.B1', r'$\beta_{x,b1,\rm TCDS.A}$ [m]',  160, -1)

#plot_sq_varconstr(ds.betytcdsb1,'betytcdsb1','bety TCDS.A*.B1', r'$\beta_{y,b1,\rm TCDS.A}$ [m]',  200, -1)
#plot_sq_varconstr(ds.betytcdsb2,'betytcdsb2','bety TCDS.A*.B2', r'$\beta_{y,b2,\rm TCDS.A}$ [m]',  200, -1)



ds=pop.StrTable.open('ir1_%s.tfs'%opt)

plot_sq(ds,'muxip1b1')
plot_sq(ds,'muyip1b1')
plot_sq(ds,'muxip1b1_l')
plot_sq(ds,'muyip1b1_l')
plot_sq(ds,'muxip1b1_r')
plot_sq(ds,'muyip1b1_r')

plot_sq(ds,'muxip1b2')
plot_sq(ds,'muyip1b2')
plot_sq(ds,'muxip1b2_l')
plot_sq(ds,'muyip1b2_l')
plot_sq(ds,'muxip1b2_r')
plot_sq(ds,'muyip1b2_r')


ds=pop.StrTable.open('ir5_%s.tfs'%opt)

plot_sq(ds,'muxip5b1')
plot_sq(ds,'muyip5b1')
plot_sq(ds,'muxip5b1_l')
plot_sq(ds,'muyip5b1_l')
plot_sq(ds,'muxip5b1_r')
plot_sq(ds,'muyip5b1_r')

plot_sq(ds,'muxip5b2')
plot_sq(ds,'muyip5b2')
plot_sq(ds,'muxip5b2_l')
plot_sq(ds,'muyip5b2_l')
plot_sq(ds,'muxip5b2_r')
plot_sq(ds,'muyip5b2_r')


ds=pop.StrTable.open('ir2_%s.tfs'%opt)

plot_sq(ds,'muxip2b1')
plot_sq(ds,'muyip2b1')
plot_sq(ds,'muxip2b1_l')
plot_sq(ds,'muyip2b1_l')
plot_sq(ds,'muxip2b1_r')
plot_sq(ds,'muyip2b1_r')

plot_sq(ds,'muxip2b2')
plot_sq(ds,'muyip2b2')
plot_sq(ds,'muxip2b2_l')
plot_sq(ds,'muyip2b2_l')
plot_sq(ds,'muxip2b2_r')
plot_sq(ds,'muyip2b2_r')

ds=pop.StrTable.open('ir8_%s.tfs'%opt)

plot_sq(ds,'muxip8b1')
plot_sq(ds,'muyip8b1')
plot_sq(ds,'muxip8b1_l')
plot_sq(ds,'muyip8b1_l')
plot_sq(ds,'muxip8b1_r')
plot_sq(ds,'muyip8b1_r')

plot_sq(ds,'muxip8b2')
plot_sq(ds,'muyip8b2')
plot_sq(ds,'muxip8b2_l')
plot_sq(ds,'muyip8b2_l')
plot_sq(ds,'muxip8b2_r')
plot_sq(ds,'muyip8b2_r')


ds=pop.StrTable.open('ir4_%s.tfs'%opt)

plot_sq(ds,'muxip4b1')
plot_sq(ds,'muyip4b1')
plot_sq(ds,'muxip4b1_l')
plot_sq(ds,'muyip4b1_l')
plot_sq(ds,'muxip4b1_r')
plot_sq(ds,'muyip4b1_r')

plot_sq(ds,'muxip4b2')
plot_sq(ds,'muyip4b2')
plot_sq(ds,'muxip4b2_l')
plot_sq(ds,'muyip4b2_l')
plot_sq(ds,'muxip4b2_r')
plot_sq(ds,'muyip4b2_r')

ds=pop.StrTable.open('ir6_%s.tfs'%opt)

plot_sq(ds,'muxip6b1')
plot_sq(ds,'muyip6b1')
plot_sq(ds,'muxip6b1_l')
plot_sq(ds,'muyip6b1_l')
plot_sq(ds,'muxip6b1_r')
plot_sq(ds,'muyip6b1_r')

plot_sq(ds,'muxip6b2')
plot_sq(ds,'muyip6b2')
plot_sq(ds,'muxip6b2_l')
plot_sq(ds,'muyip6b2_l')
plot_sq(ds,'muxip6b2_r')
plot_sq(ds,'muyip6b2_r')


ds=pop.StrTable.open('ir3_%s.tfs'%opt)


plot_sq(ds,'muxip3b1')
plot_sq(ds,'muyip3b1')
plot_sq(ds,'muxip3b1_l')
plot_sq(ds,'muyip3b1_l')
plot_sq(ds,'muxip3b1_r')
plot_sq(ds,'muyip3b1_r')

plot_sq(ds,'muxip3b2')
plot_sq(ds,'muyip3b2')
plot_sq(ds,'muxip3b2_l')
plot_sq(ds,'muyip3b2_l')
plot_sq(ds,'muxip3b2_r')
plot_sq(ds,'muyip3b2_r')

ds=pop.StrTable.open('ir7_%s.tfs'%opt)

plot_sq(ds,'muxip7b1')
plot_sq(ds,'muyip7b1')
plot_sq(ds,'muxip7b1_l')
plot_sq(ds,'muyip7b1_l')
plot_sq(ds,'muxip7b1_r')
plot_sq(ds,'muyip7b1_r')

plot_sq(ds,'muxip7b2')
plot_sq(ds,'muyip7b2')
plot_sq(ds,'muxip7b2_l')
plot_sq(ds,'muyip7b2_l')
plot_sq(ds,'muxip7b2_r')
plot_sq(ds,'muyip7b2_r')


####################################################

sys.exit()

ds=pop.StrTable.open('rng_%s.tfs'%opt)

plot_sq(ds,'dtct1b1')
plot_sq(ds,'dtct5b1')
plot_sq(ds,'dtct1b2')
plot_sq(ds,'dtct5b2')

plot_sq(ds,'dtct1b1a')
plot_sq(ds,'dtct5b1a')
plot_sq(ds,'dtct1b2a')
plot_sq(ds,'dtct5b2a')


plot_sq_varconstr(ds['ddtct1b1'],'ddtct1b1','mux B1 TCTXH.4L1 <-> MKD.O5L6', r'$mu_{x}$ [deg]',-50,2,constrval2=50)
plot_sq_varconstr(ds['ddtct5b1'],'ddtct5b1','mux B1 TCTXH.4L5 <-> MKD.O5L6', r'$mu_{x}$ [deg]',-50,2,constrval2=50)
plot_sq_varconstr(ds['ddtct1b2'],'ddtct1b2','mux B2 TCTXH.4R1 <-> MKD.O5R6', r'$mu_{x}$ [deg]',-50,2,constrval2=50)
plot_sq_varconstr(ds['ddtct5b2'],'ddtct5b2','mux B2 TCTXH.4R5 <-> MKD.O5R6', r'$mu_{x}$ [deg]',-50,2,constrval2=50)

plot_sq_varconstr(ds['ddtct1b1a'],'ddtct1b1a','mux B1 TCTXH.4L1 <-> MKD.A5L6', r'$mu_{x}$ [deg]',-50,2,constrval2=50)
plot_sq_varconstr(ds['ddtct5b1a'],'ddtct5b1a','mux B1 TCTXH.4L5 <-> MKD.A5L6', r'$mu_{x}$ [deg]',-50,2,constrval2=50)
plot_sq_varconstr(ds['ddtct1b2a'],'ddtct1b2a','mux B2 TCTXH.4R1 <-> MKD.A5R6', r'$mu_{x}$ [deg]',-50,2,constrval2=50)
plot_sq_varconstr(ds['ddtct5b2a'],'ddtct5b2a','mux B2 TCTXH.4R5 <-> MKD.A5R6', r'$mu_{x}$ [deg]',-50,2,constrval2=50)


sys.exit()

ds=pop.StrTable.open('ir6_%s.tfs'%opt)
scale=23348.89927
qtlimit2 = 160.0/scale
plot_sq(ds,'kq4.l6.b1',title='k1 of KQ4.L6.B1', ylab=r'$\k1_{KQ4.L6.B1}$ ')
plot_sq(ds,'kq4.r6.b1',title='k1 of KQ4.R6.B1', ylab=r'$\k1_{KQ4.R6.B1}$ ')
plot_sq(ds,'kq4.l6.b2',title='k1 of KQ4.L6.B2', ylab=r'$\k1_{KQ4.L6.B2}$ ')
plot_sq(ds,'kq4.r6.b2',title='k1 of KQ4.R6.B2', ylab=r'$\k1_{KQ4.R6.B2}$ ')





sys.exit();

plot_sq(ds,'tarir1b1',log=True)
plot_sq(ds,'tarir1b2',log=True)
plot_sq(ds,'tarir2b1',log=True)
plot_sq(ds,'tarir2b2',log=True)
plot_sq(ds,'tarir3b1',log=True)
plot_sq(ds,'tarir3b2',log=True)
plot_sq(ds,'tarir4b1',log=True)
plot_sq(ds,'tarir4b2',log=True)
plot_sq(ds,'tarir5b1',log=True)
plot_sq(ds,'tarir5b2',log=True)
plot_sq(ds,'tarir6b1',log=True)
plot_sq(ds,'tarir6b2',log=True)
plot_sq(ds,'tarir7b1',log=True)
plot_sq(ds,'tarir7b2',log=True)
plot_sq(ds,'tarir8b1',log=True)
plot_sq(ds,'tarir8b2',log=True)

sys.exit()

ds=pop.StrTable.open('rng_%s.tfs'%opt)

plot_sq(ds,'refqxb1')
plot_sq(ds,'refqyb1')
plot_sq(ds,'refqxb2')
plot_sq(ds,'refqyb2')


#plot_squeeze_all(opt=opt)


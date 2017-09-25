import pyoptics as pop
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import matplotlib.ticker as ticker
import scipy as sp
import numpy as np
import sys
import math	
#--- compare new/old squeeze

def plot_squeeze_diff(ir='6',dir2='../pass13',n1=0,n2=None,x=None):
  opt='flat'
#  for i in ir:
  fname1 = 'ir%s_%s.tfs'%(ir,opt)
  fname2 = '%s/ir%s_%s.tfs'%(dir2,ir,opt)
  print fname1, fname2
  ds1=pop.StrTable.open(fname1)
  ds2=pop.StrTable.open(fname2)

  fig=plt.figure('squeeze',figsize=(16,12))
  fig.canvas.mpl_connect('button_release_event',ds1.button_press)
  plt.clf()
  if len(ds1.get_vars('kqx'))>0:
    plt.subplot(3,4,1)
    ds1.plot_triplet(n1,n2,x=x)
    ds1.plot_triplet(n1,n2,x=x)
  for n in range(4,11):
    if len(ds1.get_kq(n))>0:
      plt.subplot(3,4,n-2)
      plot_twoinone(ds1,ds2,n,n1,n2,x=x,sign=False)
  for n in range(11,14):
    if len(ds1.get_kq(n))>0:
      plt.subplot(3,4,n-2)
      plot_twoinone(ds1,ds2,n,n1,n2,x=x,sign=True)
  plt.subplot(3,4,12)
  #self.plot_ipbeta(n1,n2,x=x)
  ds1.plot_phase(n1,n2,x=x)
  #plt.tight_layout()

  plt.savefig('ir%s_diff.png'%ir)


def plot_twoinone(ds1, ds2, kq,n1,n2,x=None,sign=False,ylab='k [T/m]'):
  scale=ds1.scale
  pal = ["" for xxx in range(6)]
  pal[0]='k'
  pal[1]='r'
  pal[2]='g'
  pal[3]='b'
  pal[4]='m'
  pal[5]='c'
  
  if x is None:
    xv =np.arange(len(ds1[ds1.keys()[0]][n1:n2]))
    xv2=np.arange(len(ds2[ds2.keys()[0]][n1:n2]))
  else:
    xv =ds1[x][n1:n2]
    xv2=ds2[x][n1:n2]
  col=0
  for k in ds1.get_kq(kq):
    kv =ds1[k][n1:n2]*scale
    kv2=ds2[k][n1:n2]*scale
    if sign or kv[0]>0:
      plt.plot(xv ,kv ,label=k, linestyle='-' , color=pal[col])
      plt.plot(xv2,kv2,label=k, linestyle='--', color=pal[col])
    else:
      plt.plot(xv ,-kv,label='-'+k, linestyle='-' , color=pal[col])
      plt.plot(xv2,-kv,label='-'+k, linestyle='--', color=pal[col])
    col=col+1
  plt.legend(loc=0,frameon=False)
  if x is not None:
    plt.xlabel(x)
  plt.ylabel(ylab)
  a,b=plt.xticks()
  plt.xticks(a[::2])


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
## PLOT_SQ
def plot_sq(ds,varname,title=None,ylab=None,log=False,noaxisexp=False):
  print 'plot_sq: ', varname
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
  if noaxisexp:
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
def plot_sq_varconstr(var,varname,title,ylab,constrval,constrtype, constrval2=np.NaN, deadspan=None ):
  print 'plot_sq_varconstr: ', varname
  if deadspan is None:
     deadspan = constrval*0.1

  plt.close('all') 
  plt.plot(var,'k',marker='.',label=title)
  xs = np.arange(0.0, len(var), 1)

  
  if (constrtype == -1):
    xmin = constrval - deadspan
    datamin = min(var)
    if ( datamin < xmin):
      xmin = 0.9*datamin
    plt.fill_between(xs, xmin, constrval, hatch='/',facecolor='white',edgecolor='red')


  if (constrtype == 2):
    xmin = constrval   - deadspan
    xmax = constrval2  + deadspan

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

opt='round' 
opt='single' 
opt='flat' 


plot_squeeze_diff('6')


sys.exit()




ds=pop.StrTable.open('arc_%s.tfs'%opt)

plot_sq(ds,'mux12b1',noaxisexp=True)

plot_sq(ds,'betxtcdqb1',title='betx TCDQA.A4R6.B1', ylab=r'$\beta_{x,b1,\rm TCDQ.A}$ [m]')
plot_sq(ds,'betxtcdqb2',title='betx TCDQA.A4L6.B1', ylab=r'$\beta_{x,b2,\rm TCDQ.A}$ [m]')

plot_sq(ds,'dxtcdqb1',title='dx TCDQA.A4R6.B1', ylab=r'$Dx_{x,b1,\rm TCDQ.A}$ [m]')
plot_sq(ds,'dxtcdqb2',title='dx TCDQA.A4L6.B1', ylab=r'$Dx_{x,b2,\rm TCDQ.A}$ [m]')







################################################


#plot_sq_varconstr(ds.betxtcdsb1,'betxtcdsb1','betx TCDS.A*.B1', r'$\beta_{x,b1,\rm TCDS.A}$ [m]',  160, -1)

#sys.exit()



ds=pop.StrTable.open('rng_%s.tfs'%opt)

plot_sq(ds,'qxb1',noaxisexp=True)
plot_sq(ds,'qyb1',noaxisexp=True)
plot_sq(ds,'qxb2',noaxisexp=True)
plot_sq(ds,'qyb2',noaxisexp=True)

plot_sq(ds,'refqxb1',noaxisexp=True)
plot_sq(ds,'refqyb1',noaxisexp=True)
plot_sq(ds,'refqxb2',noaxisexp=True)
plot_sq(ds,'refqyb2',noaxisexp=True)

#sys.exit()


plot_squeeze_all(opt=opt)

# sys.exit()


ds=pop.StrTable.open('ir1_%s.tfs'%opt)

plot_sq(ds,'betxip1b1')
plot_sq(ds,'betyip1b1')

# sys.exit()

ds=pop.StrTable.open('ir2_%s.tfs'%opt)
plot_sq(ds,'scxir1')
plot_sq(ds,'scyir1')

########################################################



ds=pop.StrTable.open('ir6_%s.tfs'%opt)
scale=23348.89927
qtlimit2 = 160.0/scale
plot_sq(ds,'kq4.l6b1',title='k1 of KQ4.L6.B1', ylab=r'$\k1_{KQ4.L6.B1}$ ')
plot_sq(ds,'kq4.r6b1',title='k1 of KQ4.R6.B1', ylab=r'$\k1_{KQ4.R6.B1}$ ')
plot_sq(ds,'kq4.l6b2',title='k1 of KQ4.L6.B2', ylab=r'$\k1_{KQ4.L6.B2}$ ')
plot_sq(ds,'kq4.r6b2',title='k1 of KQ4.R6.B2', ylab=r'$\k1_{KQ4.R6.B2}$ ')





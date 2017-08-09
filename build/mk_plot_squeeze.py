import pyoptics as pop
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import matplotlib.ticker as ticker
import scipy as sp
import numpy as np
import sys
import math	
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
opt='flat' 
opt='single' 



ds=pop.StrTable.open('arc_%s.tfs'%opt)
plot_sq(ds,'mux12b1',noaxisexp=True)
plot_sq(ds,'muy12b1',noaxisexp=True)
plot_sq(ds,'mux12b2',noaxisexp=True)
plot_sq(ds,'muy12b2',noaxisexp=True)
plot_sq(ds,'mux23b1',noaxisexp=True)
plot_sq(ds,'muy23b1',noaxisexp=True)
plot_sq(ds,'mux23b2',noaxisexp=True)
plot_sq(ds,'muy23b2',noaxisexp=True)
plot_sq(ds,'mux34b1',noaxisexp=True)
plot_sq(ds,'muy34b1',noaxisexp=True)
plot_sq(ds,'mux34b2',noaxisexp=True)
plot_sq(ds,'muy34b2',noaxisexp=True)
plot_sq(ds,'mux45b1',noaxisexp=True)
plot_sq(ds,'muy45b1',noaxisexp=True)
plot_sq(ds,'mux45b2',noaxisexp=True)
plot_sq(ds,'muy45b2',noaxisexp=True)
plot_sq(ds,'mux56b1',noaxisexp=True)
plot_sq(ds,'muy56b1',noaxisexp=True)
plot_sq(ds,'mux56b2',noaxisexp=True)
plot_sq(ds,'muy56b2',noaxisexp=True)
plot_sq(ds,'mux67b1',noaxisexp=True)
plot_sq(ds,'muy67b1',noaxisexp=True)
plot_sq(ds,'mux67b2',noaxisexp=True)
plot_sq(ds,'muy67b2',noaxisexp=True)
plot_sq(ds,'mux78b1',noaxisexp=True)
plot_sq(ds,'muy78b1',noaxisexp=True)
plot_sq(ds,'mux78b2',noaxisexp=True)
plot_sq(ds,'muy78b2',noaxisexp=True)
plot_sq(ds,'mux81b1',noaxisexp=True)
plot_sq(ds,'muy81b1',noaxisexp=True)
plot_sq(ds,'mux81b2',noaxisexp=True)
plot_sq(ds,'muy81b2',noaxisexp=True)

#sys.exit()


###############################################################
# betx TCDS.A*.B1

ds=pop.StrTable.open('ir6_%s.tfs'%opt)

################################################
# Chiara C2
#Horizontal phase advance MKDsTCDQ 90deg plus minus 4deg

#constraint, expr=abs(refdmuxkickb1-0.250)<0.011;                   refdmuxkickb1=table(twiss,TCDQA.A4R6.B1,mux)- table(twiss,MKD.H5L6.B1,mux);
plot_sq_varconstr(ds.dmuxkickb1,'dmuxkickb1','mux TCDQA <--> MKDH', r'$\mu_{x,b1,\rm TCDQ.A \rm MKD.H} [2 \cdot \pi]$ ',  0.25 - 0.011, 2, constrval2=0.25+0.011)
#constraint,weight=1000,expr= abs(refdmuxkickb2_tcdq-0.250)<0.0111; refdmuxkickb2_tcdq=table(twiss,MKD.H5R6.B2,mux)-table(twiss,TCDQA.C4L6.B2,mux);
plot_sq_varconstr(ds.dmuxkickb2_tcdq,'dmuxkickb2','mux TCDQA <--> MKDH', r'$\mu_{x,b2,\rm TCDQ.A \rm MKD.H} [2 \cdot \pi]$ ',  0.25 - 0.011, 2, constrval2=0.25+0.011)


################################################
# Chiara C3
# TCDS: by,min >= 200 m (no more than 10% smaller than present value)

#     constraint, range=TCDSA.4L6.B1,bety > 200;  
plot_sq_varconstr(ds.betytcdsb1,'betytcdsb1','bety TCDSA.4L6.B1',  r'$\beta_{y,b2,\rm TCDS.A}$ [m]',  200, -1)
plot_sq_varconstr(ds.betytcdsb2,'betytcdsb2','bety TCDSA.4R6.B2',  r'$\beta_{y,b2,\rm TCDS.A}$ [m]',  200, -1)


################################################
# Chiara C4
#     constraint, range=TCDQA.A4R6.B1,bety > 145;  ! betytcdqb1
plot_sq_varconstr(ds.betytcdqb1,'betytcdqb1','bety TCDQA.A4R6.B1', r'$\beta_{y,b1,\rm TCDQ.A}$ [m]',  145, -1)
# betytcdqb2=table(twiss,TCDQA.A4L6.B2,bety);
plot_sq_varconstr(ds.betytcdqb2,'betytcdqb2','bety TCDQA.A4L6.B2', r'$\beta_{y,b2,\rm TCDQ.A}$ [m]',  145, -1)


################################################
# Chiara C5
# Applies only to injection




################################################
# Chiara C6
# Applies only to injection
# TCDQ: bx,min such that minimum gap at 7 TeV > 3 mm taking into account all margins 
# (0.3 mm setup and optics errors + Dx*Dp/p + orbit offset depending on achievable interlock BPM reliability/accuracy)
nsig = 10.1; dPoverP = 2e-4; emitx=2.5e-6/(7000/0.9382720814); maxorbitdrift = 1.2e-3;
#nsig*sqrt(emitx*betx) - 3e-4  - abs(dx*dPoverP) - maxorbitdrift > 3e-3

#betxtcdqb1   =table(twiss,TCDQA.A4R6.B1,betx);
#betytcdqb1   =table(twiss,TCDQA.A4R6.B1,bety);
#dxtcdqb1     =table(twiss,TCDQA.A4R6.B1,dx);
#dytcdqb1=table(twiss,TCDQA.A4R6.B1,dy);

tcdqmingapb1 = nsig*np.sqrt(emitx*ds.betxtcdqb1) - 3e-4  - abs(ds.dxtcdqb1*dPoverP) - maxorbitdrift
plot_sq_varconstr(tcdqmingapb1,'tcdqmingapb1','minimum gap of TCDQA.A4R6.B1 (betx&dx)', r'min. gap [m]',  3e-3, -1, deadspan=3e-3)

tcdqmingapb2 = nsig*np.sqrt(emitx*ds.betxtcdqb2) - 3e-4  - abs(ds.dxtcdqb2*dPoverP) - maxorbitdrift
plot_sq_varconstr(tcdqmingapb2,'tcdqmingapb2','minimum gap of TCDQA.A4L6.B1 (betx&dx)', r'min. gap [m]',  3e-3, -1, deadspan=3e-3)

plot_sq(ds,'betxtcdqb1',title='betx TCDQA.A4R6.B1', ylab=r'$\beta_{x,b1,\rm TCDQ.A}$ [m]')
plot_sq(ds,'betxtcdqb2',title='betx TCDQA.A4L6.B1', ylab=r'$\beta_{x,b2,\rm TCDQ.A}$ [m]')

plot_sq(ds,'dxtcdqb1',title='dx TCDQA.A4R6.B1', ylab=r'$Dx_{x,b1,\rm TCDQ.A}$ [m]')
plot_sq(ds,'dxtcdqb2',title='dx TCDQA.A4L6.B1', ylab=r'$Dx_{x,b2,\rm TCDQ.A}$ [m]')




################################################
# Chiara C8
# fot abs(Dx) < 2m 
# mux MKD <--> TCTs 0 or 180 plus minus 50 degrees

ds=pop.StrTable.open('rng_%s.tfs'%opt)

plot_sq(ds,'dtct1b1')
plot_sq(ds,'dtct5b1')
plot_sq(ds,'dtct1b2')
plot_sq(ds,'dtct5b2')

plot_sq(ds,'dtct1b1a')
plot_sq(ds,'dtct5b1a')
plot_sq(ds,'dtct1b2a')
plot_sq(ds,'dtct5b2a')


plot_sq_varconstr(ds['ddtct1b1'],'ddtct1b1','mux B1 TCTXH.4L1 <-> MKD.O5L6', r'$mu_{x}$ [deg]',-50,2,constrval2=50, deadspan=80)
plot_sq_varconstr(ds['ddtct5b1'],'ddtct5b1','mux B1 TCTXH.4L5 <-> MKD.O5L6', r'$mu_{x}$ [deg]',-50,2,constrval2=50, deadspan=80)
plot_sq_varconstr(ds['ddtct1b2'],'ddtct1b2','mux B2 TCTXH.4R1 <-> MKD.O5R6', r'$mu_{x}$ [deg]',-50,2,constrval2=50, deadspan=80)
plot_sq_varconstr(ds['ddtct5b2'],'ddtct5b2','mux B2 TCTXH.4R5 <-> MKD.O5R6', r'$mu_{x}$ [deg]',-50,2,constrval2=50, deadspan=80)

plot_sq_varconstr(ds['ddtct1b1a'],'ddtct1b1a','mux B1 TCTXH.4L1 <-> MKD.A5L6', r'$mu_{x}$ [deg]',-50,2,constrval2=50, deadspan=80)
plot_sq_varconstr(ds['ddtct5b1a'],'ddtct5b1a','mux B1 TCTXH.4L5 <-> MKD.A5L6', r'$mu_{x}$ [deg]',-50,2,constrval2=50, deadspan=80)
plot_sq_varconstr(ds['ddtct1b2a'],'ddtct1b2a','mux B2 TCTXH.4R1 <-> MKD.A5R6', r'$mu_{x}$ [deg]',-50,2,constrval2=50, deadspan=80)
plot_sq_varconstr(ds['ddtct5b2a'],'ddtct5b2a','mux B2 TCTXH.4R5 <-> MKD.A5R6', r'$mu_{x}$ [deg]',-50,2,constrval2=50, deadspan=80)


## sys.exit()




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




# sys.exit();



ds=pop.StrTable.open('ir1_%s.tfs'%opt)

plot_sq(ds,'muxip1b1',noaxisexp=True)
plot_sq(ds,'muyip1b1',noaxisexp=True)
plot_sq(ds,'muxip1b1_l',noaxisexp=True)
plot_sq(ds,'muyip1b1_l',noaxisexp=True)
plot_sq(ds,'muxip1b1_r',noaxisexp=True)
plot_sq(ds,'muyip1b1_r',noaxisexp=True)

plot_sq(ds,'muxip1b2',noaxisexp=True)
plot_sq(ds,'muyip1b2',noaxisexp=True)
plot_sq(ds,'muxip1b2_l',noaxisexp=True)
plot_sq(ds,'muyip1b2_l',noaxisexp=True)
plot_sq(ds,'muxip1b2_r',noaxisexp=True)
plot_sq(ds,'muyip1b2_r',noaxisexp=True)


ds=pop.StrTable.open('ir5_%s.tfs'%opt)

plot_sq(ds,'muxip5b1',noaxisexp=True)
plot_sq(ds,'muyip5b1',noaxisexp=True)
plot_sq(ds,'muxip5b1_l',noaxisexp=True)
plot_sq(ds,'muyip5b1_l',noaxisexp=True)
plot_sq(ds,'muxip5b1_r',noaxisexp=True)
plot_sq(ds,'muyip5b1_r',noaxisexp=True)

plot_sq(ds,'muxip5b2',noaxisexp=True)
plot_sq(ds,'muyip5b2',noaxisexp=True)
plot_sq(ds,'muxip5b2_l',noaxisexp=True)
plot_sq(ds,'muyip5b2_l',noaxisexp=True)
plot_sq(ds,'muxip5b2_r',noaxisexp=True)
plot_sq(ds,'muyip5b2_r',noaxisexp=True)


ds=pop.StrTable.open('ir2_%s.tfs'%opt)

plot_sq(ds,'muxip2b1',noaxisexp=True)
plot_sq(ds,'muyip2b1',noaxisexp=True)
plot_sq(ds,'muxip2b1_l',noaxisexp=True)
plot_sq(ds,'muyip2b1_l',noaxisexp=True)
plot_sq(ds,'muxip2b1_r',noaxisexp=True)
plot_sq(ds,'muyip2b1_r',noaxisexp=True)

plot_sq(ds,'muxip2b2',noaxisexp=True)
plot_sq(ds,'muyip2b2',noaxisexp=True)
plot_sq(ds,'muxip2b2_l',noaxisexp=True)
plot_sq(ds,'muyip2b2_l',noaxisexp=True)
plot_sq(ds,'muxip2b2_r',noaxisexp=True)
plot_sq(ds,'muyip2b2_r',noaxisexp=True)

ds=pop.StrTable.open('ir8_%s.tfs'%opt)

plot_sq(ds,'muxip8b1',noaxisexp=True)
plot_sq(ds,'muyip8b1',noaxisexp=True)
plot_sq(ds,'muxip8b1_l',noaxisexp=True)
plot_sq(ds,'muyip8b1_l',noaxisexp=True)
plot_sq(ds,'muxip8b1_r',noaxisexp=True)
plot_sq(ds,'muyip8b1_r',noaxisexp=True)

plot_sq(ds,'muxip8b2',noaxisexp=True)
plot_sq(ds,'muyip8b2',noaxisexp=True)
plot_sq(ds,'muxip8b2_l',noaxisexp=True)
plot_sq(ds,'muyip8b2_l',noaxisexp=True)
plot_sq(ds,'muxip8b2_r',noaxisexp=True)
plot_sq(ds,'muyip8b2_r',noaxisexp=True)


ds=pop.StrTable.open('ir4_%s.tfs'%opt)

plot_sq(ds,'muxip4b1',noaxisexp=True)
plot_sq(ds,'muyip4b1',noaxisexp=True)
plot_sq(ds,'muxip4b1_l',noaxisexp=True)
plot_sq(ds,'muyip4b1_l',noaxisexp=True)
plot_sq(ds,'muxip4b1_r',noaxisexp=True)
plot_sq(ds,'muyip4b1_r',noaxisexp=True)

plot_sq(ds,'muxip4b2',noaxisexp=True)
plot_sq(ds,'muyip4b2',noaxisexp=True)
plot_sq(ds,'muxip4b2_l',noaxisexp=True)
plot_sq(ds,'muyip4b2_l',noaxisexp=True)
plot_sq(ds,'muxip4b2_r',noaxisexp=True)
plot_sq(ds,'muyip4b2_r',noaxisexp=True)

ds=pop.StrTable.open('ir6_%s.tfs'%opt)

plot_sq(ds,'muxip6b1',noaxisexp=True)
plot_sq(ds,'muyip6b1',noaxisexp=True)
plot_sq(ds,'muxip6b1_l',noaxisexp=True)
plot_sq(ds,'muyip6b1_l',noaxisexp=True)
plot_sq(ds,'muxip6b1_r',noaxisexp=True)
plot_sq(ds,'muyip6b1_r',noaxisexp=True)

plot_sq(ds,'muxip6b2',noaxisexp=True)
plot_sq(ds,'muyip6b2',noaxisexp=True)
plot_sq(ds,'muxip6b2_l',noaxisexp=True)
plot_sq(ds,'muyip6b2_l',noaxisexp=True)
plot_sq(ds,'muxip6b2_r',noaxisexp=True)
plot_sq(ds,'muyip6b2_r',noaxisexp=True)




ds=pop.StrTable.open('ir3_%s.tfs'%opt)


plot_sq(ds,'muxip3b1',noaxisexp=True)
plot_sq(ds,'muyip3b1',noaxisexp=True)
plot_sq(ds,'muxip3b1_l',noaxisexp=True)
plot_sq(ds,'muyip3b1_l',noaxisexp=True)
plot_sq(ds,'muxip3b1_r',noaxisexp=True)
plot_sq(ds,'muyip3b1_r',noaxisexp=True)

plot_sq(ds,'muxip3b2',noaxisexp=True)
plot_sq(ds,'muyip3b2',noaxisexp=True)
plot_sq(ds,'muxip3b2_l',noaxisexp=True)
plot_sq(ds,'muyip3b2_l',noaxisexp=True)
plot_sq(ds,'muxip3b2_r',noaxisexp=True)
plot_sq(ds,'muyip3b2_r',noaxisexp=True)

ds=pop.StrTable.open('ir7_%s.tfs'%opt)

plot_sq(ds,'muxip7b1',noaxisexp=True)
plot_sq(ds,'muyip7b1',noaxisexp=True)
plot_sq(ds,'muxip7b1_l',noaxisexp=True)
plot_sq(ds,'muyip7b1_l',noaxisexp=True)
plot_sq(ds,'muxip7b1_r',noaxisexp=True)
plot_sq(ds,'muyip7b1_r',noaxisexp=True)

plot_sq(ds,'muxip7b2',noaxisexp=True)
plot_sq(ds,'muyip7b2',noaxisexp=True)
plot_sq(ds,'muxip7b2_l',noaxisexp=True)
plot_sq(ds,'muyip7b2_l',noaxisexp=True)
plot_sq(ds,'muxip7b2_r',noaxisexp=True)
plot_sq(ds,'muyip7b2_r',noaxisexp=True)



ds=pop.StrTable.open('arc_%s.tfs'%opt)
plot_sq(ds,'mux12b1',noaxisexp=True)
plot_sq(ds,'muy12b1',noaxisexp=True)
plot_sq(ds,'mux12b2',noaxisexp=True)
plot_sq(ds,'muy12b2',noaxisexp=True)
plot_sq(ds,'mux23b1',noaxisexp=True)
plot_sq(ds,'muy23b1',noaxisexp=True)
plot_sq(ds,'mux23b2',noaxisexp=True)
plot_sq(ds,'muy23b2',noaxisexp=True)
plot_sq(ds,'mux34b1',noaxisexp=True)
plot_sq(ds,'muy34b1',noaxisexp=True)
plot_sq(ds,'mux34b2',noaxisexp=True)
plot_sq(ds,'muy34b2',noaxisexp=True)
plot_sq(ds,'mux45b1',noaxisexp=True)
plot_sq(ds,'muy45b1',noaxisexp=True)
plot_sq(ds,'mux45b2',noaxisexp=True)
plot_sq(ds,'muy45b2',noaxisexp=True)
plot_sq(ds,'mux56b1',noaxisexp=True)
plot_sq(ds,'muy56b1',noaxisexp=True)
plot_sq(ds,'mux56b2',noaxisexp=True)
plot_sq(ds,'muy56b2',noaxisexp=True)
plot_sq(ds,'mux67b1',noaxisexp=True)
plot_sq(ds,'muy67b1',noaxisexp=True)
plot_sq(ds,'mux67b2',noaxisexp=True)
plot_sq(ds,'muy67b2',noaxisexp=True)
plot_sq(ds,'mux78b1',noaxisexp=True)
plot_sq(ds,'muy78b1',noaxisexp=True)
plot_sq(ds,'mux78b2',noaxisexp=True)
plot_sq(ds,'muy78b2',noaxisexp=True)
plot_sq(ds,'mux81b1',noaxisexp=True)
plot_sq(ds,'muy81b1',noaxisexp=True)
plot_sq(ds,'mux81b2',noaxisexp=True)
plot_sq(ds,'muy81b2',noaxisexp=True)


ds=pop.StrTable.open('rng_%s.tfs'%opt)

plot_sq(ds,'tarsqueeze',log=True)
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

# sys.exit()

########################################################

####################################################

## sys.exit()




#plot_squeeze_all(opt=opt)


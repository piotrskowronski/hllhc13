file1=opt_100_400_400_100.madx
file2=opt_080_320_320_080.madx
bases=( opt_096_384_384_096 opt_092_368_368_092 opt_088_352_352_088 opt_084_336_336_084  )




irs="4 6"
beams=( 1 1 )


npoints=${#bases[@]}
npoints=$((npoints + 1))

#############################################
#############################################
#############################################
#############################################



dopoint()
 {
 
   echo "ttt=$ttt;" > $outfile

   if [ "$b1" -eq 1 ] ; then
     grep kq $file1 | grep -E  $irsel | grep b1 | awk '{print "one_"$0}' >>  $outfile
     grep kq $file2 | grep -E  $irsel | grep b1 | awk '{print "two_"$0}' >> $outfile
     grep kq $file2 | grep -E  $irsel | grep b1 | awk '{print $1 "= one_"$1 "*(1-ttt) + two_"$1 "*ttt;"}' >> $outfile
     grep kq $file2 | grep -E  $irsel | grep b1 | awk '{print "value, "$1", one_"$1", two_"$1" ;"}'       >> $outfile
   fi

   if [ "$b2" -eq 1 ] ; then
     grep kq $file1 | grep -E  $irsel | grep b2 | awk '{print "one_"$0}' >>  $outfile
     grep kq $file2 | grep -E  $irsel | grep b2 | awk '{print "two_"$0}' >> $outfile
     grep kq $file2 | grep -E  $irsel | grep b2 | awk '{print $1 "= one_"$1 "*(1-ttt) + two_"$1 "*ttt;"}' >> $outfile
     grep kq $file2 | grep -E  $irsel | grep b2 | awk '{print "value, "$1", one_"$1", two_"$1" ;"}'       >> $outfile
   fi

   if [ ! -f ${base}_v0.madx ] ; then 
     cp $base.madx ${base}_v0.madx
   fi

   echo "call, file=\"$cdir/$outfile\";" >> ${base}_v0.madx
   
   
   
 
 }

#############################################
#############################################

cdir=`pwd`
echo "=== MPIBTW === cdir=$cdir"


b1=0
b2=0

if [  ${beams[0]} -gt 0 ] ; then
 b1=1
fi

if [  ${beams[1]} -gt 0 ] ; then
 b2=1
fi

echo "=== MPIBTW === npoints=$npoints B1=$b1 B2=$b2"


point=1
while [ "$point" -lt "$npoints" ]; do
  ttt="$point/$npoints"
  n=$((point - 1))
  base=${bases[$n]}

  echo "=== MPIBTW === ttt=$ttt base=$base"
  
  for ir in $irs ; do
    irsel="r$ir|l$ir"
    echo "=== MPIBTW === Selecting IR$ir with $irsel"

    outfile=${base}_ir$ir.madx
    
    dopoint
  done

  
  if [ ! -d /home/skowron/cern/hllhc13/tmp_build ] ; then
    mkdir /home/skowron/cern/hllhc13/tmp_build
  fi
  
  echo "$cdir/${base}_v0.madx" > /home/skowron/cern/hllhc13/tmp_build/lastMatchedOpticFileName.txt

  betxmm=`echo $base | cut -d'_' -f 2`
  betymm=`echo $base | cut -d'_' -f 3`
  
  echo "=== MPIBTW === betxmm=$betxmm betymm=$betxmm"
  
  betx="0.$betxmm"
  bety="0.$betymm"
  
  echo "=== MPIBTW === betx=$betx bety=$betx"
    
  
  cd ~/cern/hllhc13/build/
#  source matchPoint2.sh $betx $bety tmp_build
  cd $cdir
  
  point=$((point + 1))
  
  

done













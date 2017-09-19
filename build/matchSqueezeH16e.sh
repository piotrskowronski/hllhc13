
# use from pass16e all the initial settings 
# match partial mux'es (muxXX_l or and _r ) to get smoother currents
# 
# 

betxa=( 0.31 0.32 0.33 0.34 0.35 0.36 0.37 0.38 0.39 )
betya=( 0.40 0.40 0.40 0.40 0.40 0.40 0.40 0.40 0.40 )

echo "flat/h/pass16e/opt_350_400_400_350.madx" > lastMatchedOpticFileName.txt

npoints=${#betxa[@]}

point=0
while [ "$point" -lt "$npoints" ]; do

  betx=${betxa[$point]}
  bety=${betya[$point]}

 
  echo "=== MatchSqueeze.sh ===   Point $point betx=$betx bety=$bety"

  betxip1mm=$(echo "($betx * 1000)/1" | bc)
  betyip1mm=$(echo "($bety * 1000)/1" | bc)
  betxip5mm=$(echo "($bety * 1000)/1" | bc)
  betyip5mm=$(echo "($betx * 1000)/1" | bc)

  lastMatchedOpticFileName=`cat lastMatchedOpticFileName.txt`
  
  
  newMatchedOpticFileName="flat/h/pass16e/opt_${betxip1mm}_${betyip1mm}_${betxip5mm}_${betyip5mm}.madx"
  if [  $betxip1mm  -lt 100 ] ; then
    newMatchedOpticFileName="flat/h/pass16e/opt_0${betxip1mm}_${betyip1mm}_${betxip5mm}_0${betyip5mm}.madx"
  fi

  if [[ -f $newMatchedOpticFileName ]] ; then
     echo "=== MatchSqueeze.sh ===   $newMatchedOpticFileName exists"
     echo "$newMatchedOpticFileName" > lastMatchedOpticFileName.txt
     
     # copy IP6 settings from the last file into the old pass file which has IP6 filtered
     # grep '^kq.*r4b1\|^kq.*l4b1' $lastMatchedOpticFileName >> $newMatchedOpticFileName
     
  else
     echo "=== MatchSqueeze.sh ===   $newMatchedOpticFileName DOES NOT EXIST"
  fi
  

  
  source matchPoint.sh $betx $bety
  
  point=$((point + 1))
  
  
done

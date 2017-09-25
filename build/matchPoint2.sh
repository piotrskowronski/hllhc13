if [ "$#" -ne 3 ]; then
    echo "Illegal number of parameters"
    return
fi

betx=$1
bety=$2

workdir=/home/skowron/cern/hllhc13/$3

mkdir $workdir

cd  $workdir

cp ../build/job_mkflat.madx .
cp ../build/FixedParametersH17.madx ./FixedParametersStage4.madx

echo "=== MatchPoint.sh ===   betx = $betx bety = $bety "

betxip1mm=$(echo "($betx * 1000)/1" | bc)
betyip1mm=$(echo "($bety * 1000)/1" | bc)
betxip5mm=$(echo "($bety * 1000)/1" | bc)
betyip5mm=$(echo "($betx * 1000)/1" | bc)


echo "=== MatchPoint.sh ===   betxip1mm = $betxip1mm"
echo "=== MatchPoint.sh ===   betxip1mm = $betyip1mm"
echo "=== MatchPoint.sh ===   betxip1mm = $betxip5mm"
echo "=== MatchPoint.sh ===   betxip1mm = $betyip5mm"

lastMatchedOpticFileName=""

echo "=== MatchPoint.sh ===   lastMatchedOpticFileName = $lastMatchedOpticFileName"


prev_tarsqueeze=10000000
tarsqueeze=0

v=1

doagain=1 

while [ "$doagain" -gt 0 ] ; do
  
  
  echo "=== MatchPoint.sh ===   tarsqueeze = $tarsqueeze"

  lastMatchedOpticFileName=`cat lastMatchedOpticFileName.txt`
  echo "=== MatchPoint.sh ===   lastMatchedOpticFileName = $lastMatchedOpticFileName"
  
  
  echo "call,file=\"$lastMatchedOpticFileName\";" > skowronInOut.madx
  echo "v=$v;" >> skowronInOut.madx


  echo "betx_ip1=${betx};  "  > skowronSetBetaStar.madx
  echo "bety_ip1=${bety};  " >> skowronSetBetaStar.madx
  echo "betx_ip5=${bety};  " >> skowronSetBetaStar.madx
  echo "bety_ip5=${betx};  " >> skowronSetBetaStar.madx
  

  
  newMatchedOpticFileName="opt_${betxip1mm}_${betyip1mm}_${betxip5mm}_${betyip5mm}_v${v}.madx"

  echo "=== MatchPoint.sh === newMatchedOpticFileName = $newMatchedOpticFileName" 
  
  
  ~/cern/madx_trunk/madx-linux64-intel job_mkflat.madx > $newMatchedOpticFileName.out
  
  tarsqueeze=`grep tarsqueeze $newMatchedOpticFileName.tar | awk '{printf "%.30f\n", $3 }'`
  
  #tarsqueeze=`printf '%.50f' $tarsqueezee`
  
  echo "=== MatchPoint.sh === v = $v  tarsqueeze = $tarsqueeze"
  
  issmaller=$(echo " $tarsqueeze < $prev_tarsqueeze" | bc)
  echo "=== MatchPoint.sh === issmaller = $issmaller  tarsqueeze = $tarsqueeze "
  oneEmin19=0.0000000000000000001
  istiny=$(echo " $tarsqueeze < $oneEmin19" | bc)
  
  if  [ $istiny -eq 1 ] ; then
    doagain=0
    echo "=== MatchPoint.sh === Fully matched"
  elif [ $issmaller -eq 1 ] ; then
    doagain=1
    echo "=== MatchPoint.sh === NEXT ITERATION"
  else
    if [ $(echo " $tarsqueeze < 0.0001" | bc) -eq 1 ] ; then
      echo "=== MatchPoint.sh === Small enough and bigger then previous"
      doagain=0
    else
      echo "=== MatchPoint.sh === Keep trying, it is still too big"
    fi
  fi
  
  echo "$newMatchedOpticFileName" > lastMatchedOpticFileName.txt
  
  v=$((v + 1))
  
  prev_tarsqueeze=$tarsqueeze

  
  
done

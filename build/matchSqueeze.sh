
betxa=(0.45 0.40 0.35 0.30 0.25 0.20 0.15 0.10 0.095 0.090  0.085  0.080  0.075 )
betya=(0.45 0.40 0.40 0.40 0.40 0.40 0.40 0.40 0.38 0.36 0.34  0.32   0.30  )

#betxa=(0.40 0.40 0.40 0.40 0.40 0.38  0.36   0.34   0.32   0.30  )
#betya=(0.35 0.30 0.20 0.15 0.10 0.095 0.090  0.085  0.080  0.075 )

#betxa=(0.40 0.40 0.40 0.40 0.40 0.40 0.38  0.36   0.34   0.32   0.30  )
#betya=(0.25 0.23 0.20 0.18 0.15 0.10 0.095 0.090  0.085  0.080  0.075 )

echo "slhc/squeeze/opt_500_500_500_500.madx" > lastMatchedOpticFileName.txt

#echo "opt_400_300_300_400_v9.madx" > lastMatchedOpticFileName.txt
npoints=${#betxa[@]}

point=0
while [ "$point" -lt "$npoints" ]; do

  betx=${betxa[$point]}
  bety=${betya[$point]}
  
  echo "=== MatchSqueeze.sh ===   Point $point betx=$betx bety=$bety"
  
  source matchPoint.sh $betx $bety
  
  point=$((point + 1))
  
  
done

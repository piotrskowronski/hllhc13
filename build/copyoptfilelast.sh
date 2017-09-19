betxa=( 500 490 480 475  470 460  450 440 430 425 420 410 400 390 380 375 350 325 300 310 320 330 340 360 370 380 390 275 250 225 200 175 150 125 115 110 105 100 120 130 140 160 170 180 190 100 99  98  97  96  95  94  93  92  91  90   85  80  75 )
betya=( 500 490 480 475  470 460  450 440 430 425 420 410 400 400 400 400 400 400 400 400 400 400 400 400 400 400 400 400 400 400 400 400 400 400 400 400 400 400 400 400 400 400 400 400 400 400 396 392 388 384 380 376 372 368 364 360 340 320 300 )




npoints=${#betxa[@]}
point=0



findlastfile()
{
  i=1
  found=1
  lastbfname=""
  while [[ "$found" -gt 0 ]] ; do
     
     bfname="opt_${betx}_${bety}_${bety}_${betx}_v$i"
     fname="${bfname}.madx"
     
     if [ -f $fname ] ; then
       found=1
       lastbfname=$bfname
     else
       found=0
     fi
    
     #echo "File $fname $found"
    
     i=$((i + 1))
  done
  
}

copylastfile()
{
  lenbetx=${#betx}
  lenbety=${#bety}
  
  if [[  "$lenbetx" -gt 2  &&  "$lenbety" -gt 2  ]] ; then
    newbfname="opt_${betx}_${bety}_${bety}_${betx}"
  elif [[ "$lenbetx" -eq 2  ]] ; then
    newbfname="opt_0${betx}_${bety}_${bety}_0${betx}"
  elif [[ "$lenbety" -eq 2  ]] ; then
    newbfname="opt_${betx}_0${bety}_0${bety}_${betx}"
  else
    
    echo "=== copyoptfilelast.sh ===   Not implemented beta function range $point betx=$betx bety=$bety"
    return
  fi 
  
  cp $lastbfname.madx ../${newbfname}.madx
  cp $lastbfname.madx.tar ../${newbfname}.madx.tar
  
  
  lastbfname=""
  newbfname=""
  
}

pointsHor()
{

   while [[ "$point" -lt "$npoints" ]] ; do

     betx=${betxa[$point]}
     bety=${betya[$point]}

     echo "=== copyoptfilelast.sh ===   Point $point betx=$betx bety=$bety"
     
     findlastfile     

     #echo "=== copyoptfilelast.sh ===   lastbfname = $lastbfname"
     
     if [ -z $lastbfname  ] ; then
       
       echo ""
       echo "=== copyoptfilelast.sh ===   !!!! No file for  $point betx=$betx bety=$bety"
       echo ""
     
     else

       echo "=== copyoptfilelast.sh ===   lastfile = $lastbfname.madx"
       copylastfile
       
     fi
     
     point=$((point + 1))


   done
}

points()
{
   betx=500
   
   while [[ "$betx" -gt 74 ]] ; do

     
     bety=500
     while [[ "$bety" -gt 74 ]] ; do

        #echo "=== copyoptfilelast.sh ===   betx=$betx bety=$bety"

        findlastfile     

        #echo "=== copyoptfilelast.sh ===   lastbfname = $lastbfname"

        if [ -z $lastbfname  ] ; then

          #echo ""
          #echo "=== copyoptfilelast.sh ===   !!!! No file for  $point betx=$betx bety=$bety"
          #echo ""
          nofile=1

        else

          echo "=== copyoptfilelast.sh ===   lastfile = $lastbfname.madx"
          copylastfile

        fi
        
        bety=$((bety - 1))
        
     done
     
     betx=$((betx - 1))


   done
}

 
points

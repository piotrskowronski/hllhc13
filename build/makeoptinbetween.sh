file1=opt_110_400_400_110.madx
file2=opt_100_400_400_100.madx
ttt="0.5"

outfile=opt_105_400_400_105_ir6b1.madx

ir="r4|l4"
ir="r6|l6"






b1=1
b2=0


echo "ttt=$ttt;" > $outfile

if [ "$b1" -eq 1 ] ; then
  grep kq $file1 | grep -E  $ir | grep b1 | awk '{print "one_"$0}' >>  $outfile
  grep kq $file2 | grep -E  $ir | grep b1 | awk '{print "two_"$0}' >> $outfile
  grep kq $file2 | grep -E  $ir | grep b1 | awk '{print $1 "= one_"$1 "*(1-ttt) + two_"$1 "*ttt;"}' >> $outfile
  grep kq $file2 | grep -E  $ir | grep b1 | awk '{print "value, "$1", one_"$1", two_"$1" ;"}'       >> $outfile
fi

if [ "$b2" -eq 1 ] ; then
  grep kq $file1 | grep -E  $ir | grep b2 | awk '{print "one_"$0}' >>  $outfile
  grep kq $file2 | grep -E  $ir | grep b2 | awk '{print "two_"$0}' >> $outfile
  grep kq $file2 | grep -E  $ir | grep b2 | awk '{print $1 "= one_"$1 "*(1-ttt) + two_"$1 "*ttt;"}' >> $outfile
  grep kq $file2 | grep -E  $ir | grep b2 | awk '{print "value, "$1", one_"$1", two_"$1" ;"}'       >> $outfile
fi

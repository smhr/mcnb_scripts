BEGIN {OFS = "\t" ; print "\
#     Time    lHwd     lCOwd   lONwd     wd      ns     bh    bh-bh   mHwd    mCOwd   mONwd    mwd     mns     mbh"}
{print $2,$266,$267,$268,$140,$141,$142,$154,$269,$270,$271,$272,$273,$274}
##$2, $266 ,$267, $268, $140, $141, $142
END {print "\
#     Time    lHwd     lCOwd   lONwd     wd      ns     bh    bh-bh   mHwd    mCOwd   mONwd    mwd     mns     mbh"}

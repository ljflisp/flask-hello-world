<?php
   header("Content-type:text/html;charset=utf-8");
   echo"阿姆斯特朗数:";
   for($num=100;$num<=999;$num++){
     $a=floor($num/100);
     $b=floor(($num%100)/10);
     $c= $num%10;
     $x=$a*$a*$a+$b*$b*$b+$c*$c*$c;
     $y=$num;
     if($x=$num)
       echo $num."";
   }
     
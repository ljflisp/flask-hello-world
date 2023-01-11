<?php
  $k= 12;
  $k1= 1;
  $k2= 0;
  $sum= 0;
  for($i=1;$i<$k;$i++){
    $sum=$k1+$k2;
    $k2=$k1;
    $k1=$sum;
  }
  echo $sum;
?>
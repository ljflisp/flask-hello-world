<?php
  header("Content-type:text/html;charset=utf-8");
   $s=0;
   $n= 1;#最后一天的桃子num
   for($i=1;$i<=10;$i++){
     $s=($n+1)*2;
     $n=$s;
   }
     printf("第一天共摘了%d个桃子.<br>",$s);
?>
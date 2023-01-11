<?php
   header("Content-type:text/html;charset=utf-8");
   define("M",41);
   define("N",3);

   $man=array(0);
   $count=1;
   $i= 0;
   $pos=-1;
   $alive= 2;

   while($count<=N){
     do{
       $pos=($pos+1)%N;
       if(@$man[$i]==0)
         $i++;
       if($i== M){
         $i= 0;
         break;
       }
     }
   while(1);
  $man[$pos]=$count;
  $count++;
   }
arsort($man);
$arr=array_slice($man,0,$alive,true);
echo"约瑟夫排列:";
for($i=0;$i<N;$i++){
  echo"".$man[$i];
}

echo"<nr>L 表示要救的".$alive."个人要放的位置:";
for($i=0;$i<N;$i++){
if(isset($arr[$i])&& $man[$i]== $arr[$i])  echo"L";
else    echo"D";
  if(($i+1)%5== 0)  echo "";
}
?> 
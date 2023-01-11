<?php
  header("Content-type:text/html;charset=utf-8");
  function hanou($n,$x,$y,$z){
    if($n== 1){
      echo"移动片1从'.$s.'到'.$z.''<br>";
    }else{
      hanou($n-1,$x,$z,$y);
      echo"移动片'.$n.'从'$x.'到'$z.";
     hanou($n-1,$x,$y,$z);
    }
  }
    hanou(3,'A','B','C',)
  

?>
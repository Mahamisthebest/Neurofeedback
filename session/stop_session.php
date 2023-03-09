<?php

//path should be changed in accordance with local PC
$path = "stop.txt";
$file2=fopen($path,'w');
fwrite($file2,"Stop");
fclose($file2);

header("location:javascript://history.go(-1)");
// header("Location: ../video/index.html");
?>
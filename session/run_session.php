<?php

$tmp='session1.py';

$command = escapeshellcmd($tmp);

$output = shell_exec($command);

echo $output;

header("Location: ../video/index.html");

?>


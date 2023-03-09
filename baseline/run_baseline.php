<?php

$tmp='baseline.py';
$command = escapeshellcmd($tmp);
$output = shell_exec($command);
echo $output;

?>

<?php
session_start();

include ("../connections.php");
 include("count.php");
		 
	$date=date("d/m/Y");

	if (notExist($connection,$_SESSION["id"],$date)==TRUE){
		insert_data($connection,$_SESSION["id"],$date);
		$ans= get_count($connection,$_SESSION["id"],$date);
	}
	else{
		$ans= get_count($connection,$_SESSION["id"],$date);
	}
	
	$file = "../". $_SESSION["structure"]."/"."session$ans.csv";
	$file1="../".$_SESSION["structure"]."/"."Mean_session$ans.csv";
	$file2a="../".$_SESSION["structure"]."/"."rawdata_session$ans.csv";
	 
		$dest="session_set.csv";
		$dest1="Mean_session.csv";
		$dest2="rawdata.csv";

		rename($dest, $file);
		rename($dest1, $file1);
		rename($dest2, $file2a);


	$ans=$ans+1;
	add_count($connection,$_SESSION["id"],$date,$ans);
	

$path = "stop.txt";
$path1 = "run_file.pid";

	if(file_exists($path)){
		if (!unlink($path)) {  
			echo ("path hasnot been deleted");  
		}  
		else {  
			unlink($path1);
			echo ("path has been deleted");  
		}  
	}
	else{
		echo ("File doesn't exists");
	}
	
header("Location: ../Testing.php");

?>
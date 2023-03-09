
<?php

//Delete this file if there is no need for enumerated files on local PC

/*
	File to get the access time to create enumerated files of threshold and mean
*/

	//used to assign session variables. They can be used in every file.
		//session_start();
	
	//connection file
		include('../connections.php');
	
	//include account file to use the functions in there
			include("../login-authentication.php");
	
/*	//initialize object of account class
		$account = new account($conn);
		
		//get the count from 'access_time' table
			$ans= $account->get_count($_SESSION["userid"],$_SESSION["userdate"]);
*/


	//name files for threshold and mean of data 
		$file = "../".$_SESSION["structure"]."/"."prebaseline.csv";
		$file1="../".$_SESSION["structure"]."/"."prebaselinemean.csv";
        $file2="../".$_SESSION["structure"]."/"."rawdata.csv";
		//get files where the python file stored the csv file
			$dest="baseline.csv";
			$dest1="means_baseline.csv";
			$dest2="rawdata.csv";
		
		//cut the files and paste in respective userid and userdate folder 
			rename($dest, $file);
			rename($dest1, $file1);
			rename($dest2,$file2);

		//store file path in session variable for further use
			$_SESSION["file"]=$file1;

	header("Location: ../testing.php");
?>
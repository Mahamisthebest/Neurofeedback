<?php

/*



Send the data from csv file that are created by the baseline.py script



*/



session_start();

include('../connections.php');



//get the variables

$id = $_SESSION["id"];

$date = date("d/m/Y");







//open the file in read mode

$file = fopen("means_baseline.csv","r");



//set the variables

$row_data =array();

$time = 0;

$band = "";



$row =1;



//check if the same record exists if it doesnot only then insert the data

$sql = "SELECT id,date from baselinemean where id=$id and date='$date'";

$query = mysqli_query( $connection , $sql) or trigger_error(mysqli_error($connection));

	$result = mysqli_num_rows($query);

	

	//get each row of csv in a variable

	while (($data = fgetcsv($file)) != FALSE){

			

			//since data type different or time,channels and band i.e: INT for time, STR for bands and FLOAT for channels

		if($row >= 2){

				//extract band name from each row 

				$band = $data[1];

			

			//push all other values in an array

			for($i=2;$i<16;$i++){

				

				array_push($row_data,$data[$i]);

				

			}

			echo $band;

			print_r($row_data);

			

			if ($result == 0) {				

				//insert into db

				$sql = "INSERT into baselinemean (id,date,bands,channel1,channel2,channel3,channel4,channel5,channel6,channel7,channel8,channel9

				,channel10,channel11,channel12,channel13,channel14) VALUES($id,'$date','$band',$row_data[0],$row_data[1],$row_data[2],$row_data[3],

				$row_data[4],$row_data[5],$row_data[6],$row_data[7],$row_data[8],$row_data[9],$row_data[10],$row_data[11],$row_data[12],$row_data[13])";

				

				$query = mysqli_query( $connection , $sql) or trigger_error(mysqli_error($connection));

				$row_data=array();

				}

					

			else{

				//update db

				$sql = "UPDATE baselinemean set id=$id,date='$date',bands='$band',channel1=$row_data[0],channel2=$row_data[1],channel3=$row_data[2],channel4=$row_data[3],

				channel5=$row_data[4],channel6=$row_data[5],channel7=$row_data[6],channel8=$row_data[7],channel9=$row_data[8],channel10=$row_data[9],channel11=$row_data[10]

				,channel12=$row_data[11],channel13=$row_data[12],channel14=$row_data[13]";

				$query = mysqli_query( $connection , $sql) or trigger_error(mysqli_error($connection));

				$row_data=array();

			}

		}

		$row++; 

	}

	

//close the file

fclose($file);


header("Location: baseline_csv.php");



?>
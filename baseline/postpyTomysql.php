<?php
/*

Send the data from csv file that are created by the baseline.py script

*/

session_start();
include('../connections.php');

//open the file in read mode
//$file = fopen("baseline.csv","r");

//get the variables
$id = $_SESSION["id"];
$date = date("d/m/Y");

// $row_data =array();
// $time = 0;
// $band = "";

// $row =1;
// //get each row of csv in a variable
// while (($data = fgetcsv($file)) != FALSE){
	
// 	//since data type different or time,channels and band i.e: INT for time, STR for bands and FLOAT for channels
// 	if($row >= 2){
// 		//extract time value and band value from each row 
// 		$time = $data[2];
// 		$band = $data[1];
	
// 	//push all other values in an array
// 	for($i=3;$i<17;$i++){
// 		array_push($row_data,$data[$i]);
		
// 	}
// 	echo $time."</br>".$band;
// 	print_r($row_data);
	
// 	//insert into db
// 	$sql = "INSERT into baselinevalues (id,date,bands,time,channel1,channel2,channel3,channel4,channel5,channel6,channel7,channel8,channel9
// 	,channel10,channel11,channel12,channel13,channel14) VALUES($id,'$date','$band',$time,$row_data[0],$row_data[1],$row_data[2],$row_data[3],$row_data[4]
// 	,$row_data[5],$row_data[6],$row_data[7],$row_data[8],$row_data[9],$row_data[10],$row_data[11],$row_data[12],$row_data[13])";
	
// 	$query = mysqli_query( $connection , $sql) or trigger_error(mysqli_error($connection));
// 	$row_data=array();
// 	}
// 	$row++; 
// }
// //close the file
// fclose($file);

//open the file in read mode
$file = fopen("means_baseline.csv","r");

//set the variables
$row_data =array();
$time = 0;
$band = "";

$row =1;
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
	
	//insert into db
	$sql = "INSERT into postbaselinemean (id,date,bands,channel1,channel2,channel3,channel4,channel5,channel6,channel7,channel8,channel9
	,channel10,channel11,channel12,channel13,channel14) VALUES($id,'$date','$band',$row_data[0],$row_data[1],$row_data[2],$row_data[3],
	$row_data[4],$row_data[5],$row_data[6],$row_data[7],$row_data[8],$row_data[9],$row_data[10],$row_data[11],$row_data[12],$row_data[13])";
	
	$query = mysqli_query( $connection , $sql) or trigger_error(mysqli_error($connection));
	$row_data=array();
	}
	$row++; 
}
//close the file
fclose($file);

//unlink("stop.txt");
header("Location: postbaseline_csv.php");

?>
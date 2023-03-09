<?php
/*

	File to set count for each login id on the same date to get count for session files

*/
function notExist($connection,$id,$date)
	{
		$query = mysqli_query($connection,"select * from access_time WHERE date='$date' and id='$id'");
		
		if(mysqli_num_rows($query) == 1) {
			return false;
		}
		else{
			return true;
		}
	}

function get_count($connection,$id,$date){	

		$sql = "SELECT count FROM access_time WHERE date='$date' and id=$id";
		//$result=$connectionsquery($sql);
		$query = mysqli_query($connection,$sql);
		$row = mysqli_num_rows($query);
		while($row = $query->fetch_assoc()){
			$data = $row['count'];
		}
			return $data;

	}
	
function add_count($connection,$id,$date,$i){	
		
		$sql = "UPDATE access_time set count=$i WHERE date='$date' and id=$id";
		$query = mysqli_query($connection,$sql);
	}

function insert_data($connection,$id,$date){
	
	$sql="Insert into access_time(id,date,count) values($id,'$date',1)";
	$query = mysqli_query($connection,$sql);
		echo "Data entered successfully";
	}


?>
<?php
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "refresh";

	$conn = mysqli_connect($servername, $username, $password, $dbname);
	if (!$conn){
		die("Connection failed: " .mysqli_connecet_error());
	}

	$showData = "SELECT * FROM refresh.refresh";
	$data = array();
	$result = mysqli_query($conn, $showData);

	if (mysqli_num_rows($result) > 0){
		while($row = mysqli_fetch_assoc($result)){
			$data[] = $row;
		}
	} else {
		echo "0 results";
	};
	echo json_encode($data);
	mysqli_close($conn);
?>
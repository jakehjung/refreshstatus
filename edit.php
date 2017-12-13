<?php
	$servername = "localhost";
	$username = "root";
	$password = "root";
	$dbname = "refresh";

	$conn = mysqli_connect($servername, $username, $password, $dbname);

    $status = $_GET ['status'];
    $orgid = $_GET ['orgid'];

    $sql="UPDATE refresh SET status = '$status' WHERE orgid = '$orgid'";

    if (mysqli_query($conn, $sql)) {
        echo "Record edited successfully";
    } else {
        echo "Error editing record: " . mysqli_error($conn);
    }

    mysqli_close($conn);
?>


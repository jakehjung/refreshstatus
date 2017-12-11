<?php
	$servername = "localhost";
	$username = "root";
	$password = "root";
	$dbname = "refresh";

	$conn = mysqli_connect($servername, $username, $password, $dbname);

    $orgid = $_GET ['orgid'];

    $sql="DELETE FROM refresh.refresh WHERE orgid = '$orgid'";

    if (mysqli_query($conn, $sql)) {
        echo "Record deleted successfully";
    } else {
        echo "Error deleting record: " . mysqli_error($conn);
    }

    mysqli_close($conn);
?>


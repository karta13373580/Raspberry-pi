<?php
include("light_control.php");

$answer=$_GET['answer'];

$sql = "INSERT INTO rc_server (answer) VALUES ('$answer')";

$result=mysqli_query($conn,$sql);

?>

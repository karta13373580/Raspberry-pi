<?php
include("light_control.php");

$answer=$_GET['answer'];

$sql = "INSERT INTO light_control_table (answer) VALUES ('$answer')";

$result=mysqli_query($conn,$sql);

?>


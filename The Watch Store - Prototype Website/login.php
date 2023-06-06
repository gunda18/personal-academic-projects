<?php 

$host="localhost";
$user="root";
$password="";
$db="registration";

$conn=mysqli_connect($host,$user,$password,$db);

if(isset($_POST['username']))
{
	$u = isset($_POST['username']) ? $_POST['username']:'';
	$p = isset($_POST['password']) ? $_POST['password']:'';

	$sql="select fullname from regtable where username='$u' AND password1='$p' limit 1";
	$result=mysqli_query($conn,$sql);
	if(mysqli_num_rows($result)==1)
	{
		echo '<script type="text/javascript">window.location.href="home.html";
		alert("Logged in Successfully!!");</script>';
		session_start();
		$_SESSION['loggedin'] = true;
		$_SESSION['username'] = $username;
	}
	else
	{
        echo '<script type="text/javascript">alert("Invalid Username or Password");
        window.location.href="login.html";</script>';
		exit();
	}
}
 ?>
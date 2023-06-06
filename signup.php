<?php
$fullname = isset($_POST['fullname']) ? $_POST['fullname']:'';
$username = isset($_POST['username']) ? $_POST['username']:'';
$email = isset($_POST['email']) ? $_POST['email']:'';
$mobile = isset($_POST['number']) ? $_POST['number']:'';
$password1 = isset($_POST['password1']) ? $_POST['password1']:'';
$password2 = isset($_POST['password2']) ? $_POST['password2']:'';
$month = isset($_POST['dobmonth']) ? $_POST['dobmonth']:'';
$day = isset($_POST['dobday']) ? $_POST['dobday']:'';
$year = isset($_POST['dobyear']) ? $_POST['dobyear']:'';
$gender = isset($_POST['gender']) ? $_POST['gender']:'';

if (!empty($fullname) && !empty($username) && !empty($email) && !empty($mobile) && !empty($password1) && !empty($password2)) 
{
	$host = "localhost";
	$dbUsername = "root";
	$dbPassword = "";
	$dbname = "registration";
	$conn = new mysqli($host, $dbUsername, $dbPassword, $dbname);
	if (mysqli_connect_error()) 
	{
        die('Connect Error('. mysqli_connect_errno().')'. mysqli_connect_error());
    }
    else
    {
        $CHECK = "SELECT * FROM regtable WHERE username='$username'";
        $RES  = mysqli_query($conn,$CHECK);
        if (mysqli_num_rows($RES)==0)
        {
    	    $INSERT = "INSERT INTO regtable (fullname, username, email, mobile, password1, password2, month, day, year, gender) VALUES ('$fullname', '$username', '$email', '$mobile', '$password1', '$password2', '$month', '$day', '$year', '$gender')";
            if ($conn->query($INSERT) == TRUE)
            {
                echo '<script type="text/javascript">window.location.href="login.html";
                alert("Registered Successfully!! Login now.");</script>';
            }
        }
        else
        {
            echo '<script type="text/javascript">window.location.href="javascript:history.go(-1)";
                alert("Username already taken.Try another one.");</script>'; 
        }
    }
}
else
{
    header("Location: signup.html");
	die();
}
?>
<?php
session_start();
if ($_SESSION['loggedin'] == true) {
    echo '<script type="text/javascript">window.location.href="loggedin.html";
		</script>';
} else {
    header("Location: login.html");
}
?>
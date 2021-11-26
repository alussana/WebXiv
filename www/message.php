<?php
date_default_timezone_set('Australia/Melbourne');
$date = date('m/d/Y h:i:s a', time());
$address = $_POST["address"];
$name = $_POST["name"];
$message = $_POST["message"];
$txt = "--\ndate: ".$date."|_|\nname: ".$name."|_|\naddress: ".$address."|_|\ntext: ".$message;
getcwd();
file_put_contents('/usr/share/nginx/html/inbox/inbox.txt', $txt.PHP_EOL , FILE_APPEND | LOCK_EX);
header("Location: sent.html");
die();
?>
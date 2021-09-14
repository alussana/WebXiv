<?php
$address = $_POST["address"];
$name = $_POST["name"];
$message = $_POST["message"];
$txt = "--\nname: ".$name."\naddress: ".$address."\n".$message;
getcwd();
file_put_contents('/usr/share/nginx/html/inbox/inbox.txt', $txt.PHP_EOL , FILE_APPEND | LOCK_EX);
header("Location: sent.html");
die();
?>
<?php
$address = $_POST["address"];
$name = $_POST["name"];
$message = $_POST["message"];
$txt = "NEW_MESSAGE\nname: ".$name."\naddress: ".$address."\n".$message."\n";
getcwd();
file_put_contents('/usr/share/nginx/html/inbox/inbox.txt', $txt.PHP_EOL , FILE_APPEND | LOCK_EX);
header("Location: message.php");
?>
<?php
$address = $_POST["address"];
$name = $_POST["name"];
$message = $_POST["message"];
$txt = "\nname: ".$name."\naddress: ".$address."\nmessage:\n".$message;
getcwd();
file_put_contents('/messages/inbox.txt', $txt.PHP_EOL , FILE_APPEND | LOCK_EX);
header("Location: message.php");
?>
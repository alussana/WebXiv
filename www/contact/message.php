<?php
$address = $_POST["address"];
$name = $_POST["name"];
$message = $_POST["message"];
$txt = "\nname: ".$name."\naddress: ".$address."\nmessage:\n".$message;
file_put_contents('inbox.txt', $txt.PHP_EOL , FILE_APPEND | LOCK_EX);
header("Location: message.php");
?>
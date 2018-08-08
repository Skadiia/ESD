<?php

$fh = fopen('index.php','r');
while ($line = fgets($fh)) {
	echo($line);
}
fclose($fh);
?>
<?php
$im = "1";
$data = "hello";
$result = shell_exec("python3 my_python_script.py $im $data");
$resp = intval(trim($result));
if ($resp==1){
    echo $im + ".png";
    echo '<img src="'+$im+".png"+'">';
}
?>
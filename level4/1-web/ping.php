<?php
$status = "c4ca4238a0b923820dcc509a6f75849b";

function waf($cmd){
	
	$black_list = ["$", "{", "}", "`", ";", "&", "|", "(", ")", "\"", "'", "~", "!", "@", "#", "%", "^", "*", "[", "]", "\\", ":", "-", "_"];
	
	foreach($black_list as $k => $v) {
		if(strpos($cmd, $v) !== false){ 
			echo 'IP包含恶意字符.';
			exit();
		}
	}
	
}

if(isset($_POST["ip"]) && $_POST["ip"] != "") {
    waf($_POST["ip"]);

	$command = "ping -nc 1 " . $_POST["ip"] . " && echo '".$status."'";
	
	exec($command, $cmd_result);	
	$cmd_result = implode("\n", $cmd_result);
	
	if(strpos($cmd_result, $status) !== false){ 
		echo 'IP Ping 成功.';
		exit();
	} else {
		echo 'IP Ping 失败.';
		exit();
	}
	
} else {
	echo "鎻愪氦鐨勬暟鎹负绌�.";
}

?>
#!/data/data/com.termux/files/usr/bin/php
<?php
error_reporting(0);
system("clear");
$green = "\e[92m";
$red   = "\e[91m";
function input($pesan) {
    global $green;
    echo "$green $pesan >>> ";
}
function asciiart() {
    system("clear");
    echo "\n \e[93m";
   _____   __    _ __                           
    /  '  /  )  ' )  )            _/_           
 ,-/-,   /--<    /--'  _  __.  _. /   o __ ____ 
(_/     /___/_  /  \_ </_(_/|_(__<__ <_(_)/ / <_";
    echo "\n \e[36m
 Author  : Cvar1984
 Code    : PHP
 Github  : http://github.com/Cvar1984
 Team    : Blackhole Security
 Version : 1.4 ( Alpha )
 Date    : 28-01-2018";
}
asciiart();
echo "\n$red =========================== Cvar1984 ))=====(@)>\n";
require_once('lib/fb.php');
$rand = array(
    "1",
    "2",
    "3",
    "4",
    "7",
    "8"
);
input("Username");
$user = trim(fgets(STDIN, 1024));
input("Password");
echo "\033[0;30m";
$pass = trim(fgets(STDIN, 1024));
echo "$red =========================== Cvar1984 ))=====(@)> \n";
echo " (1)Like\n";
echo " (2)Love\n";
echo " (3)Wow\n";
echo " (4)Haha\n";
echo " (7)Sad\n";
echo " (8)Angry\n";
echo " (0)Random\n";
echo "$red =========================== Cvar1984 ))=====(@)> \n";
input("Male Reaction");
$r_male = trim(fgets(STDIN, 1024));
if ($r_male == "0") {
    $r_male = array_rand($rand);
}
echo "$red =========================== Cvar1984 ))=====(@)> \n";
echo " (1)Like\n";
echo " (2)Love\n";
echo " (3)Wow\n";
echo " (4)Haha\n";
echo " (7)Sad\n";
echo " (8)Angry\n";
echo " (0)Random\n";
echo "$red =========================== Cvar1984 ))=====(@)> \n";
input("Female Reaction");
$r_female = trim(fgets(STDIN, 1024));
if ($r_female == "0") {
    $r_female = array_rand($rand);
}
input("Count");
$max_status = trim(fgets(STDIN, 1024));
input("Token");
$token = trim(fgets(STDIN, 1024));
echo "$red =========================== Cvar1984 ))=====(@)>$green\n";
$config['cookie_file'] = 'cookie.txt';
if (!file_exists($config['cookie_file'])) {
    $fp = @fopen($config['cookie_file'], 'w');
    @fclose($fp);
} else {
    $fp = @fopen($config['cookie_file'], 'w+');
    @fclose($fp);
}
$reaction = new Reaction();
$reaction->send_reaction($user, $pass, $token, $r_male, $r_female, $max_status);
?>

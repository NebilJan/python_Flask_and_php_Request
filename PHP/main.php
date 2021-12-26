<!DOCTYPE html>
<html>
<head>
<title>
Send Request
</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">

</head>
<style>
*{
margin:0;
padding:0;
outline:none;

}
body{
background:dodgerblue;
text-align:center;
}
form{
width:95%;
height:400px;
background:white;
margin:20px auto;
}
input{
border:1px solid rgba(0,0,0,0.30);;
width:50%;
height:38px;
padding:2px;
border-radius:8px;
margin-top:18px;;

}
.txt{
padding-bottom:40px;
}
input::placeholder{
color:green;
}
.btn{
background:dodgerblue;
color:white;
font-size:16px;
}
</style>
<body>
<!--
Flask app running log
You host the action 
-->
<form action="http://127.0.0.1/users"  method="POST">
<br>
<p>
■ Send Message ■</p>
<input type="text" name="user" placeholder="Username ..." id="user"/>
<br>
<input type="text" placeholder="message ..." name="msg" class="txt"/>
<br>
<input type="submit" value="Send" name="btn" class="btn"/>



</form>

</body>

</html>

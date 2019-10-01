<html>
<head>
<title>Stationary shop</title>
</head>
<body>
<h1>Welcome to cdac stationary shop</h1>
<p1> **** list of Books ****</p1>
<p2> Dated -August , 02 ,2019</p2>
<ul>
<?php
$json = file_get_contents('http://book-service/');
$obj = json_decode($json);
$books = $obj->books;
foreach($books as $book)
{
   echo "<li>$book</li>";
}

?>
</ul>
</body>
</htnl>



	

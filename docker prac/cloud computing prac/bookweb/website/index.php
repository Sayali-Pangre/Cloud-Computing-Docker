<html>
  <head>
    <title>stationary shop</title>
  </head>
  <body>
    <h1>welcome to cdac stationary shop</h1>
    <p1>****** list of books****</p1>
    <p2>dated - august,02,2019</p2>
    <ul>
      <?php
      $json=file_get_contents
('http://book-service/');
$obj=json_decode($json);
$books=$obj->books;
foreach ($books as $book)
{
echo "<li>$book</li>";
}
      ?>
</ul>
</body>
</html>

<?php
/* === Conexão em MySql
    $pdo = new PDO('mysql:host=localhost;dbname=creche_imaginar', 'root', 'ivanoel1987');
    $pdo->exec("set names utf8");
==*/
/* === Conexão em PostgreSQL ==*/
    $pdo = new PDO('pgsql:user=postgres dbname=creche_imaginar password=ivanoel1987');
    $pdo->exec("set names utf8");


?>
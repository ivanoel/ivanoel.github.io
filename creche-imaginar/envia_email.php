<?php
$nome = $_POST['name'];
$mail = $_POST['email'];
$msg = $_POST['comments'];

require 'vendor/autoload.php'; // If you're using Composer (recommended)

$email = new \SendGrid\Mail\Mail(); 
$email->setFrom("atendimento@crecheimaginar.com");
$email->setSubject("Mensagem do Atendimento.");
$email->addTo("ivanoel_33@hotmail.com");
$email->addContent("text/html", "Olá, <br><br>Mensagem do Atendimento Creche Imaginar.
	<br><br>Nome: $nome<br>Email: $mail <br>Mensagem: $msg");

$sendgrid = new \SendGrid('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');
$response = $sendgrid->send($email);
if (isset($_POST['$response'])) {
	print "<script>window.location='index.html';alert('$nome, sua mensagem foi enviada com sucesso! Estaremos retornando em breve');</script>";
}else{
	print "<script>window.location='fale-conosco.php';alert('$nome, falha ao enviar email!');</script>";
}


?>

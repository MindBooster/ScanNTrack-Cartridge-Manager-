<?php
include('connection.php');
?>
<!DOCTYPE html>
<html>
<body style="background-color: aqua;">
<center>
<h2>issue cartridge</h2>

<form action="/action_page.php">
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" ><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" ><br>
  <label for="cartridge model">cartridge model</label><br>
  <input type="text" id ="cartridge model" name="cmodel"><br>
  <label for="cartridge brand">cartridge brand</label><br>
  <input type="text" id = "cartridge brand" name="cbrand><br><br>
  <input type="submit" value="Submit" class="submit" name="submit">
</form> 

<p>If you click the "Submit" button, the form-data will be sent to a page called "/action_page.php".</p>

</center>
</body>
</html>

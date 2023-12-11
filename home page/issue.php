<?php
    include('connection.php');
    if (isset($_POST['submit'])) {
        $fname = $_POST['fname'];
        $lname = $_POST['lname'];
        $catridge_model = $_POST['cmodel'];
        $catridge_brand = $_POST['cbrand'];

        $sql = "select * from logindetails where fname='$fname' and lname='$lname' and cmodel='$catridge_model and cbrand='$catridge_brand'";
  
        $result = mysqli_query($conn, $sql);  
        $row = mysqli_fetch_array($result, MYSQLI_ASSOC);  
        $count = mysqli_num_rows($result);  

        if (mysqli_num_rows($result) > 0) {
            // Output data of each row
            while($row = mysqli_fetch_assoc($result)) {
                echo "ID: " . $row["id"]. " - Name: " . $row["name"]. " - Description: " . $row["description"]. " - Price: " . $row["price"]. "<br>";
            }
        } else {
            echo "0 results";
    }
}
?>
<?php
    // Create connection
    $db  = new mysqli("127.0.0.1", "root", "password", "slippers");
    // Check connection
    if ($db->connect_error) {
        die("&e=0");
    }

    // Query user data from the database
    $data = $db->query("SELECT * FROM users WHERE username = '" . $db->real_escape_string($_POST["Username"]) . "'");

    if ($data->num_rows > 0) { // If the user was found
        $user = mysqli_fetch_assoc($data);
    } else { // If the user was not found
        die("&e=100");
    }

    // Authenticate login
    if (password_verify($_POST["Password"], $user["password"])) { // If the password is correct
        // Formats item array
        $items = explode(",", $user["items"]);
        $items = str_replace(array("[", "]", "\"", " "), "", $items);
        $items = implode("|", $items);
        $member = "1";

        die("&s=0&rt=0&str=0&crumb=" .
        $user["id"] . "|" .
        $user["username"] . "|" .
        $user["color"] . "|" .
        $user["head"] . "|" .
        $user["face"] . "|" .
        $user["neck"] . "|" .
        $user["body"] . "|" .
        $user["hand"] . "|" .
        $user["feet"] . "|" .
        $user["pin"] . "|" .
        $user["background"] .
        "|0|0|0|" . $member . "|0" .
        "&il=" . $items .
        "&c=" . $user["coins"] .
        "&bl=" .
        "&nl=" .
        "&k1=" . $user["loginKey"] .
        "&ed=" . "86400" .
        "&jd=" . "2018-1-1");
    } else { // If the password is incorrect
        die("&e=101");
    }
?>

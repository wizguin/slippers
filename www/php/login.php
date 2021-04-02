<?php

    class Login {

        const HOST = "127.0.0.1";
        const USER = "root";
        const PASSWORD = "password";
        const DATABASE = "slippers";

        private $db;

        function __construct($username, $password) {
            $this->db = new mysqli(self::HOST, self::USER, self::PASSWORD, self::DATABASE);

            $this->testConnection();
            $this->login($username, $password);
        }

        function testConnection() {
            if ($this->db->connect_error) {
                die("&e=0");
            }
        }

        function login($username, $password) {
            $user = $this->getUser($username);

            $this->verifyPassword($password, $user);
            $this->returnUser($user);
        }

        function getUser($username) {
            $escapedUsername = $this->db->real_escape_string($username);

            $statement = $this->db->prepare("SELECT * FROM users WHERE username = ?");
            $statement->bind_param("s", $escapedUsername);
            $statement->execute();
            $result = $statement->get_result();

            if ($result->num_rows > 0) {
                // User found
                return mysqli_fetch_assoc($result);
            }

            // User not found
            die("&e=100");
        }

        function verifyPassword($password, $user) {
            if (!password_verify($password, $user["password"])) {
                // Incorrect password
                die("&e=101");
            }
        }

        function returnUser($user) {
            $items = $this->getItems($user);
            $crumb = $this->getCrumb($user);

            die("&s=0&rt=0&str=0&crumb=" . $crumb  .
                "&il=" . $items .
                "&c=" . $user["coins"] .
                "&bl=" .
                "&nl=" .
                "&k1=" . $user["loginKey"] .
                "&ed=" . "86400" .
                "&jd=" . "2018-1-1"
            );
        }

        function getItems($user) {
            $items = [];

            $statement = $this->db->prepare("SELECT itemId FROM inventory WHERE userId = ?");
            $statement->bind_param("s", $user["id"]);
            $statement->execute();
            $result = $statement->get_result();

            while ($row = $result->fetch_assoc()) {
                array_push($items, $row["itemId"]);
            }

            return implode("|", $items);
        }

        function getCrumb($user) {
            $member = "1";

            return implode("|", array(
                $user["id"],
                $user["username"],
                $user["color"],
                $user["head"],
                $user["face"],
                $user["neck"],
                $user["body"],
                $user["hand"],
                $user["feet"],
                $user["flag"],
                $user["photo"],
                "0", "0", "0", $member, "0"
            ));
        }

    }

    New Login(
        $_POST["Username"],
        $_POST["Password"]
    );

?>

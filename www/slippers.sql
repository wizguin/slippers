-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 27, 2018 at 09:37 PM
-- Server version: 10.1.29-MariaDB
-- PHP Version: 7.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `slippers`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL,
  `loginKey` text NOT NULL,
  `rank` int(1) NOT NULL,
  `banned` int(1) NOT NULL,
  `coins` int(11) NOT NULL,
  `items` text NOT NULL,
  `buddies` text NOT NULL,
  `head` int(11) NOT NULL,
  `face` int(11) NOT NULL,
  `neck` int(11) NOT NULL,
  `body` int(11) NOT NULL,
  `hand` int(11) NOT NULL,
  `feet` int(11) NOT NULL,
  `color` int(11) NOT NULL,
  `photo` int(11) NOT NULL,
  `flag` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `loginKey`, `rank`, `banned`, `coins`, `items`, `buddies`, `head`, `face`, `neck`, `body`, `hand`, `feet`, `color`, `photo`, `flag`) VALUES
(1, 'User', '$2y$10$gB2PVvlGm30WSExn87on0.2httR7onfZFISHt92czCiHrvsB48O3m', 'MgBaHaKJfhGIXT8', 2, 0, 10000, '[\"413\", \"403\", \"201\", \"404\", \"401\", \"405\", \"220\", \"131\", \"103\", \"408\", \"212\", \"481\", \"106\", \"301\", \"244\", \"412\", \"252\", \"219\", \"221\", \"101\", \"214\", \"102\", \"503\", \"8\", \"1\", \"2\", \"3\", \"4\", \"5\", \"6\", \"7\", \"9\", \"10\", \"11\", \"12\", \"452\", \"172\", \"484\", \"502\", \"410\", \"222\", \"500\", \"501\", \"504\", \"505\", \"506\", \"507\", \"508\", \"509\", \"510\", \"511\", \"512\", \"513\", \"514\", \"515\", \"516\", \"517\", \"518\", \"519\", \"235\", \"234\", \"417\", \"453\", \"418\", \"402\", \"233\", \"107\", \"800\", \"352\", \"176\", \"175\", \"351\", \"363\", \"414\", \"173\", \"237\", \"238\", \"421\", \"420\", \"406\", \"253\", \"456\", \"108\", \"171\", \"419\", \"216\", \"451\", \"422\", \"240\", \"424\", \"174\", \"218\", \"262\", \"110\", \"550\", \"263\", \"425\", \"520\", \"524\", \"522\", \"521\", \"523\", \"407\", \"366\", \"423\", \"181\", \"261\", \"551\"]\r\n', '[]', 413, 0, 0, 0, 0, 0, 4, 0, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

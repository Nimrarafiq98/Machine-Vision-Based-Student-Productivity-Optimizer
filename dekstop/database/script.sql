-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: db_attendance
-- ------------------------------------------------------
-- Server version	8.0.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `new_section`
--

DROP TABLE IF EXISTS `new_section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `new_section` (
  `section_Id` int(11) NOT NULL,
  `section_name` varchar(45) NOT NULL,
  PRIMARY KEY (`section_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new_section`
--

LOCK TABLES `new_section` WRITE;
/*!40000 ALTER TABLE `new_section` DISABLE KEYS */;
INSERT INTO `new_section` VALUES (1,'A'),(2,'B'),(3,'C'),(4,'D');
/*!40000 ALTER TABLE `new_section` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_attendance`
--

DROP TABLE IF EXISTS `tbl_attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_attendance` (
  `att_ID` int(11) NOT NULL AUTO_INCREMENT,
  `reg_ID` int(11) DEFAULT NULL,
  `sub_ID` int(11) NOT NULL,
  `att_attendance` tinyint(4) DEFAULT NULL,
  `att_date` date DEFAULT NULL,
  `sec_ID` int(11) NOT NULL,
  `ses_ID` int(11) DEFAULT NULL,
  `att_productivity` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`att_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_attendance`
--

LOCK TABLES `tbl_attendance` WRITE;
/*!40000 ALTER TABLE `tbl_attendance` DISABLE KEYS */;
INSERT INTO `tbl_attendance` VALUES (21,12,12,1,'2020-06-19',18,21,'Inactive'),(22,13,12,1,'2020-06-19',19,22,'Inactive'),(23,14,13,NULL,'2020-06-19',19,21,'Inactive');
/*!40000 ALTER TABLE `tbl_attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_registration`
--

DROP TABLE IF EXISTS `tbl_registration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_registration` (
  `reg_ID` int(11) NOT NULL AUTO_INCREMENT,
  `reg_firstname` varchar(45) NOT NULL,
  `reg_lastname` varchar(45) NOT NULL,
  `reg_email` varchar(45) NOT NULL,
  `reg_session` int(11) DEFAULT NULL,
  `reg_section` int(11) DEFAULT NULL,
  `reg_department` varchar(45) DEFAULT NULL,
  `reg_designation` varchar(45) DEFAULT NULL,
  `reg_registration` varchar(45) NOT NULL,
  PRIMARY KEY (`reg_ID`),
  UNIQUE KEY `reg_email_UNIQUE` (`reg_email`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_registration`
--

LOCK TABLES `tbl_registration` WRITE;
/*!40000 ALTER TABLE `tbl_registration` DISABLE KEYS */;
INSERT INTO `tbl_registration` VALUES (12,'Anum','Tahir','anumrahir242@gmail.com',21,18,'Computer science',NULL,'2016-cs-359'),(13,'Nimra','Rafique','nimrarafique42@gmail.com',22,19,'Computer science',NULL,'2016-cs-355'),(14,'Hafza','Khan','hafzakhan22@gmail.com',21,19,'Computer science',NULL,'2016-cs-345');
/*!40000 ALTER TABLE `tbl_registration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_section`
--

DROP TABLE IF EXISTS `tbl_section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_section` (
  `sec_ID` int(11) NOT NULL AUTO_INCREMENT,
  `sec_name` varchar(45) NOT NULL,
  `ses_ID` int(11) NOT NULL,
  PRIMARY KEY (`sec_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_section`
--

LOCK TABLES `tbl_section` WRITE;
/*!40000 ALTER TABLE `tbl_section` DISABLE KEYS */;
INSERT INTO `tbl_section` VALUES (17,'A',21),(18,'B',21),(19,'A',22),(20,'C',22);
/*!40000 ALTER TABLE `tbl_section` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_session`
--

DROP TABLE IF EXISTS `tbl_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_session` (
  `ses_ID` int(11) NOT NULL AUTO_INCREMENT,
  `ses_name` int(11) NOT NULL,
  PRIMARY KEY (`ses_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_session`
--

LOCK TABLES `tbl_session` WRITE;
/*!40000 ALTER TABLE `tbl_session` DISABLE KEYS */;
INSERT INTO `tbl_session` VALUES (21,2016),(22,2017);
/*!40000 ALTER TABLE `tbl_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_subject`
--

DROP TABLE IF EXISTS `tbl_subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_subject` (
  `sub_ID` int(11) NOT NULL AUTO_INCREMENT,
  `ses_ID` int(11) NOT NULL,
  `sub_name` varchar(45) NOT NULL,
  PRIMARY KEY (`sub_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_subject`
--

LOCK TABLES `tbl_subject` WRITE;
/*!40000 ALTER TABLE `tbl_subject` DISABLE KEYS */;
INSERT INTO `tbl_subject` VALUES (11,21,'Programming Fundamentals'),(12,22,'Computer Networks'),(13,21,'Leadership Strategies'),(14,22,'Web development');
/*!40000 ALTER TABLE `tbl_subject` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-19  9:34:41

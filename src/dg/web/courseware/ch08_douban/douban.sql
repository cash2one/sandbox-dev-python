/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50535
Source Host           : localhost:3306
Source Database       : douban

Target Server Type    : MYSQL
Target Server Version : 50535
File Encoding         : 65001

Date: 2015-04-26 22:52:53
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for focus
-- ----------------------------
DROP TABLE IF EXISTS `focus`;
CREATE TABLE `focus` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `focus_id` int(11) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `focus_id` (`focus_id`),
  KEY `uid` (`uid`),
  CONSTRAINT `focus_ibfk_1` FOREIGN KEY (`focus_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `focus_ibfk_2` FOREIGN KEY (`uid`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of focus
-- ----------------------------

-- ----------------------------
-- Table structure for forum
-- ----------------------------
DROP TABLE IF EXISTS `forum`;
CREATE TABLE `forum` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `content` text,
  `owner` int(11) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `owner` (`owner`),
  CONSTRAINT `forum_ibfk_1` FOREIGN KEY (`owner`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of forum
-- ----------------------------
INSERT INTO `forum` VALUES ('1', 'dfs', 'sdfsdf', '1', '2015-04-26 10:06:45', null);
INSERT INTO `forum` VALUES ('2', 'sdf', 'dfdfd', '14', null, null);
INSERT INTO `forum` VALUES ('3', '小组4', '发帖', '14', null, null);
INSERT INTO `forum` VALUES ('4', '小组4发帖', '帖子内容', '14', null, null);
INSERT INTO `forum` VALUES ('5', '小组2帖子', '小组2第一个帖子', '14', null, null);
INSERT INTO `forum` VALUES ('6', '搭讪是一门技巧性很强的学问么', '叔叔，我们不约！！！！！', '14', null, null);

-- ----------------------------
-- Table structure for groups
-- ----------------------------
DROP TABLE IF EXISTS `groups`;
CREATE TABLE `groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `description` text,
  `owner` int(11) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`) USING BTREE,
  KEY `owner` (`owner`),
  CONSTRAINT `groups_ibfk_1` FOREIGN KEY (`owner`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of groups
-- ----------------------------
INSERT INTO `groups` VALUES ('1', 'xiao', '第一个小组', '1', '2015-04-26 10:02:58', null);
INSERT INTO `groups` VALUES ('2', '', '', null, null, null);
INSERT INTO `groups` VALUES ('3', 'sdf', 'sdfsdfsdf', null, null, null);
INSERT INTO `groups` VALUES ('4', 'sddfs', 'sdfsdfsdf', '14', null, null);
INSERT INTO `groups` VALUES ('5', '就爱搭讪', '关注搭讪技巧，学习交友能力', '14', null, null);

-- ----------------------------
-- Table structure for group_forum
-- ----------------------------
DROP TABLE IF EXISTS `group_forum`;
CREATE TABLE `group_forum` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gid` int(11) DEFAULT NULL,
  `fid` int(11) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fid` (`fid`),
  KEY `group_forum_ibfk_2` (`gid`),
  CONSTRAINT `group_forum_ibfk_1` FOREIGN KEY (`fid`) REFERENCES `forum` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `group_forum_ibfk_2` FOREIGN KEY (`gid`) REFERENCES `groups` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of group_forum
-- ----------------------------
INSERT INTO `group_forum` VALUES ('1', '1', '1', '2015-04-26 10:07:03');
INSERT INTO `group_forum` VALUES ('2', '4', '1', null);
INSERT INTO `group_forum` VALUES ('3', '4', '3', null);
INSERT INTO `group_forum` VALUES ('4', '4', '4', null);
INSERT INTO `group_forum` VALUES ('5', '2', '5', null);
INSERT INTO `group_forum` VALUES ('6', '5', '6', null);

-- ----------------------------
-- Table structure for group_user
-- ----------------------------
DROP TABLE IF EXISTS `group_user`;
CREATE TABLE `group_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gid` int(11) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `gid` (`gid`) USING BTREE,
  KEY `uid` (`uid`),
  CONSTRAINT `group_user_ibfk_1` FOREIGN KEY (`gid`) REFERENCES `groups` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `group_user_ibfk_2` FOREIGN KEY (`uid`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of group_user
-- ----------------------------

-- ----------------------------
-- Table structure for mail
-- ----------------------------
DROP TABLE IF EXISTS `mail`;
CREATE TABLE `mail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `content` text,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `is_read` int(11) DEFAULT '0',
  `main_id` int(11) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `from_id` (`from_id`),
  KEY `to_id` (`to_id`),
  CONSTRAINT `mail_ibfk_1` FOREIGN KEY (`from_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `mail_ibfk_2` FOREIGN KEY (`to_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mail
-- ----------------------------

-- ----------------------------
-- Table structure for reply
-- ----------------------------
DROP TABLE IF EXISTS `reply`;
CREATE TABLE `reply` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fid` int(11) DEFAULT NULL,
  `content` text,
  `parent_id` int(11) DEFAULT NULL,
  `parent_content` text,
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fid` (`fid`),
  CONSTRAINT `reply_ibfk_1` FOREIGN KEY (`fid`) REFERENCES `forum` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of reply
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `passwd` varchar(255) DEFAULT NULL,
  `mobilephone` int(11) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  `is_avaliable` int(11) DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'no1', '001@test.com', 'sfsd', null, null, null, null, '1');
INSERT INTO `user` VALUES ('2', '', '', '', null, null, '0000-00-00 00:00:00', null, '1');
INSERT INTO `user` VALUES ('10', 'dd', 'dd', 'dd', null, null, '0000-00-00 00:00:00', null, '1');
INSERT INTO `user` VALUES ('11', 'ccc', 'qqq', 'aaa', null, null, '0000-00-00 00:00:00', null, '1');
INSERT INTO `user` VALUES ('13', 'd的', 'qq', 'b2ca678b4c936f905fb82f2733f5297f', null, null, '0000-00-00 00:00:00', null, '1');
INSERT INTO `user` VALUES ('14', '123', '123', '202cb962ac59075b964b07152d234b70', null, null, '0000-00-00 00:00:00', null, '1');
INSERT INTO `user` VALUES ('15', '321', '321', 'caf1a3dfb505ffed0d024130f58c5cfa', null, null, '0000-00-00 00:00:00', null, '1');

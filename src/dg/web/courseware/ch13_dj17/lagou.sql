/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50535
Source Host           : localhost:3306
Source Database       : lagou

Target Server Type    : MYSQL
Target Server Version : 50535
File Encoding         : 65001

Date: 2015-06-06 19:05:15
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add category1', '7', 'add_category1');
INSERT INTO `auth_permission` VALUES ('20', 'Can change category1', '7', 'change_category1');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete category1', '7', 'delete_category1');
INSERT INTO `auth_permission` VALUES ('22', 'Can add category2', '8', 'add_category2');
INSERT INTO `auth_permission` VALUES ('23', 'Can change category2', '8', 'change_category2');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete category2', '8', 'delete_category2');
INSERT INTO `auth_permission` VALUES ('25', 'Can add company', '9', 'add_company');
INSERT INTO `auth_permission` VALUES ('26', 'Can change company', '9', 'change_company');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete company', '9', 'delete_company');
INSERT INTO `auth_permission` VALUES ('28', 'Can add django migrations', '10', 'add_djangomigrations');
INSERT INTO `auth_permission` VALUES ('29', 'Can change django migrations', '10', 'change_djangomigrations');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete django migrations', '10', 'delete_djangomigrations');
INSERT INTO `auth_permission` VALUES ('31', 'Can add job', '11', 'add_job');
INSERT INTO `auth_permission` VALUES ('32', 'Can change job', '11', 'change_job');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete job', '11', 'delete_job');
INSERT INTO `auth_permission` VALUES ('34', 'Can add job apply', '12', 'add_jobapply');
INSERT INTO `auth_permission` VALUES ('35', 'Can change job apply', '12', 'change_jobapply');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete job apply', '12', 'delete_jobapply');
INSERT INTO `auth_permission` VALUES ('37', 'Can add job feedback', '13', 'add_jobfeedback');
INSERT INTO `auth_permission` VALUES ('38', 'Can change job feedback', '13', 'change_jobfeedback');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete job feedback', '13', 'delete_jobfeedback');
INSERT INTO `auth_permission` VALUES ('40', 'Can add resume', '14', 'add_resume');
INSERT INTO `auth_permission` VALUES ('41', 'Can change resume', '14', 'change_resume');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete resume', '14', 'delete_resume');
INSERT INTO `auth_permission` VALUES ('43', 'Can add sender valid', '15', 'add_sendervalid');
INSERT INTO `auth_permission` VALUES ('44', 'Can change sender valid', '15', 'change_sendervalid');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete sender valid', '15', 'delete_sendervalid');
INSERT INTO `auth_permission` VALUES ('46', 'Can add study experience', '16', 'add_studyexperience');
INSERT INTO `auth_permission` VALUES ('47', 'Can change study experience', '16', 'change_studyexperience');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete study experience', '16', 'delete_studyexperience');
INSERT INTO `auth_permission` VALUES ('49', 'Can add user', '17', 'add_user');
INSERT INTO `auth_permission` VALUES ('50', 'Can change user', '17', 'change_user');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete user', '17', 'delete_user');
INSERT INTO `auth_permission` VALUES ('52', 'Can add work experience', '18', 'add_workexperience');
INSERT INTO `auth_permission` VALUES ('53', 'Can change work experience', '18', 'change_workexperience');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete work experience', '18', 'delete_workexperience');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$12000$Pj7kCsYuu8ib$wF9Y5uz0COK9Lh56tqXpnVlNaBcGViUeU7/rZevmSDM=', '2015-06-04 11:50:50', '1', 'macy', '', '', 'five3@163.com', '1', '1', '2015-06-04 11:50:50');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for category1
-- ----------------------------
DROP TABLE IF EXISTS `category1`;
CREATE TABLE `category1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `path` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of category1
-- ----------------------------

-- ----------------------------
-- Table structure for category2
-- ----------------------------
DROP TABLE IF EXISTS `category2`;
CREATE TABLE `category2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `parent_id` int(11) DEFAULT NULL,
  `path` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `parent_id` (`parent_id`),
  CONSTRAINT `category2_ibfk_1` FOREIGN KEY (`parent_id`) REFERENCES `category1` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of category2
-- ----------------------------

-- ----------------------------
-- Table structure for company
-- ----------------------------
DROP TABLE IF EXISTS `company`;
CREATE TABLE `company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `stage` varchar(255) DEFAULT NULL,
  `tag` varchar(255) DEFAULT NULL,
  `people_num` int(11) DEFAULT NULL,
  `home_url` varchar(255) DEFAULT NULL,
  `logo` varchar(255) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of company
-- ----------------------------
INSERT INTO `company` VALUES ('1', '百度', '北京', '上市', '互联网，大数据', '10000', 'http://www.baidu.com', 'baidu.gif', null, null, '16');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'log entry', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'permission', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('3', 'group', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('4', 'user', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'content type', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'session', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('7', 'category1', 'login', 'category1');
INSERT INTO `django_content_type` VALUES ('8', 'category2', 'login', 'category2');
INSERT INTO `django_content_type` VALUES ('9', 'company', 'login', 'company');
INSERT INTO `django_content_type` VALUES ('10', 'django migrations', 'login', 'djangomigrations');
INSERT INTO `django_content_type` VALUES ('11', 'job', 'login', 'job');
INSERT INTO `django_content_type` VALUES ('12', 'job apply', 'login', 'jobapply');
INSERT INTO `django_content_type` VALUES ('13', 'job feedback', 'login', 'jobfeedback');
INSERT INTO `django_content_type` VALUES ('14', 'resume', 'login', 'resume');
INSERT INTO `django_content_type` VALUES ('15', 'sender valid', 'login', 'sendervalid');
INSERT INTO `django_content_type` VALUES ('16', 'study experience', 'login', 'studyexperience');
INSERT INTO `django_content_type` VALUES ('17', 'user', 'login', 'user');
INSERT INTO `django_content_type` VALUES ('18', 'work experience', 'login', 'workexperience');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2015-06-04 11:50:26');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2015-06-04 11:50:27');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2015-06-04 11:50:28');
INSERT INTO `django_migrations` VALUES ('4', 'login', '0001_initial', '2015-06-04 11:50:28');
INSERT INTO `django_migrations` VALUES ('5', 'sessions', '0001_initial', '2015-06-04 11:50:28');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('rxmfjmra62k9w4lfa44vvo5zbw310jfc', 'OGEzYTFiZTUxZmY5Yzg1M2Y2YmY2MzQ5YzA4OTA5YzVhOTIxZDIzZDp7ImlzbG9naW4iOnRydWUsInVzZXJfaW5mbyI6eyJlbWFpbCI6IjEyMyIsImlkIjoxNiwibmFtZSI6IjEyMyJ9fQ==', '2015-06-19 14:42:15');

-- ----------------------------
-- Table structure for job
-- ----------------------------
DROP TABLE IF EXISTS `job`;
CREATE TABLE `job` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  `category_path` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `scale` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `experience` varchar(255) DEFAULT NULL,
  `educational` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `tag` varchar(255) DEFAULT NULL,
  `desc` text,
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `uid` (`uid`),
  KEY `cid` (`cid`),
  CONSTRAINT `job_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `job_ibfk_2` FOREIGN KEY (`cid`) REFERENCES `company` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of job
-- ----------------------------

-- ----------------------------
-- Table structure for job_apply
-- ----------------------------
DROP TABLE IF EXISTS `job_apply`;
CREATE TABLE `job_apply` (
  `id` int(11) NOT NULL,
  `uid` int(11) DEFAULT NULL,
  `job_id` int(11) DEFAULT NULL,
  `resume_id` int(11) DEFAULT NULL,
  `send_uid` int(11) DEFAULT NULL,
  `is_read` int(11) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `uid` (`uid`),
  KEY `job_id` (`job_id`),
  KEY `resume_id` (`resume_id`),
  KEY `send_uid` (`send_uid`),
  CONSTRAINT `job_apply_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `job_apply_ibfk_2` FOREIGN KEY (`job_id`) REFERENCES `job` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `job_apply_ibfk_3` FOREIGN KEY (`resume_id`) REFERENCES `resume` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `job_apply_ibfk_4` FOREIGN KEY (`send_uid`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of job_apply
-- ----------------------------

-- ----------------------------
-- Table structure for job_feedback
-- ----------------------------
DROP TABLE IF EXISTS `job_feedback`;
CREATE TABLE `job_feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `content` text,
  `job_id` int(11) DEFAULT NULL,
  `is_read` int(11) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `uid` (`uid`),
  KEY `job_id` (`job_id`),
  CONSTRAINT `job_feedback_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `job_feedback_ibfk_2` FOREIGN KEY (`job_id`) REFERENCES `job` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of job_feedback
-- ----------------------------

-- ----------------------------
-- Table structure for login_user
-- ----------------------------
DROP TABLE IF EXISTS `login_user`;
CREATE TABLE `login_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(18) DEFAULT NULL,
  `passwd` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of login_user
-- ----------------------------

-- ----------------------------
-- Table structure for resume
-- ----------------------------
DROP TABLE IF EXISTS `resume`;
CREATE TABLE `resume` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `tag` varchar(255) DEFAULT NULL,
  `education` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `mobilephone` int(11) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `self_evaluate` varchar(255) DEFAULT NULL,
  `hope_work` varchar(255) DEFAULT NULL,
  `hope_type` varchar(255) DEFAULT NULL,
  `hope_city` varchar(255) DEFAULT NULL,
  `hope_salary` int(11) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  `attach_file` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `uid` (`uid`),
  CONSTRAINT `resume_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of resume
-- ----------------------------
INSERT INTO `resume` VALUES ('2', '16', ' 陈晓伍', '6年工作经验', '精通python', '本科', '合肥', '2147483647', 'five3@163.com', '工作能力强，', '运维', '全职', '合肥', '90000', null, null, 'mysql.chm');
INSERT INTO `resume` VALUES ('3', '17', 'chenxiaowu', 'fine', 'show', '本科', '合肥', '1234567899', 'five3@163.com', '活好', 'python开发', '全职', '北京', '90000', null, null, null);

-- ----------------------------
-- Table structure for sender_valid
-- ----------------------------
DROP TABLE IF EXISTS `sender_valid`;
CREATE TABLE `sender_valid` (
  `id` int(11) NOT NULL,
  `phone` int(11) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `is_valid` int(11) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cid` (`cid`),
  KEY `uid` (`uid`),
  CONSTRAINT `sender_valid_ibfk_1` FOREIGN KEY (`cid`) REFERENCES `company` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `sender_valid_ibfk_2` FOREIGN KEY (`uid`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sender_valid
-- ----------------------------

-- ----------------------------
-- Table structure for study_experience
-- ----------------------------
DROP TABLE IF EXISTS `study_experience`;
CREATE TABLE `study_experience` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `resume_id` int(11) DEFAULT NULL,
  `school_name` varchar(255) DEFAULT NULL,
  `start_date` datetime DEFAULT NULL,
  `end_date` datetime DEFAULT NULL,
  `educational` varchar(255) DEFAULT NULL,
  `subject` varchar(255) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `resume_id` (`resume_id`),
  CONSTRAINT `study_experience_ibfk_1` FOREIGN KEY (`resume_id`) REFERENCES `resume` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of study_experience
-- ----------------------------
INSERT INTO `study_experience` VALUES ('1', '2', '北京航空航天大学', '2013-10-11 00:00:00', '2013-10-11 00:00:00', '本科', '计算机', null, null);
INSERT INTO `study_experience` VALUES ('2', '3', '北京航空航天大学', '2015-11-11 00:00:00', '2015-11-11 00:00:00', '本科', '计算机科学与技术', null, null);

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
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('16', '123', '123', '202cb962ac59075b964b07152d234b70', null, null, '0000-00-00 00:00:00', null, '1');
INSERT INTO `user` VALUES ('17', 'chenxiaowu', 'chenxiaowu@test.com', '96e79218965eb72c92a549dd5a330112', null, null, '0000-00-00 00:00:00', null, '1');
INSERT INTO `user` VALUES ('18', '111', '111', '698d51a19d8a121ce581499d7b701668', null, null, '2015-06-04 23:23:53', null, null);

-- ----------------------------
-- Table structure for work_experience
-- ----------------------------
DROP TABLE IF EXISTS `work_experience`;
CREATE TABLE `work_experience` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `resume_id` int(11) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `start_date` datetime DEFAULT NULL,
  `end_date` datetime DEFAULT NULL,
  `job` varchar(255) DEFAULT NULL,
  `description` text,
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `resume_id` (`resume_id`),
  CONSTRAINT `work_experience_ibfk_1` FOREIGN KEY (`resume_id`) REFERENCES `resume` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of work_experience
-- ----------------------------
INSERT INTO `work_experience` VALUES ('1', '2', '当当', '2012-10-11 00:00:00', '2012-10-11 00:00:00', '剩斗士', '22', null, null);
INSERT INTO `work_experience` VALUES ('2', '3', '百度', '2012-03-03 00:00:00', '2014-06-06 00:00:00', 'python', '后台开发', null, null);
INSERT INTO `work_experience` VALUES ('3', '3', '当当', '2999-02-02 00:00:00', '2015-11-11 00:00:00', 'python', '前端', null, null);

/*
Navicat MySQL Data Transfer

Source Server         : MySQL
Source Server Version : 50719
Source Host           : localhost:3306
Source Database       : python

Target Server Type    : MYSQL
Target Server Version : 50719
File Encoding         : 65001

Date: 2019-05-09 08:36:29
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for brande
-- ----------------------------
DROP TABLE IF EXISTS `brande`;
CREATE TABLE `brande` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of brande
-- ----------------------------
INSERT INTO `brande` VALUES ('1', '李宁');
INSERT INTO `brande` VALUES ('2', '耐克');
INSERT INTO `brande` VALUES ('3', '华为');
INSERT INTO `brande` VALUES ('4', '小米');
INSERT INTO `brande` VALUES ('5', 'OPPO');
INSERT INTO `brande` VALUES ('6', 'vivo');
INSERT INTO `brande` VALUES ('7', '魅族');
INSERT INTO `brande` VALUES ('8', '苹果');
INSERT INTO `brande` VALUES ('9', '格力');
INSERT INTO `brande` VALUES ('10', '海尔');
INSERT INTO `brande` VALUES ('11', '富士通');
INSERT INTO `brande` VALUES ('12', '飞利浦');
INSERT INTO `brande` VALUES ('13', '锐步');
INSERT INTO `brande` VALUES ('14', '361°');
INSERT INTO `brande` VALUES ('15', '阿迪达斯');
INSERT INTO `brande` VALUES ('16', '亚瑟士');
INSERT INTO `brande` VALUES ('17', '卡郎琪');
INSERT INTO `brande` VALUES ('18', '爱马仕');
INSERT INTO `brande` VALUES ('19', '路易威登');
INSERT INTO `brande` VALUES ('20', '香奈儿');
INSERT INTO `brande` VALUES ('21', '雅诗兰黛');
INSERT INTO `brande` VALUES ('22', '巴黎欧莱雅');
INSERT INTO `brande` VALUES ('23', '兰蔻');
INSERT INTO `brande` VALUES ('24', '帮宝适');
INSERT INTO `brande` VALUES ('25', '贝恩施');
INSERT INTO `brande` VALUES ('26', '富光');
INSERT INTO `brande` VALUES ('27', '洁柔');
INSERT INTO `brande` VALUES ('28', '洽洽');
INSERT INTO `brande` VALUES ('29', '百草味');
INSERT INTO `brande` VALUES ('30', '三全');
INSERT INTO `brande` VALUES ('31', '江诗丹顿');
INSERT INTO `brande` VALUES ('32', '劳力士');
INSERT INTO `brande` VALUES ('33', '朗格');
INSERT INTO `brande` VALUES ('34', '时代出版');
INSERT INTO `brande` VALUES ('35', '中文传媒');
INSERT INTO `brande` VALUES ('36', '乐高');
INSERT INTO `brande` VALUES ('37', '得力');
INSERT INTO `brande` VALUES ('38', '汉乐府');
INSERT INTO `brande` VALUES ('39', '宝马');
INSERT INTO `brande` VALUES ('40', '新丝路');
INSERT INTO `brande` VALUES ('41', '腾讯');
INSERT INTO `brande` VALUES ('42', '老马蔬菜店');

-- ----------------------------
-- Table structure for cate
-- ----------------------------
DROP TABLE IF EXISTS `cate`;
CREATE TABLE `cate` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cate
-- ----------------------------
INSERT INTO `cate` VALUES ('1', '游戏充值');
INSERT INTO `cate` VALUES ('2', 'cpd');
INSERT INTO `cate` VALUES ('3', '李宁');
INSERT INTO `cate` VALUES ('4', '一小时达');
INSERT INTO `cate` VALUES ('5', '老马蔬菜店');
INSERT INTO `cate` VALUES ('6', '京东商城');
INSERT INTO `cate` VALUES ('7', '天猫超市');
INSERT INTO `cate` VALUES ('8', '当当');
INSERT INTO `cate` VALUES ('9', '电脑数码');
INSERT INTO `cate` VALUES ('10', '家用电器');
INSERT INTO `cate` VALUES ('11', '运动户外');
INSERT INTO `cate` VALUES ('12', '服饰鞋包');
INSERT INTO `cate` VALUES ('13', '个护化妆');
INSERT INTO `cate` VALUES ('14', '母婴用品');
INSERT INTO `cate` VALUES ('15', '日用百货');
INSERT INTO `cate` VALUES ('16', '食品生鲜');
INSERT INTO `cate` VALUES ('17', '礼品钟表');
INSERT INTO `cate` VALUES ('18', '图书音像');
INSERT INTO `cate` VALUES ('19', '玩模乐器');
INSERT INTO `cate` VALUES ('20', '办公设备');
INSERT INTO `cate` VALUES ('21', '家居家装');
INSERT INTO `cate` VALUES ('22', '汽车消费');
INSERT INTO `cate` VALUES ('23', '文化娱乐');
INSERT INTO `cate` VALUES ('24', '房产置业');
INSERT INTO `cate` VALUES ('25', '旅游出行');

-- ----------------------------
-- Table structure for classes
-- ----------------------------
DROP TABLE IF EXISTS `classes`;
CREATE TABLE `classes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of classes
-- ----------------------------
INSERT INTO `classes` VALUES ('1', '计算机科学与技术');
INSERT INTO `classes` VALUES ('2', '电子商务');
INSERT INTO `classes` VALUES ('5', '心理学');

-- ----------------------------
-- Table structure for goods
-- ----------------------------
DROP TABLE IF EXISTS `goods`;
CREATE TABLE `goods` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `price` decimal(8,2) DEFAULT NULL,
  `is_delete` int(11) DEFAULT '0',
  `is_show` int(11) DEFAULT '1',
  `is_selt` int(11) DEFAULT '0',
  `cate_id` int(10) unsigned DEFAULT NULL,
  `brande_id` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cate_id` (`cate_id`),
  KEY `brande_id` (`brande_id`),
  CONSTRAINT `goods_ibfk_1` FOREIGN KEY (`cate_id`) REFERENCES `cate` (`id`),
  CONSTRAINT `goods_ibfk_2` FOREIGN KEY (`brande_id`) REFERENCES `brande` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods
-- ----------------------------
INSERT INTO `goods` VALUES ('1', 'oppo reno', '5555.00', '0', '1', '1', '9', '5');
INSERT INTO `goods` VALUES ('2', 'oppo r17', '3555.00', '0', '1', '1', '9', '5');
INSERT INTO `goods` VALUES ('3', '宝马', '990000.00', '0', '1', '1', '22', '39');
INSERT INTO `goods` VALUES ('4', 'honor v20', '3999.00', '0', '1', '1', '9', '3');
INSERT INTO `goods` VALUES ('5', 'HUAWEI Mate20', '6999.00', '0', '1', '1', '9', '3');
INSERT INTO `goods` VALUES ('6', 'Q币100', '99.00', '0', '1', '0', '1', '41');
INSERT INTO `goods` VALUES ('7', 'Q币10', '9.90', '0', '1', '1', '1', '41');
INSERT INTO `goods` VALUES ('8', '点劵168', '16.80', '0', '1', '1', '1', '41');
INSERT INTO `goods` VALUES ('9', '点劵888', '88.80', '0', '1', '1', '1', '41');
INSERT INTO `goods` VALUES ('10', '积分100', '90.00', '0', '1', '0', '1', '41');
INSERT INTO `goods` VALUES ('11', '积分88', '78.00', '0', '1', '1', '1', '41');
INSERT INTO `goods` VALUES ('12', '5G手机', '8988.00', '0', '1', '1', '9', '3');
INSERT INTO `goods` VALUES ('13', '5G手机', '15988.00', '0', '1', '0', '9', '4');
INSERT INTO `goods` VALUES ('14', '5G手机', '6999.00', '0', '1', '0', '9', '5');
INSERT INTO `goods` VALUES ('15', '5G手机', '5988.00', '0', '1', '1', '9', '6');

-- ----------------------------
-- Table structure for inventory
-- ----------------------------
DROP TABLE IF EXISTS `inventory`;
CREATE TABLE `inventory` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `goods_id` int(10) unsigned NOT NULL,
  `stock_number` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_id` (`goods_id`),
  CONSTRAINT `inventory_ibfk_1` FOREIGN KEY (`goods_id`) REFERENCES `goods` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of inventory
-- ----------------------------
INSERT INTO `inventory` VALUES ('1', '1', '100');
INSERT INTO `inventory` VALUES ('2', '2', '100');
INSERT INTO `inventory` VALUES ('3', '3', '100');
INSERT INTO `inventory` VALUES ('4', '4', '100');
INSERT INTO `inventory` VALUES ('5', '5', '100');
INSERT INTO `inventory` VALUES ('6', '6', '100');
INSERT INTO `inventory` VALUES ('7', '7', '100');
INSERT INTO `inventory` VALUES ('8', '8', '100');
INSERT INTO `inventory` VALUES ('9', '9', '100');
INSERT INTO `inventory` VALUES ('10', '10', '100');
INSERT INTO `inventory` VALUES ('11', '11', '100');
INSERT INTO `inventory` VALUES ('12', '12', '100');
INSERT INTO `inventory` VALUES ('13', '13', '100');
INSERT INTO `inventory` VALUES ('14', '14', '100');
INSERT INTO `inventory` VALUES ('15', '15', '100');

-- ----------------------------
-- Table structure for order_m
-- ----------------------------
DROP TABLE IF EXISTS `order_m`;
CREATE TABLE `order_m` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_name` varchar(20) DEFAULT NULL,
  `goods_id` int(10) unsigned NOT NULL,
  `cost` decimal(8,2) NOT NULL,
  `serial_number` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_m
-- ----------------------------
INSERT INTO `order_m` VALUES ('1', 'xx', '1', '5500.00', '10010');
INSERT INTO `order_m` VALUES ('2', 'xx', '3', '990000.00', '10011');
INSERT INTO `order_m` VALUES ('3', 'xx', '7', '9.90', '10012');
INSERT INTO `order_m` VALUES ('4', 'xx', '2', '3555.00', '10013');
INSERT INTO `order_m` VALUES ('5', 'xx', '11', '78.00', '10014');
INSERT INTO `order_m` VALUES ('6', 'xx', '4', '3999.00', '10015');
INSERT INTO `order_m` VALUES ('7', 'xx', '15', '5988.00', '10016');
INSERT INTO `order_m` VALUES ('8', 'qwe', '5', '6999.00', '10017');
INSERT INTO `order_m` VALUES ('9', 'qwe', '8', '16.80', '10018');
INSERT INTO `order_m` VALUES ('10', 'aaas', '9', '88.80', '10019');
INSERT INTO `order_m` VALUES ('11', 'qwe', '12', '8988.00', '10020');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) DEFAULT '',
  `age` int(11) DEFAULT '0',
  `height` decimal(5,2) DEFAULT NULL,
  `gender` enum('男','女') DEFAULT NULL,
  `cls_id` int(11) DEFAULT '0',
  `is_delete` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('1', '小刚', '15', '157.33', '男', '1', '0');
INSERT INTO `student` VALUES ('2', '小红', '16', '167.45', '女', '1', '0');
INSERT INTO `student` VALUES ('3', '小朱', '20', '157.00', '女', '1', '0');
INSERT INTO `student` VALUES ('4', '小静', '15', '157.45', '女', '1', '0');
INSERT INTO `student` VALUES ('5', '小彩', '15', '157.45', '女', '1', '0');
INSERT INTO `student` VALUES ('6', '大明', '20', '198.45', '男', '1', '0');
INSERT INTO `student` VALUES ('7', '李逵', '35', '180.98', '男', '1', '0');
INSERT INTO `student` VALUES ('8', '小韩', '12', '165.22', '女', '2', '0');
INSERT INTO `student` VALUES ('9', '小高', '12', '165.22', '女', '2', '0');
INSERT INTO `student` VALUES ('10', '大韩', '12', '165.22', '男', '3', '0');
INSERT INTO `student` VALUES ('11', '跳跳', '12', '165.22', '男', '4', '0');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `password` varchar(8) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'xx', 'xx');
INSERT INTO `user` VALUES ('2', 'qwe', 'qwe');
INSERT INTO `user` VALUES ('3', '111', '111');
INSERT INTO `user` VALUES ('4', 'aaas', 'aaa');

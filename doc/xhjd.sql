USE bike;

CREATE TABLE IF NOT EXISTS `wypcs110Content` (
  `id` int(50) NOT NULL auto_increment,
  `openid` varchar(255) DEFAULT '',
  `nickname` varchar(255) DEFAULT '',
  `sex` int(2) DEFAULT 0,
  `city` varchar(255) DEFAULT '',
  `country` varchar(255) DEFAULT '',
  `province` varchar(255) DEFAULT '',
  `msgType` varchar(255) DEFAULT '',
  `event` varchar(255) DEFAULT '',
  `text` varchar(255) DEFAULT '',
  `latitude` varchar(255) DEFAULT '',
  `longitude` varchar(255) DEFAULT '',
  `label` varchar(255) DEFAULT '',
  `createTime` varchar(255) DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `openid` (`openid`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
USE bike;

CREATE TABLE `station` (
  `id` bigint(11) unsigned NOT NULL AUTO_INCREMENT,
  `cid` int(11) NOT NULL DEFAULT '0' COMMENT 'city.cid',
  `sid` int(11) NOT NULL DEFAULT '0' COMMENT 'data_source.id',
  `code` varchar(128) NOT NULL DEFAULT '' COMMENT '租赁点编号',
  `status` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '是否有效，0：否 1：是',
  `type` varchar(20) NOT NULL DEFAULT '' COMMENT '租赁点类型',
  `total` int(11) NOT NULL DEFAULT '0' COMMENT '总车位数',
  `name` varchar(128) NOT NULL DEFAULT '' COMMENT '租赁点名称',
  `address` varchar(256) NOT NULL DEFAULT '' COMMENT '租赁点地址',
  `rid` varchar(20) NOT NULL DEFAULT '' COMMENT '租赁点城区id, region.rid',
  `longitude` varchar(30) NOT NULL DEFAULT '' COMMENT '租赁点经度（百度系）',
  `latitude` varchar(30) NOT NULL DEFAULT '' COMMENT '租赁点纬度（百度系）',
  `telephone` varchar(11) NOT NULL DEFAULT '' COMMENT '联系电话',
  `service_time` varchar(256) NOT NULL DEFAULT '' COMMENT '服务时间',
  `is_24` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '是否24小时 0：否 1：是',
  `is_duty` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '是否有人值守 0：否 1：是',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `IDX_CODE_CITYID_SID` (`code`, `cid`, `sid`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='自行车租赁点';

CREATE TABLE `user` (
  `id` bigint(1) unsigned NOT NULL AUTO_INCREMENT COMMENT '主key',
  `city_id` int(11) NOT NULL DEFAULT '0' COMMENT '用户选择的城市服务city.id',
  `is_subscribe` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '是否关注 0：否 1：是',
  `openid` varchar(28) NOT NULL COMMENT '用户openid',
  `nickname` varchar(100) CHARACTER SET utf8mb4 NOT NULL DEFAULT '' COMMENT '用户昵称',
  `sex` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '用户性别 0：未知 1：男性 2：女性',
  `city` varchar(32) DEFAULT '' COMMENT '用户所在城市',
  `country` varchar(32) DEFAULT '' COMMENT '用户所在国家',
  `province` varchar(32) DEFAULT '' COMMENT '用户所在省份',
  `language` varchar(32) NOT NULL DEFAULT '' COMMENT '用户语言',
  `headimg` varchar(512) DEFAULT '' COMMENT '用户头像',
  `subscribe_time` datetime DEFAULT NULL COMMENT '用户关注时间',
  `unsubscibe_time` datetime DEFAULT NULL COMMENT '用户取消关注时间',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `IDX_OPENID` (`openid`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='用户表';


CREATE TABLE `scrap_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) NOT NULL DEFAULT '0' COMMENT 'city.cid',
  `status` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '是否成功，0：否 1：是',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='抓取脚本log';

CREATE TABLE `data_source` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(512) DEFAULT '' COMMENT '来源名称, 对应 header中的键名',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='数据来源';


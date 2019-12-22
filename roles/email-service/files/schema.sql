

CREATE TABLE  IF NOT EXISTS `domain` (
  `domain` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `mailboxes` int(10) NOT NULL DEFAULT '0',
  `backupmx` tinyint(1) NOT NULL DEFAULT '0',
  `quota` bigint(20) NOT NULL DEFAULT '0',
  `active` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`domain`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 ;


CREATE TABLE  IF NOT EXISTS  `alias` (
  `address` varchar(255) NOT NULL,
  `goto` text NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`address`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 ;


CREATE TABLE  IF NOT EXISTS `mailbox` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 NOT NULL,
  `local_part` varchar(255) NOT NULL,
  `domain` varchar(255) NOT NULL,
  `quota` bigint(20) NOT NULL DEFAULT '0',
  `active` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# CREATE TABLE  IF NOT EXISTS `userquota` (
#   `address` varchar(255) NOT NULL,
#   `quota` bigint(20) NOT NULL DEFAULT '0',
#   `mails` bigint(20) NOT NULL DEFAULT '0',
#   PRIMARY KEY (`address`)
# ) ENGINE=MyISAM DEFAULT CHARSET=utf8;
#
# CREATE TABLE  IF NOT EXISTS `domainquota` (
#   `domain` varchar(255) NOT NULL,
#   `quota` bigint(20) NOT NULL DEFAULT '0',
#   `mails` bigint(20) NOT NULL DEFAULT '0',
#   PRIMARY KEY (`domain`)
# ) ENGINE=MyISAM DEFAULT CHARSET=utf8;

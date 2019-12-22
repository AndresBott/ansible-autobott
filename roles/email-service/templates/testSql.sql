INSERT INTO `domain`(
  domain,
  created,
  modified
) VALUES (
  'andresbott.com',
  '2017-03-25 14:37:03',
  '2017-03-25 14:37:03'
  ,'0') ON DUPLICATE KEY UPDATE
  modified='2017-03-25 14:37:03'
  ,active='0' ;










create database Diagnosed;
create table give(customerid varchar(255),gender varchar(255),seniorcitizen varchar(255));
select * from give;
#insert into go(customerid,gender,seniorcitizen) values ('7590-VHVEG','female',0),('5575-GNVDE','male',0),('3668-QPYBK','male',0),('7795-CFOCW','male',0),('9237-HQITU','female',0),('9305-CDSKC','female',0),('1452-KIOVK','male',0),('6713-OKOMC','female',0),('7892-POOKP','female',0),('6388-TABGU','male',0),('9763-GRSKD','male',0),('7469-LKBCI','male',0),('8091-TTVAX','male',0),('0280-XJGEX','male',0);
select * from give;


insert into give(customerid,gender,seniorcitizen) values ('7590 VHVEG','female',0),('5575 GNVDE','male',0),('3668 QPYBK','male',0),('7795 CFOCW','male',0),('9237 HQITU','female',0),('9305 CDSKC','female',0),('1452 KIOVK','male',0),('6713 OKOMC','female',0),('7892 POOKP','female',0),('6388 TABGU','male',0),('9763 GRSKD','male',0),('7469 LKBCI','male',0),('8091 TTVAX','male',0),('0280 XJGEX','male',0);
select * from give;
select count(gender) from go where gender = 'male';
update give set seniorcitizen = '1' where customerid = '1452 KIOVK' limit 1;
select * from give;
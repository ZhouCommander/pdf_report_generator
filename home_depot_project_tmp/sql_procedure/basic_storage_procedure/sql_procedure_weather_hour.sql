
DROP PROCEDURE if EXISTS report_weather_hour;
CREATE PROCEDURE  report_weather_hour (in in_property_id int, in start_time DATETIME,in end_time DATETIME)


BEGIN

-- return  creatd_time,wather,temperature
  
SELECT distinct RIGHT(LEFT(created_time,13),2) as dateNeed ,
weather_text ,
(weather_temp * 1.8 + 32) as Temp 
FROM weather_per_hour 
WHERE city_name = (SELECT property.city_name FROM property WHERE property.id=in_property_id) 
and created_time  BETWEEN start_time AND end_time
GROUP BY created_time 
ORDER BY created_time;
  
END;

CALL report_weather_hour(121,'2017-11-25 06:00:00','2017-11-26 05:59:00')
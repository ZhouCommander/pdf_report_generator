
DROP PROCEDURE if EXISTS report_weather_day;
CREATE PROCEDURE  report_weather_day (in in_property_id int, in start_time DATETIME,in end_time DATETIME)


BEGIN

-- return  creatd_time,wather,temperature
  
SELECT distinct LEFT(created_time,11) as dateNeed ,
weather_text ,
(weather_temp * 1.8 + 32) as Temp 
FROM weather
WHERE city_name = (SELECT property.city_name FROM property WHERE property.id=in_property_id) 
and created_time  BETWEEN start_time AND end_time
GROUP BY created_time 
ORDER BY created_time;
  
END;

CALL report_weather_day(121,'2018-11-12 06:00:00','2018-11-13 05:59:00')
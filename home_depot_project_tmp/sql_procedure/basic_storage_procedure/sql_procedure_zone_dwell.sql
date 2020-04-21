

DROP PROCEDURE if EXISTS report_zone_dwell;
CREATE PROCEDURE  report_zone_dwell(in in_model_id int, in start_time DATETIME,in end_time DATETIME )
BEGIN


SELECT name,RIGHT(LEFT(a.update_time,13),2) as hour,a.dwell_time
FROM 
zone
LEFT JOIN 
(SELECT update_time ,
sum(dwell_time) as dwell_time ,
dwell_time.model_id
FROM dwell_time 
WHERE type_id = 60  AND 
dwell_time.model_id = in_model_id AND 
update_time BETWEEN start_time AND end_time 
GROUP BY  RIGHT(LEFT(update_time,13),2))AS a 
ON a.model_id =zone.id
WHERE zone.id = in_model_id 
order BY update_time;
END;

CALL report_zone_dwell(1,'2018-11-03 08:00:00','2018-11-03 20:00:00')



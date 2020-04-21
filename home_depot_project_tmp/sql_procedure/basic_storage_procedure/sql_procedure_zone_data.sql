

DROP PROCEDURE if EXISTS report_zone_data;
CREATE PROCEDURE  report_zone_data(in in_typed_id int,in in_model_id int, in start_time DATETIME,in end_time DATETIME )
BEGIN

-- return avgEnter.TotalEnter.PeakEntrance.PeakEnetrTime.PeakOccupancy.PeakOccupancyTime
SELECT name,RIGHT(LEFT(a.created_time,13),2) as hour,a.entry,a.exits,a.peak_occupancy
FROM 
zone
LEFT JOIN 
(SELECT created_time ,
sum(enter) as entry ,
SUM(hourly_index.exitnum)as exits, 
MAX(hourly_index.tmp_occupancy)as peak_occupancy,
hourly_index.model_id
FROM hourly_index 
WHERE type_id = in_typed_id  AND 
hourly_index.model_id = in_model_id AND 
created_time BETWEEN start_time AND end_time 
GROUP BY  RIGHT(LEFT(created_time,13),2))AS a 
ON a.model_id =zone.id
WHERE zone.id = in_model_id 
order BY created_time;
END;

CALL report_zone_data(60,739,'2018-10-29 08:00:00','2018-10-29 20:00:00')

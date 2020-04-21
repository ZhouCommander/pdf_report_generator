

DROP PROCEDURE if EXISTS report_entry_data;
CREATE PROCEDURE  report_entry_data(in typed_id int,in in_model_id VARCHAR(20), in start_time DATETIME,in end_time DATETIME )
BEGIN

-- return hour.entry.exits.peak_occupancy.

        SELECT RIGHT(LEFT(created_time,13),2) as hour ,
        sum(enter) as entry ,
        SUM(hourly_index.exitnum)as exits, 
        MAX(hourly_index.tmp_occupancy)as peak_occupancy
        FROM hourly_index 
        WHERE type_id = typed_id  AND 
        find_in_set(hourly_index.model_id, in_model_id) AND 
        created_time BETWEEN start_time AND end_time 
        GROUP BY  RIGHT(LEFT(created_time,13),2)
        ORDER BY created_time;
END;

CALL report_entry_data(62,'121','2018-10-29 08:00:00','2018-10-29 08:59:00')
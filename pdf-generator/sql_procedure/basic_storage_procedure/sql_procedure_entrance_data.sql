DROP PROCEDURE if EXISTS report_entrance_data;
CREATE PROCEDURE  report_entrance_data(in in_type_id int,in in_model_id   INT, in in_type VARCHAR(64),in entrance_name varchar(128), in start_time DATETIME,in end_time DATETIME )


BEGIN

-- return total enter.gatename


    select RIGHT(LEFT(created_time,13),2) as hour ,
    sum(enter) as entry ,
    SUM(hourly_index.exitnum)as exits, 
    MAX(hourly_index.tmp_occupancy)as peak_occupancy 
    FROM 
    hourly_index
    where 
    hourly_index.type_id = 58 
    and model_id in 
    (SELECT dashgate_line.line_id FROM dashgate_line WHERE dashgate_line.gate_id in 
    (SELECT dash_gate.id FROM dash_gate WHERE dash_gate.gatename =entrance_name 
    AND dash_gate.type_id = in_type_id 
    AND dash_gate.model_id = in_model_id 
    AND dash_gate.type = in_type)) 
    and created_time BETWEEN start_time AND end_time 
    GROUP BY  RIGHT(LEFT(created_time,13),2) 
    ORDER BY created_time;


  
END;

CALL report_entrance_data(90,121,'people',"Capital Dim Sum",'2018-01-18 11:00:00','2018-01-18 11:59:00')
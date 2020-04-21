
DROP PROCEDURE if EXISTS report_zone_entrance;
CREATE PROCEDURE  report_zone_entrance(in in_type_id int,in in_model_id   INT, in in_type VARCHAR(64) )


BEGIN

-- return  gatename
  
SELECT 
dash_gate.gatename,
dash_gate.id
FROM dash_gate 
WHERE dash_gate.type_id = in_type_id 
AND dash_gate.model_id = in_model_id 
AND dash_gate.type = in_type;
  
END;

CALL report_zone_entrance(90,121,'people')
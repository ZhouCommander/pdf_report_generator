DROP PROCEDURE if EXISTS report_zone_id;
CREATE PROCEDURE  report_zone_id(in in_type_id int)


BEGIN

-- return zone id

   SELECT zone.id, zone.name
   FROM zone
   WHERE
   zone.type_id = in_type_id;

END;

call report_zone_id(17)
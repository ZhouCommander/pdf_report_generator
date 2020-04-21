

DROP PROCEDURE if EXISTS report_heatmap;
CREATE PROCEDURE  report_heatmap(in in_property_id int,in in_time_range int, in start_time DATETIME,in end_time DATETIME )
BEGIN


        select 
        heatmap_horizontal,heatmap_vertical 
        from 
        topview 
        where 
        property_id = in_property_id
        and 
        time_range = in_time_range 
        and 
        created_time 
        BETWEEN 
        start_time and end_time;
END;

CALL report_heatmap(1,195,'2018-10-23','2018-10-24')


DROP PROCEDURE if EXISTS report_insert;
CREATE PROCEDURE  report_insert(in in_company_id int,
                                in in_property_id int,
                                in in_date varchar(100),
                                in in_report_url varchar(1024),
                                in in_type_id int,
                                in in_report_type int,
                                in in_space_type int )
    BEGIN
    
    DECLARE t_error INTEGER DEFAULT 0;
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET t_error=1;
    START TRANSACTION;
        insert into report
        (company_id,property_id,date,report_url,type_id,report_type,space_type)
            VALUES
            ( in_company_id,
            in_property_id,
            in_date,
            in_report_url,
            in_type_id,
            in_report_type,
            in_space_type);

    IF t_error = 1 THEN
        SELECT '0';
        ROLLBACK;
    ELSE
        COMMIT;
        SELECT '1';
    END IF;

    END;




CALL report_insert(1,1,'2018-10-27',"https://",20,192,24);

DROP PROCEDURE if EXISTS report_insert_hourly_traffic;
CREATE PROCEDURE report_insert_hourly_traffic(in in_create_time datetime,
                                              in in_zone_id     int,
                                              in in_enter_num   int, in in_exit_num int, in in_occupancy_num int)
  BEGIN
    DECLARE flag integer default -1;
    declare t_id integer;
    DECLARE t_error INTEGER DEFAULT 0;
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET t_error = 1;


    START TRANSACTION;
    select id
    into t_id
    from hourly_traffic_records_without_employee
    where create_time = in_create_time and zone_id = in_zone_id;

    if t_id is not null
    then
      set flag = 1;
      update hourly_traffic_records_without_employee
      set enter = in_enter_num, exitnum = in_exit_num, max_occupancy = in_occupancy_num
      where create_time = in_create_time and zone_id = in_zone_id;
    else
      insert ignore into hourly_traffic_records_without_employee
    (create_time, zone_id, enter, exitnum, max_occupancy)
    VALUES
      (in_create_time,
       in_zone_id,
       in_enter_num,
       in_exit_num,
       in_occupancy_num);
    end if;

    IF t_error = 1
    THEN
      SELECT '0';
      ROLLBACK;
    ELSE
      COMMIT;
      if flag = -1
        then
        SELECT '1';
      ELSE
        SELECT '2';
      end if;
    END IF;



  END;


CALL report_insert_hourly_traffic('2019-05-23 08:00:00', 1, 233, 0, 0);

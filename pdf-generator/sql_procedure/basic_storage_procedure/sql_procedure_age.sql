

DROP PROCEDURE if EXISTS report_age;
CREATE PROCEDURE  report_age(in start_time DATETIME,in end_time DATETIME  )

BEGIN


DECLARE gender_sum INT;

DECLARE gender_male INT;
DECLARE gender_male_percent FLOAT;
DECLARE male_sum_age INT;
DECLARE male_less_thirty INT;
DECLARE male_thirty_to_fifty_five INT;
DECLARE male_forty_to_sixty INT;
DECLARE male_more_sixty INT;
DECLARE male_less_thirty_percent FLOAT;
DECLARE male_thirty_to_fifty_five_percent FLOAT;
DECLARE male_forty_to_sixty_percent FLOAT;
DECLARE male_more_sixty_percent FLOAT;

DECLARE gender_female INT;
DECLARE gender_female_percent FLOAT;
DECLARE female_sum_age INT;
DECLARE female_less_thirty INT;
DECLARE female_thirty_to_fifty_five INT;
DECLARE female_forty_to_sixty INT;
DECLARE female_more_sixty INT;
DECLARE female_less_thirty_percent FLOAT;
DECLARE female_thirty_to_fifty_five_percent FLOAT;
DECLARE female_forty_to_sixty_percent FLOAT;
DECLARE female_more_sixty_percent FLOAT;

        SELECT 
        A+B+C+D,A,B,C,D INTO male_sum_age,male_less_thirty,male_thirty_to_fifty_five,male_forty_to_sixty,male_more_sixty
        from 
        (SELECT sum(agender.male_less_20)+SUM(agender.male_20_25)+sum(agender.male_25_30) as A ,
        sum(agender.male_30_35)+SUM(agender.male_35_40)+SUM(agender.male_40_45) as B ,
        SUM(agender.male_45_50)+SUM(agender.male_50_55)+SUM(agender.male_55_60) as C ,
        SUM(agender.male_more_60)as D 
        FROM agender WHERE agender.timestamp 
        BETWEEN start_time AND end_time)table_male;
        

        SELECT A+B+C+D,A,B,C,D INTO female_sum_age,female_less_thirty,female_thirty_to_fifty_five,female_forty_to_sixty,female_more_sixty
        from 
        (SELECT sum(agender.less_20)+SUM(agender.20_25)+sum(agender.25_30) as A ,
        sum(agender.30_35)+SUM(agender.35_40)+SUM(agender.40_45) as B ,
        SUM(agender.45_50)+SUM(agender.50_55)+SUM(agender.55_60) as C ,
        SUM(agender.more_60)as D 
        FROM agender WHERE agender.timestamp 
        BETWEEN start_time AND end_time)table_female;

        SELECT 
        SUM(unique_male)+SUM(unique_female), SUM(unique_male),SUM(unique_female)  INTO gender_sum,gender_male,gender_female
        FROM 
        agender_unique_repeat 
        WHERE agender_unique_repeat.timestamp BETWEEN  start_time AND end_time;

        SET gender_male_percent = gender_male/gender_sum;
        SET male_less_thirty_percent = male_less_thirty/male_sum_age;
        SET male_thirty_to_fifty_five_percent = male_thirty_to_fifty_five/male_sum_age;
        SET male_forty_to_sixty_percent = male_forty_to_sixty/male_sum_age;
        SET male_more_sixty_percent = male_more_sixty/male_sum_age;
        SET gender_female_percent = gender_female/gender_sum;
        SET female_less_thirty_percent = female_less_thirty/female_sum_age;
        SET female_thirty_to_fifty_five_percent = female_thirty_to_fifty_five/female_sum_age;
        SET female_forty_to_sixty_percent = female_forty_to_sixty/female_sum_age;
        SET female_more_sixty_percent = female_more_sixty/female_sum_age;

        select gender_male_percent,
                male_less_thirty_percent,
                male_thirty_to_fifty_five_percent,
                male_forty_to_sixty_percent,
                male_more_sixty_percent,
                gender_female_percent,
                female_less_thirty_percent,
                female_thirty_to_fifty_five_percent,
                female_forty_to_sixty_percent,
                female_more_sixty_percent;

END;

CALL report_age('2018-10-23','2018-10-24')

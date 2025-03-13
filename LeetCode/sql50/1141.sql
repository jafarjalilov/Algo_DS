-- # Write your MySQL query statement below
SELECT 
activity_date AS day, 
COUNT(DISTINCT(user_id)) AS active_users 
FROM Activity 
WHERE activity_date BETWEEN DATE_ADD('2019-07-28', INTERVAL -30 DAY) AND '2019-07-27'
GROUP BY activity_date;

-- SQLITE
SELECT 
activity_date AS day, 
COUNT(DISTINCT(user_id)) AS active_users 
FROM Activity 
WHERE activity_date BETWEEN  date('2019-07-27', '-30 days') AND '2019-07-27'  
GROUP BY activity_date;
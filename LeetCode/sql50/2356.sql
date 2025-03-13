-- https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/description/?envType=study-plan-v2&envId=top-sql-50

-- # Write your MySQL query statement below
SELECT teacher_id, COUNT(DISTINCT(subject_id)) AS cnt
FROM Teacher
GROUP BY teacher_id;
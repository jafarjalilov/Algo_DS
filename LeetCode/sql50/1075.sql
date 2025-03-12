-- https://leetcode.com/problems/project-employees-i/description/?envType=study-plan-v2&envId=top-sql-50

SELECT project_id, ROUND(AVG(Employee.experience_years),2) AS average_years 
FROM Project
JOIN Employee ON Project.employee_id = Employee.employee_id
GROUP BY project_id
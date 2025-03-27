-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

SELECT
    name
FROM Employee
JOIN(
    SELECT
        managerId,
        COUNT(managerId) AS c
    FROM Employee
    GROUP BY managerId
    HAVING c >= 5 AND managerId IS NOT NULL
) X ON X.managerId = Employee.id
-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/

SELECT 
customer_id,
COUNT(CASE WHEN Transactions.transaction_id IS NULL THEN 1 ELSE NULL END) AS count_no_trans
FROM Visits
LEFT JOIN Transactions ON Transactions.visit_id = Visits.visit_id
GROUP BY customer_id
HAVING count_no_trans > 0
-- https://leetcode.com/problems/average-selling-price/description/?envType=study-plan-v2&envId=top-sql-50
SELECT Prices.product_id, COALESCE(ROUND(SUM(units*price)/SUM(units), 2), 0) AS average_price 
FROM Prices
LEFT JOIN UnitsSold ON Prices.product_id = UnitsSold.product_id 
AND (UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date)
GROUP BY Prices.product_id
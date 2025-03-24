-- https://leetcode.com/problems/product-sales-analysis-i/description/?envType=study-plan-v2&envId=top-sql-50

-- # Write your MySQL query statement below
SELECT 
    Product.product_name,
    Sales.year,
    Sales.price
FROM Product
JOIN Sales ON Sales.product_id=Product.product_id 
-- https://leetcode.com/problems/article-views-i/description/?envType=study-plan-v2&envId=top-sql-50

SELECT author_id AS id FROM(
    SELECT author_id, COUNT(viewer_id) FROM Views
    WHERE author_id=viewer_id
    GROUP BY author_id 
)ORDER BY id ASC
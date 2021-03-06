-- Using both the customers and orders table, write a query to give 
-- this output. If you add order by first_order_at limit 5, 
-- you should get the above output. 

WITH orders AS (
    SELECT customer_id
    , MIN(created_at) first_order_at
    , COUNT(DISTINCT id) number_of_orders
    FROM analytics-engineers-club.coffee_shop.orders
    GROUP BY 1
)

SELECT o.customer_id
, c.name
, c.email
, o.first_order_at
, o.number_of_orders
FROM analytics-engineers-club.coffee_shop.customers c
LEFT JOIN orders o ON o.customer_id=c.id
ORDER BY first_order_at asc
LIMIT 5

-- Using both the customers and orders table, write a query to give 
-- this output. If you add order by first_order_at limit 5, 
-- you should get the above output. 

SELECT o.customer_id
, c.name
, c.email
, MIN(o.created_at) first_order_at
, COUNT(distinct o.id) number_of_orders
FROM analytics-engineers-club.coffee_shop.orders o 
LEFT JOIN analytics-engineers-club.coffee_shop.customers c on o.customer_id=c.id
GROUP BY 1,2,3
ORDER BY first_order_at
LIMIT 5

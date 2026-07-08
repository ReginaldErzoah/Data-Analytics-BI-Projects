/*
==========================================================
02 - Customer Analytics
==========================================================
*/


/* Customers by Country */

SELECT
Country,
COUNT(DISTINCT customer_id) AS Number_of_Customers
FROM RetailTransactions
GROUP BY country
ORDER BY Number_of_Customers DESC;

/*
==========================================================
02 - Customer Analytics
==========================================================
*/


/* Customers by Country */

SELECT
Country,
COUNT(DISTINCT CustomerID) AS Number_of_Customers
FROM RetailTransactions
GROUP BY Country
ORDER BY Number_of_Customers DESC;

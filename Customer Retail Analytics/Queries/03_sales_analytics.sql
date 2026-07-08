/*
03 - Sales Analytics
==========================================================
*/


/* Transactions by Year */

SELECT
strftime('%Y', InvoiceDate) AS Sales_Year,
COUNT(*) AS Number_of_Transactions
FROM RetailTransactions
GROUP BY Sales_Year
ORDER BY Sales_Year;


/* Total Quantity Sold */

SELECT
SUM(Quantity) AS Total_Items_Sold
FROM RetailTransactions;


/* Total Revenue */

SELECT
ROUND(SUM(Quantity * Price),2) AS Total_Revenue
FROM RetailTransactions;

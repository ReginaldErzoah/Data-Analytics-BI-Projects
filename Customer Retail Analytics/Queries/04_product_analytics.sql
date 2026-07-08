/*
04 - Product Analytics
==========================================================
*/


/* Top 10 Products by Quantity Sold */

SELECT
StockCode,
Description,
SUM(Quantity) AS Total_Quantity_Sold
FROM RetailTransactions
GROUP BY
StockCode,
Description
ORDER BY Total_Quantity_Sold DESC
LIMIT 10;


/* Top 10 Products by Revenue */

SELECT
StockCode,
Description,
ROUND(SUM(Quantity * Price),2) AS Revenue
FROM RetailTransactions
GROUP BY
StockCode,
Description
ORDER BY Revenue DESC
LIMIT 10;

/*
04 - Product Analytics
==========================================================
*/


/* Top 10 Products by Quantity Sold */

SELECT
stockcode,
description,
SUM(quantity) AS Total_Quantity_Sold
FROM RetailTransactions
GROUP BY
stockcode,
description
ORDER BY Total_Quantity_Sold DESC
LIMIT 10;


/* Top 10 Products by Revenue */

SELECT
stockcode,
description,
ROUND(SUM(quantity * Price),2) AS Revenue
FROM RetailTransactions
GROUP BY
stockcode,
description
ORDER BY Revenue DESC
LIMIT 10;

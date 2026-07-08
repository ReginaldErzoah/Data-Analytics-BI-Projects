/*
01 - Data Exploration
==========================================================

Objective:
Understand the dataset structure, size, coverage,
and time period before performing business analysis.
*/


/* 01 - Preview Dataset */

SELECT *
FROM RetailTransactions
LIMIT 10;


/* 02 - Total Transaction Records */

SELECT
COUNT(*) AS Total_Transactions
FROM RetailTransactions;


/* 03 - Dataset Time Period */

SELECT
MIN(invoicedate) AS First_Transaction_Date,
MAX(invoicedate) AS Last_Transaction_Date
FROM RetailTransactions;


/* 04 - Total Unique Customers */

SELECT
COUNT(DISTINCT customer_id) AS Total_Customers
FROM RetailTransactions;


/* 05 - Total Unique Products */

SELECT
COUNT(DISTINCT stockcode) AS Total_Products
FROM RetailTransactions;


/* 06 - Total Countries */

SELECT
COUNT(DISTINCT country) AS Total_Countries
FROM RetailTransactions;


/* 07 - Countries Represented */

SELECT DISTINCT
country
FROM RetailTransactions
ORDER BY country;

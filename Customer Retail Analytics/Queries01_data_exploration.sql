SELECT *
FROM RetailTransactions
LIMIT 10;


SELECT COUNT(*)
FROM RetailTransactions;


SELECT MIN(InvoiceDate),
       MAX(InvoiceDate)
FROM RetailTransactions;

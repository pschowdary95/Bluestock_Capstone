SELECT COUNT(*) FROM fact_nav;

SELECT COUNT(*) FROM fact_transactions;

SELECT COUNT(*) FROM fact_performance;

SELECT AVG(nav) FROM fact_nav;

SELECT MAX(nav) FROM fact_nav;

SELECT MIN(nav) FROM fact_nav;

SELECT SUM(amount) FROM fact_transactions;

SELECT AVG(amount) FROM fact_transactions;

SELECT * FROM fact_performance
WHERE expense_ratio < 1;

SELECT fund_name,aum
FROM fact_performance
ORDER BY aum DESC
LIMIT 5;
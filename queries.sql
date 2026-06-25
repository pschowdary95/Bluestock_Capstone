-- =====================================================
-- Bluestock Mutual Fund Analytics
-- 10 Analytical SQL Queries
-- =====================================================

-- 1. Top 5 funds by AUM
SELECT scheme_name, fund_house, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-------------------------------------------------------

-- 2. Average NAV per month
SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav),2) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-------------------------------------------------------

-- 3. Total SIP inflow by month
SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM fact_sip_industry
ORDER BY month;

-------------------------------------------------------

-- 4. Transactions by State
SELECT
    state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-------------------------------------------------------

-- 5. Funds having expense ratio below 1%
SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-------------------------------------------------------

-- 6. Top Fund Houses by AUM
SELECT
    fund_house,
    ROUND(SUM(aum_crore),2) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC;

-------------------------------------------------------

-- 7. Average Return by Category
SELECT
    category,
    ROUND(AVG(return_3yr_pct),2) AS avg_return
FROM fact_performance
GROUP BY category
ORDER BY avg_return DESC;

-------------------------------------------------------

-- 8. Transaction Type Distribution
SELECT
    transaction_type,
    COUNT(*) AS total
FROM fact_transactions
GROUP BY transaction_type;

-------------------------------------------------------

-- 9. Highest Rated Funds
SELECT
    scheme_name,
    morningstar_rating,
    sharpe_ratio
FROM fact_performance
ORDER BY morningstar_rating DESC,
         sharpe_ratio DESC;

-------------------------------------------------------

-- 10. Benchmark Closing Value
SELECT
    index_name,
    ROUND(MAX(close_value),2) AS highest_close
FROM fact_benchmark
GROUP BY index_name
ORDER BY highest_close DESC;
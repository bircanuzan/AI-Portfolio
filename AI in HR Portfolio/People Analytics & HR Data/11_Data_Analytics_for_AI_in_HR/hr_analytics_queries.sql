-- AI in HR Analytics Lab | Example SQL
-- Synthetic data only. Demonstrates HR analytics query patterns.

-- 1. Workforce overview by department
SELECT
    department,
    COUNT(*) AS headcount,
    ROUND(AVG(tenure_years), 1) AS avg_tenure_years,
    ROUND(AVG(performance_rating), 2) AS avg_performance_rating,
    SUM(exit_12m) AS exits_12m,
    ROUND(100.0 * SUM(exit_12m) / COUNT(*), 1) AS exit_rate_pct
FROM hr_employee_analytics
GROUP BY department
ORDER BY headcount DESC;

-- 2. Skills coverage and capability gaps
SELECT
    primary_skill,
    COUNT(*) AS employees,
    ROUND(AVG(skill_level), 2) AS avg_skill_level,
    SUM(CASE WHEN skill_level < 3 THEN 1 ELSE 0 END) AS employees_below_proficiency
FROM hr_employee_analytics
GROUP BY primary_skill
ORDER BY employees_below_proficiency DESC;

-- 3. Internal mobility by level
SELECT
    level,
    COUNT(*) AS headcount,
    SUM(internal_move_12m) AS internal_moves,
    ROUND(100.0 * SUM(internal_move_12m) / COUNT(*), 1) AS mobility_rate_pct
FROM hr_employee_analytics
GROUP BY level
ORDER BY level;

-- 4. Recruitment source and time-to-fill
SELECT
    hire_source,
    COUNT(*) AS hires_in_sample,
    ROUND(AVG(time_to_fill_days), 1) AS avg_time_to_fill_days
FROM hr_employee_analytics
GROUP BY hire_source
ORDER BY avg_time_to_fill_days;

-- 5. Attrition pattern for analyst investigation (not individual prediction)
SELECT
    department,
    CASE
        WHEN tenure_years < 2 THEN '<2 years'
        WHEN tenure_years < 5 THEN '2-5 years'
        ELSE '5+ years'
    END AS tenure_band,
    COUNT(*) AS employees,
    SUM(exit_12m) AS exits,
    ROUND(100.0 * SUM(exit_12m) / COUNT(*), 1) AS exit_rate_pct
FROM hr_employee_analytics
GROUP BY department,
    CASE
        WHEN tenure_years < 2 THEN '<2 years'
        WHEN tenure_years < 5 THEN '2-5 years'
        ELSE '5+ years'
    END
ORDER BY department, tenure_band;

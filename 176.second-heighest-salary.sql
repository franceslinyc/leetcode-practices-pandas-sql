-- 176. Second Heighest Salary
-- https://leetcode.com/problems/second-highest-salary/

-- This does not take care of NULL

SELECT DISTINCT
    Salary AS SecondHighestSalary
FROM
    Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1 -- LIMIT 1 Return 1 row
                 -- OFFSET 1 Skip 1st row
; 

-- This does

SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;
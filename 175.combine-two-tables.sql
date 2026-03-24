-- 175. Combine Two Tables
-- https://leetcode.com/problems/combine-two-tables/description/

SELECT FirstName, LastName, City, State
FROM Person 
LEFT JOIN Address
    ON Person.PersonId = Address.PersonId
;
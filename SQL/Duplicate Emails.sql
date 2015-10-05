-- Duplicate Emails
-- for leetcode problems
-- 2015.10.06 by zhanglin

-- Problem Link:
-- https://leetcode.com/problems/duplicate-emails/

-- Problem:
-- Write a SQL query to find all duplicate emails in a table named Person.

-- +----+---------+
-- | Id | Email   |
-- +----+---------+
-- | 1  | a@b.com |
-- | 2  | c@d.com |
-- | 3  | a@b.com |
-- +----+---------+
-- For example, your query should return the following for the above table:

-- +---------+
-- | Email   |
-- +---------+
-- | a@b.com |
-- +---------+

-- Write your MySQL query statement below
select distinct p1.Email from
Person p1 join Person p2 on
p1.Email = p2.Email where
p1.Id != p2.Id;



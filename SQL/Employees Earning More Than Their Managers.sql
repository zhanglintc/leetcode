-- Employees Earning More Than Their Managers
-- for leetcode problems
-- 2015.10.06 by zhanglin

-- Problem Link:
-- https://leetcode.com/problems/employees-earning-more-than-their-managers/

-- Problem:
-- The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

-- +----+-------+--------+-----------+
-- | Id | Name  | Salary | ManagerId |
-- +----+-------+--------+-----------+
-- | 1  | Joe   | 70000  | 3         |
-- | 2  | Henry | 80000  | 4         |
-- | 3  | Sam   | 60000  | NULL      |
-- | 4  | Max   | 90000  | NULL      |
-- +----+-------+--------+-----------+
-- Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

-- +----------+
-- | Employee |
-- +----------+
-- | Joe      |
-- +----------+

-- Write your MySQL query statement below
select emp.Name from
  Employee emp join Employee mana on
  emp.ManagerId = mana.Id
where
  emp.Salary > mana.Salary;



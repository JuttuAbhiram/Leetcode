# Write your MySQL query statement below
select emp.unique_id,e.name
from Employees e
Left Join EmployeeUNI emp ON emp.id=e.id
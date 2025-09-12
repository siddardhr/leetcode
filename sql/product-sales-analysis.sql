select product_name, year, price
from sales join product on sales.product_id = product.product_id

#project employeess

select project_id, round(avg(experience_years), 2) as average_years
from project left join employee on project.employee_id = employee.employee_id
group by project_id

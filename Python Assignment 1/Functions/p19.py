def average(salaries):
    
    total_salary = sum(salaries)   
    average_salary = total_salary / len(salaries)  
    return average_salary

 
employee_salaries = [50000, 60000, 75000, 80000, 90000]
result = average(employee_salaries)
print(f"The average salary is: {result}")  
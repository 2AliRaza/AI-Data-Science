def sum_of_even_numbers(numbers):
     sum=0
     for i in numbers:
          if i%2==0:
            sum= sum+i

     return sum


numbers = [1, 2, 3, 4, 5, 6]
result = sum_of_even_numbers(numbers)
print(f"The sum of even numbers is: {result}")
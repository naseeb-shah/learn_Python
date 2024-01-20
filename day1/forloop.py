def find_first_occurrence(nums, target):
    for x in range(len(nums)):
        if nums[x]==target:
            return x
            
    return -1       

   






    """
    Given a list of integers, find the index of the first occurrence of the target value.

    Parameters:
    - nums (list of int): The list of integers.
    - target (int): The target value to find.

    Returns:
    - int: The index of the first occurrence of the target value, or -1 if not found.
    """
   

# Example Usage:
numbers = [5, 8, 3, 2, 8, 6, 8, 9, 4]
target_value = 10
result = find_first_occurrence(numbers, target_value)
# print(f"The first occurrence of {target_value} is at index {result}.")
# sum of all elements of list
def sumOfNumbers(nums):
    sum=0
    for x in range(len(nums)):
        sum+=nums[x]
    return sum

# print("Sum of Array Elements",sumOfNumbers(numbers))
# Write a function that calculates the sum of the digits of a given positive integer.

def calculatesPositiveSumOne(num):
    sum=0
    for i in range(1,num+1):
        sum+=i
    print(sum)
    # Second way math approach
    sum2=num*((num+1)/2)
    print(sum2)

# calculatesPositiveSumOne(50)
# Write a function to find the factorial of a given non-negative integer.
# 5 factorial=1*2*3*4*5=120
    
def factorial(num):
    if num==0 or num==1:
        return 1
    result=1
    for index in range(1,num+1):

        result=result*index
        # print(result)
    return result

# print("Factorial ",factorial(5))


#Write a function to generate the Fibonacci series up to a specified term.
def generate_fibonacci_series(n):
    """
    Generate the Fibonacci series up to the n-th term.

    Parameters:
    - n (int): Positive integer specifying the term up to which the series should be generated.

    Returns:
    - list: List containing the Fibonacci series.
    """
    initial_Series=[0,1]
    # Your code here
    for x in range(2,n):
        nextElement= initial_Series[-1]+initial_Series[-2]
        initial_Series.append(nextElement)
    return initial_Series
# Example Usage:
term = 8
fibonacci_series = generate_fibonacci_series(term)
# print(f"The Fibonacci series up to the {term}-th term is: {fibonacci_series}")

# reverse list
# 


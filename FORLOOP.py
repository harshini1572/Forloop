#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to print the numbers from 1 to 10 using a `for` loop.

# In[1]:


for i in range(0,9):
    print(i)


# 2. Create a program that calculates the sum of all numbers in a list using a `for` loop.

# In[8]:


l=[2,3,4]
total=0
for i in l:
    total+=i
print(total)


# 3. Write a program to print the characters of a string in reverse order using a `for` loop.

# In[18]:


def reverse(str):
    str1=""
    for i in str:
        str1=i+str1
    return str1
str="string"
print(reverse(str))
    
        


# 4. Develop a program that finds the factorial of a given number using a `for` loop.

# In[20]:


def fact(n):
    return 1 if n==0 or n==1 else n*fact(n-1)
n=5
print("factorial of ",n,"is",fact(n))


# 5. Create a program to print the multiplication table of a given number using a `for` loop.

# In[34]:


n=int(input())
print("the multiplication table of:",n)
for count in range(1,11):
    print(n,'x',count,'=',n*count)


# 6. Write a program that counts the number of even and odd numbers in a list using a `for` loop.

# In[39]:


l=[2,3,5]
even=0
odd=0
for i in l:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("count of even is",even)
print("count of odd is",odd)


# 7. Develop a program that prints the squares of numbers from 1 to 5 using a `for` loop.

# In[42]:


for i in range(1,6):
    i=i*i
    print(i)


# 8. Create a program to find the length of a string without using the `len()` function.

# In[53]:


str="string"
count=0
for i in str:
    count+=1
print(count)


# 9. Write a program that calculates the average of a list of numbers using a `for` loop.

# In[54]:


n=int(input("no of elements:"))
a=[]
for i in range(0,n):
    ele=int(input("enter elements"))
    a.append(ele)
avg=sum(a)/n
print(avg)


# 10. Develop a program that prints the first `n` Fibonacci numbers using a `for` loop.

# In[67]:



def fibonacci(n):
    if n<=1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
nterm=10
if nterm<=0:
    print("enter a number")
else:
    print("fibonacci series")
    for i in range(nterm):
        print(fibonacci(i))


# 11. Write a program to check if a given list contains any duplicates using a `for` loop.

# In[69]:


l=[2,3,3,5,6,7,7,9]
unique=[]
duplicate=[]
for i in l:
    if i not in unique:
        unique.append(i)
    elif i not in duplicate:
        duplicate.append(i)
print(duplicate)


# 12. Create a program that prints the prime numbers in a given range using a `for` loop.

# In[74]:


def prime(n):
    if(n==1 or n==0): return False
    
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
N=100
for i in range(1,N+1):
    if(prime(i)):
        print(i)


# 13. Develop a program that counts the number of vowels in a string using a `for` loop.

# In[86]:


def vowels(string):
    count=0
    vowel=set("AEIOUaeiou")
    for i in string:
        if i in vowel:
            count=count+1
    print(count)
string="geek"
vowels(string)
       


# 14. Write a program to find the maximum element in a 2D list using a nested `for` loop.

# In[ ]:


def maximum(l):
    for i in l:
        for j in l:


# 15. Create a program that removes all occurrences of a specific element from a list using a `for` loop.

# In[89]:


def remove(l):
    for i in l:
        if i is element:
            l.remove(i)
    print(l)
l=[1,2,3,2]
element=2
remove(l)
    


# 16. Develop a program that generates a multiplication table for numbers from 1 to 5 using a nested `for` loop.

# In[98]:


max_no=5
for i in range(1,6):
    for j in range(1,11):
        print(i,"x",j,"=",i*j,"\n")
        


# 17. Write a program that converts a list of Fahrenheit temperatures to Celsius using a `for` loop.

# In[137]:


def fartocel(l):
    for i in l:
        Celsius = ((i-32)*(5/9))
        new.append(Celsius)
    return new
l=[32,45]
fartocel(l)


# 18. Create a program to print the common elements from two lists using a `for` loop.

# In[136]:


def similar(a,b):
    common_dict={}
    for elem in a:
        if elem in common_dict:
            common_dict[elem]+=1
        else:
            common_dict[elem]=1
    for elem in b:
        if elem in common_dict:
            common_dict[elem]+=1
        else:
            common_dict[elem]=1
    common = [ele for ele in common_dict if common_dict[ele] == 2]
    if len(common) > 0:
        return common 
    else: 
        return "no common elements" # return a message saying so

a = [1, 2, 5]
b = [5, 6,]
print(similar(a, b))


# 19. Develop a program that prints the pattern of right-angled triangles using a `for` loop. Use ‘*’ to draw the
# pattern

# In[139]:


for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()


# 20. Write a program to find the greatest common divisor (GCD) of two numbers using a `for` loop.

# In[142]:


x=int(input())
y=int(input())
if x>y :
    x,y=y,x
for i in range(1,x+1):
    if x%i==0 and y%i==0:
        gcd=i
print(gcd)
    


# 21. Create a program that calculates the sum of the digits of numbers in a list using a list comprehension.

# In[1]:


numbers = [123, 456, 789]
sums = [sum(int(digit) for digit in str(number)) for number in numbers]
print(sums)  # Output: [6, 15, 24]


# In[2]:


#Q22. Write a program to find the prime factors of a given number using a for loop and list comprehension.

def prime_factors(n):
    factors = []
    # Check for number of 2s
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    # Check for odd factors
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    # If n becomes a prime number greater than 2
    if n > 2:
        factors.append(n)
    return factors

number = 56
print(prime_factors(number)) 


# In[3]:


#Q23. Develop a program that extracts unique elements from a list and stores them in a new list using a 
# list comprehension.

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list({num for num in numbers})
print(unique_numbers) 


# In[4]:


#Q24. Create a program that generates a list of all palindromic numbers up to a specified limit using a list
#  comprehension.

limit = 100
palindromes = [num for num in range(limit) if str(num) == str(num)[::-1]]
print(palindromes) 


# In[5]:


#Q25. Write a program to flatten a nested list using list comprehension.

nested_list = [[1, 2, 3], [4, 5], [6]]
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list) 


# In[6]:


#Q26. Develop a program that computes the sum of even and odd numbers in a list separately using list comprehension.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
sum_even = sum(num for num in numbers if num % 2 == 0)
sum_odd = sum(num for num in numbers if num % 2 != 0)
print(f"Sum of even numbers: {sum_even}")  
print(f"Sum of odd numbers: {sum_odd}")   


# In[7]:


#Q27. Create a program that generates a list of squares of odd numbers between 1 and 10 using list comprehension.

squares_of_odds = [num**2 for num in range(1, 11) if num % 2 != 0]
print(squares_of_odds)


# In[8]:


#Q28. Write a program that combines two lists into a dictionary using list comprehension.

keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = {keys[i]: values[i] for i in range(len(keys))}
print(dictionary) 


# In[9]:


#Q29. Develop a program that extracts the vowels from a string and stores them in a list using list comprehension.

string = "hello world"
vowels = [char for char in string if char in 'aeiou']
print(vowels) 


# In[10]:


#Q30. Create a program that removes all non-numeric characters from a list of strings using list comprehension.

strings = ['abc123', 'def456', 'ghi789']
cleaned = [''.join(char for char in string if char.isdigit()) for string in strings]
print(cleaned)


# In[11]:


#CHALLENGING


# In[12]:


#31. Write a program to generate a list of prime numbers using the Sieve of Eratosthenes algorithm and list 
# comprehension.

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if primes[p]]

limit = 50
prime_numbers = sieve_of_eratosthenes(limit)
print(prime_numbers) 


# In[13]:


#32. Create a program that generates a list of all Pythagorean triplets up to a specified limit using list 
# comprehension.

def pythagorean_triplets(limit):
    return [
        (a, b, c) for a in range(1, limit + 1)
        for b in range(a, limit + 1)
        for c in range(b, limit + 1)
        if a * a + b * b == c * c
    ]

limit = 30
triplets = pythagorean_triplets(limit)
print(triplets)  


# In[14]:


#33. Develop a program that generates a list of all possible combinations of two lists using list comprehension.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combinations = [(x, y) for x in list1 for y in list2]
print(combinations)  


# In[15]:


#34. Write a program that calculates the mean, median, and mode of a list of numbers using list comprehension.

from statistics import mean, median, mode

numbers = [1, 2, 3, 4, 4, 5, 6]

mean_value = mean(numbers)
median_value = median(numbers)
mode_value = mode(numbers)

print(f"Mean: {mean_value}") 
print(f"Median: {median_value}") 
print(f"Mode: {mode_value}")  


# In[16]:


#Q35. Create a program that generates Pascal's triangle up to a specified number of rows using list comprehension.


def generate_pascals_triangle(n):
    triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle

rows = 5
triangle = generate_pascals_triangle(rows)
for row in triangle:
    print(row)


# In[17]:


#Q36. Develop a program that calculates the sum of the digits of a factorial of numbers from 1 to 5 using 
# list comprehension.

import math

def sum_of_digits(number):
    """Calculate the sum of the digits of a number."""
    return sum(int(digit) for digit in str(number))

# Calculate the factorial of numbers from 1 to 5
factorials = [math.factorial(n) for n in range(1, 6)]

# Calculate the sum of digits of each factorial
sum_digits = [sum_of_digits(factorial) for factorial in factorials]

print(sum_digits) 


# In[18]:


#Q37. Write a program that finds the longest word in a sentence using list comprehension.

sentence = "Find the longest word in this sentence"
longest_word = max(sentence.split(), key=len)
print(longest_word)  


# In[19]:


#Q38. Create a program that filters a list of strings to include only those with more than three vowels 
# using list comprehension.

def count_vowels(word):
    vowels = "aeiouAEIOU"  # both lowercase and uppercase vowels
    return sum(1 for char in word if char in vowels)

def filter_strings_by_vowels(strings):
    return [word for word in strings if count_vowels(word) > 3]

# Example usage
strings_list = ["hello", "education", "beautiful", "sky", "algorithm"]
filtered_list = filter_strings_by_vowels(strings_list)

print(filtered_list)


# In[20]:


#Q39. Develop a program that calculates the sum of the digits of numbers from 1 to 1000 using list comprehension.

def sum_of_digits(number):
    """Calculate the sum of the digits of a number."""
    return sum(int(digit) for digit in str(number))

# Calculate the sum of digits for numbers from 1 to 1000
sum_digits = [sum_of_digits(n) for n in range(1, 1001)]

print(sum(sum_digits)) 


# In[21]:


#Q40. Write a program that generates a list of prime palindromic numbers using list comprehension.

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

limit = 1000
prime_palindromes = [n for n in range(2, limit) if is_prime(n) and is_palindrome(n)]
print(prime_palindromes)  


# In[ ]:





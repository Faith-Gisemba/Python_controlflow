# Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50. 
def print_even_numbers():
    x = 0
    while x<50:
        x+= 1
        if x%2 != 0:
            continue
        print(x)


# Write a function that takes an integer argument and prints "Prime" if the number is prime, and "Not prime" if the number is not prime.
def prime_number(number):
    if number <= 1:
        for i in range(2, number):
            if number % i == 0:
                print("Not prime")
            break
            else:
                print("Prime")

    
# Write a function that takes a list of integers as input and prints the sum of all the even numbers in the list.
def sum_even_numbers(numbers):
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    print(even_sum)


# Write a function that takes any two integers as input, and prints the sum of all the numbers between the two integers (inclusive) that are divisible by 3.
def add_integer(int1,int2):
    b=0
    for i in range(int1,int2):
        if i%2!=0:
            b+=i
    print(b)

"""
Solutions to module 1
Student: Sepehr Mohammadi
Mail: sepehr.mohammadi.1613@student.uu.se
Reviewed by: David Meadon
Reviewed date: 02/09/2022
"""

import random
import time


def power(x, n):         # Optional
    if n==0:
        return 1
    elif n > 0:
        return x * power(x,n-1)
    else:
        return (1/x) * power(x, n+1)


def multiply(m, n):      # Compulsory
    if m==0 or n==0:
        return 0
    else:
        return m + multiply (m,n-1)


def divide(t, n):        # Optional
    if n > t:
        return 0
    else:
        return 1 + divide(t-n, n)


def harmonic(n):         # Compulsory
    if n==1:
        return 1
    else:
        return 1/n + harmonic(n-1)


def digit_sum(x):        # Optional
    if x==0:
        return 0
    else:
        return x % 10 + digit_sum(x//10)


def get_binary(x):       # Optional
    if x==0:
        return ''
    # elif x<0:
    #     return str((-1*x%2 +1) % 2) + get_binary(-1*x//2)
    else:
        return  str(x%2) + get_binary(x//2)


def reverse(s):          # Optional
    if len(s) == 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])


def largest(a):          # Compulsory
    if len(a)==1:
        return a[0]
    else:
        if a[0] >= largest(a[1:]):
            return a[0]
        else:
            return largest(a[1:])

#result = [0]
def count(x, s):         # Compulsory
    if len(s) == 0:
        return 0
    else:
        if s[0] == x:
            #result[0] += 1
            return count(x, s[1:]) + 1
            
        elif type(s[0])==list:
            return count(x, s[1:]) + count(x, s[0])
        else: 
            return count(x, s[1:])



def zippa(l1, l2):       # Compulsory
    if len(l1)==0:
        return l2
    elif len(l2)==0:
        return l1
    else:
        return [l1[0], l2[0]] + zippa(l1[1:],l2[1:])



def bricklek(f, t, h, n): # Compulsory
    if n == 1:
        return [('{}->{}' .format(f, t))] 
    
    else:
        return bricklek (f, h, t, n-1) + [('{}->{}' .format(f, t))] + bricklek (h, t, f, n-1)
coins = [1,5,10,50,100]    
def exchange(a, coins):
    if a==0:
        return 1
    elif a<0 or len(coins) == 0:
        return 0
    else:
        return exchange(a, coins[1:]) + exchange(a-coins[0], coins)

def main():
    """ Demonstates my implementations """
    print(exchange(40,coins))
    print(reverse('abcd'))
    #print(get_binary(-18))
    print(power(2,-3))
    print(divide(15,4))
    print(digit_sum(2))
    print(largest([2,1,2,3,4]))
    print(multiply(5,4))
    print(zippa ([ 2, 4, 6, 8, 10,11],[1, 3, 5]))
    print(bricklek ('f', 't', 'h' ,3))
    #print(bricklek('f', 't', 'h' ,2))
    print(count(4,[1, 4,4, 2, ['a', [ [ 4,4 ] , 3, 4] ] ]))
    print('Bye')
    

if __name__ == "__main__":
    main()
    
####################################################    
    
"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 16: Time for bricklek with 50 bricks:
  t(50) = 2^50 - 1
  
  
  
  
  
  Exercise 17: Time for Fibonacci:
  n = [2, 4, 8, 16, 32]
  t = [5.170000000020991e-05, 3.61000000026479e-05, 3.869999999750462e-05, 0.0005007999999975254, 0.9512465000000034]
    By drawing the diagram for the 2 lists above and comparing it to the diagram of (1.618 ^ n) I verified the statement.(Though I could 
    devide the t(5) to t(4) and reach 1.618, I found this way much more reliable to confirm our equation)
    
    section B:
    t(25) = 0.04 sec ==> t(50) = t(25) * (1.618 ^ 25) = 6706 sec ≈ 1.9 hour
                        t(100) = t(25) * (1.618 ^ 75) ≈ 59800 years
    
    
  
  

  Exercise 20: Comparison sorting methods:

  Insertion Sort
  t(n) = c * (n^2)
  t(1000) = 1 ==> c = 10^-6
  t(10^6) = 10^-6 * 10^12 = 10^6 sec ≈ 277 hours
  t(10^9) = 10^-6 * 10^18 = 10^12 sec ≈ 31709 years
  
  Merge Sort
  t(n) = c * n * log n
  t(1000) = 1 ==> c = 1/3000
  t(10^6) = (1/3000) * 10^6 * log 10^6 = 2000 sec ≈ 33 min
  t(10^9) = (1/3000) * 10^9 * log(10^9) ≈ 833 hours
  
  
  Exercise 21: Comparison Theta(n) and Theta(n log n)
  
  Algorithm A: t(n) = n
  Algorithm B: t(n) = c * n * log n
    t(10) = c * 10 * log 10 = 1 ==> c = 1/10
  we want algorithm A to be faster than algorithm B, so:
  1/10 * n * log n > n
  log n > 10
  n > 10^10
  
  
  
  
  





"""
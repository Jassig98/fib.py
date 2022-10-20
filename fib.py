# Author: Jasmine Singh
# Github username: Jassig98
# Date: October 19, 2022
# Description: fib.py

def fib(num):
    n1=1
    n2=1
    count=0
    while count < num:
        term=n1
        nth= n1+n2
        n1=n2
        n2=nth
        count += 1
    return term

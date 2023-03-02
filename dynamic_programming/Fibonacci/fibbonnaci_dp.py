import time as t
def fibb_naive(n):
    if n<=1:
        return n
    return fibb_naive(n-1)+fibb_naive(n-2)


def fibb_dp(n,d1={}):
    if n<=1:
        return n
    if n in d1.keys():
        return d1[n]
    d1[n]=fibb_dp(n-1,d1)+fibb_dp(n-2,d1)
    return d1[n]


n=int(input('Enter a positive number'))

t1=t.time_ns()
f1=fibb_dp(n)
t2=t.time_ns()
print(f'{f1} in {t2-t1} nano seconds')

t1=t.time_ns()
f1=fibb_naive(n)
t2=t.time_ns()
print(f'{f1} in {t2-t1} nano seconds')
import time

# function implementation
def calc_fib(n):
    if (n <= 1):
        return n
    former_number = 0
    current_number = 1
    fir = 0
    for i in range(1, n):
        fir = former_number + current_number
        former_number = current_number
        current_number = fir

    assert (fir>0), "number cant be negative"
    return fir

# files redirection
pr_time=time.perf_counter()
f=open('input.txt','r')
number=f.readline()
n = int(number)
f=open('output.txt','w')
f.write(str(calc_fib(n) % 10))
print("Time spent is : %s seconds" % (time.perf_counter() - pr_time))
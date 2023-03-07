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
    assert fir > 0 , "number can not be negative"
    return fir

# files redirection
f = open('input.txt', 'r')
number = f.read()
n = int(number)
f = open('output.txt', 'w')
f.write(str(calc_fib(n)))

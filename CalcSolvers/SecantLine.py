##Do this Average Velocity formula for me
import math
def run_formula1(a, b, c, d, x):
    ans = math.pow(x, b)
    ans = float(a*ans)
    cx = float(c*x)
    ans = ans + cx
    ans = ans + d
    return ans

def run_formula2(a, b, x):
    ans = a/(x+b)
    return ans
print("1. Ax^B + Cx + D")
print("2. A/(x + B)")
formula_format = input("Which is the correct format? (1, 2, ect...)")
a = float(input("What is A? "))
b = int(input("What is B? "))
if formula_format == 1:
    c = float(input("What is C? "))
    d = float(input("What is D? "))


x1 = 0
x2 = 0
while(x1 != 1337):
    x1 = float(input("What is stating x? "))
    x2 = float(input("What is the second x? "))
    if formula_format == 1:
        t1 = float(run_formula1(a, b, c, d, x1))
        t2 = float(run_formula1(a, b, c, d, x2))
    else:
        t1 = float(run_formula2(a, b, x1))
        t2 = float(run_formula2(a, b, x2))
    ans1 = t2 - t1
    print(t2, t1)
    print(x2, x1)
    ans2 = x2 - x1
    ans = ans1/ans2
    print(ans)
    

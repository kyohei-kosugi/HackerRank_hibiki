from cmath import phase

num = input()
z = eval(num)
x = z.real
y = z.imag

r = abs(complex(z))
g = phase(complex(z))

print(r)
print(g)
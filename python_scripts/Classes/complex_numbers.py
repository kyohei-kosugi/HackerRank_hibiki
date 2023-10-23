import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        add_real = self.real + no.real
        add_imaginary = self.imaginary + no.imaginary
        return Complex(add_real, add_imaginary)
        
    def __sub__(self, no):
        sub_real = self.real - no.real
        sub_imaginary = self.imaginary - no.imaginary
        return Complex(sub_real, sub_imaginary)
        
    def __mul__(self, no):
        mul_real = self.real * no.real - self.imaginary * no.imaginary
        mul_imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(mul_real, mul_imaginary)
    
    def __truediv__(self, no):
        tmul_real = self.real * no.real + self.imaginary * no.imaginary
        tmul_imaginary = self.imaginary * no.real - self.real * no.imaginary 
        m = no.real**2 + no.imaginary**2
        return Complex(tmul_real / m, tmul_imaginary / m)

    def mod(self):
        a = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(a, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
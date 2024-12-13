class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
 
    def __str__(self):
        return str(self.real) + " + " + str(self.imag) + "i"
 
    def __add__(self, other):        
        real_part = self.real + other.real	# Add the real and imaginary parts separately
        imag_part = self.imag + other.imag
        return ComplexNumber(real_part, imag_part)
 
# Create two complex number objects
complex1 = ComplexNumber(3, 2)
complex2 = ComplexNumber(5, 3)
 
# Add the complex numbers using the + operator
result = complex1 + complex2
 
print("Addition :",result)
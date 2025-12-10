##task3

#Write a function `approx_real_root(coeffs, interval)` that:

#- receives a list `coeffs` of four numbers representing a cubic polynomial,
    #starting with the coefficient of the free term and finishing with the coefficient of x^3
#- receives a tuple `interval = (a, b)` with `a < b`,
#- assumes that **the polynomial has exactly one real root inside this interval**,
#- computes and returns a floating-point approximation of that root,
#- and ensures that the approximation is accurate to at least **1×10⁻⁹** in absolute error

def approx_real_root(coeffs, interval):
    a, b = interval
    
    def f(x):
        return coeffs[0] + coeffs[1]*x + coeffs[2]*x**2 + coeffs[3]*x**3
    
    c = 1 * 10**-6
    x = a
    while x < b:
        if f(x) * f(x + c) < 0:
            c_a, c_b = x, x + c
            break
        x += c
    else:
        c_a, c_b = a, b
    
    d = 1 * 10**-9
    x = c_a
    
    while x <= c_b:
        if -1 * 10**-9 <= f(x) <= 1 * 10**-9:
            return x
        x += d
    
    return c_b
    
    pass

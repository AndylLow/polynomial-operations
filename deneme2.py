# a class that does holds polynomial functions and does basic arithmetic operations on them
    
class Polynomials:
        def __init__(self, polynomial):
            self.polynomial = polynomial
            self.coefs = {}
            for term in polynomial.split('+'):
                if term[0] == '-':
                    sign = -1
                    term = term[1:]
                else:
                    sign = 1
                if term == '1':
                    self.coefs[0] = 1 * sign
                elif term == '-1':
                    self.coefs[0] = -1 * sign
                elif 'x' not in term:
                    self.coefs[0] = int(term) * sign
                elif '^' not in term:
                    self.coefs[1] = int(term[:-1]) * sign
                else:
                    exp, coef = term.split('x^')
                    self.coefs[int(coef)] = int(exp) * sign
        def __add__(self, other):
            result = Polynomials("")
            for exp, coef in self.coefs.items():
                if exp in other.coefs:
                    new_coef = coef + other.coefs[exp]
                    if new_coef != 0:
                        result.coefs[exp] = new_coef
                else:
                    result.coefs[exp] = coef
            for exp, coef in other.coefs.items():
                if exp not in self.coefs:
                    result.coefs[exp] = coef
            return result
        def __sub__(self, other):
            result = Polynomials("")
            for exp, coef in self.coefs.items():
                if exp in other.coefs:
                    new_coef = coef - other.coefs[exp]
                    if new_coef != 0:
                        result.coefs[exp] = new_coef
                else:
                    result.coefs[exp] = coef
            for exp, coef in other.coefs.items():
                if exp not in self.coefs:
                    result.coefs[exp] = -coef
            return result
        def __mul__(self, other):
            result = Polynomials("")
            for exp1, coef1 in self.coefs.items():
                for exp2, coef2 in other.coefs.items():
                    new_exp = exp1 + exp2
                    new_coef = coef1 * coef2
                    if new_exp in result.coefs:
                        result.coefs[new_exp] += new_coef
                    else:
                        result.coefs[new_exp] = new_coef
            return result
        def __str__(self):
            result = ""
            for exp, coef in sorted(self.coefs.items(), reverse=True):
                if coef > 0:
                    result += " + "
                else:
                    result += " - "
                if abs(coef) != 1 or exp == 0:
                    result += str(abs(coef))
                if exp > 0:
                    result += "x"
                if exp > 1:
                    result += "^" + str(exp)
            return result[3:] 


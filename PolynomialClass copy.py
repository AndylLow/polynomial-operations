from collections import defaultdict

class Polynomials:
    def __init__(self, equation):
        self.coefs = defaultdict(float)
        parsed_equation = self.parse_equation(equation)
        for exp, coef in parsed_equation.items():
            self.coefs[exp] += coef


    def parse_equation(self, equation):
        equation = equation.replace(' ', '')
        terms = equation.split('+')
        coefs = defaultdict(float)
        for term in terms:
            if '-' in term:
                subterms = term.split('-')
                for subterm in subterms:
                    if subterm:
                        coef, exp = subterm.split('x^')
                        coefs[int(exp)] += float(coef)
            else:
                if term:
                    coef, exp = term.split('x^')
                    coefs[int(exp)] += float(coef)
        return coefs


    def add_term(self, term, sign):
        if not term:
            coef = 0
            exp = 0
        elif "x" not in term:
            coef = float(term) * sign
            exp = 0
        else:
            if 'x^' in term:
                term = term.replace("x^", "")
                exp = int(term)
                coef = sign
            elif 'x' in term:
                if term == 'x':
                    coef = 1
                    exp = 1
                elif term == '-x':
                    coef = -1
                    exp = 1
                else:
                    if 'x' in term:
                        coef = float(term.split('x')[0])
                        exp = 1
                    else:
                        coef = float(term)
                        exp = 0
        if exp in self.coefs:
            self.coefs[exp] += coef
        else:
            if coef==1:
                self.coefs[exp] = 1
            elif coef==-1:
                self.coefs[exp] = -1
            else:
                self.coefs[exp] = coef



    # a function to add two polynomials
    



    def __add__(self, other):
        new_coefs = defaultdict(float)
        for exp, coef in self.coefs.items():
            new_coefs[exp] += coef
        for exp, coef in other.coefs.items():
            new_coefs[exp] += coef
        return Polynomials(new_coefs)

    
    def __sub__(self, other):
        result = Polynomials("")
        result.coefs = self.coefs.copy()
        for exp, coef in other.coefs.items():
            if exp in result.coefs:
                result.coefs[exp] -= coef
            else:
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
        polynomial = ''
        for exp, coef in sorted(self.coefs.items(), key=lambda x: x[0], reverse=True):
            if coef==0:
                continue
            if exp == 0:
                if coef == 1:
                    polynomial += '+1'
                elif coef == -1:
                    polynomial += '-1'
                else:
                    polynomial += f'{coef}'
            elif exp == 1:
                if coef == 1:
                    polynomial += '+x'
                elif coef == -1:
                    polynomial += '-x'
                elif coef > 0:
                    polynomial += f'+{coef}x'
                else:
                    polynomial += f'{coef}x'
            else:
                if coef == 1:
                    polynomial += f'+x^{exp}'
                elif coef == -1:
                    polynomial += f'-x^{exp}'
                elif coef > 0:
                    polynomial += f'+{coef}x^{exp}'
                else:
                    polynomial += f'{coef}x^{exp}'
        return polynomial



    def derivative(self):
        result = Polynomials("")
        for exp, coef in self.coefs.items():
            if exp != 0:
                new_exp = exp - 1
                new_coef = coef * exp
                result.coefs[new_exp] = new_coef
        return result
    
    def integral(self):
        result = Polynomials("")
        for exp, coef in self.coefs.items():
            new_exp = exp + 1
            new_coef = coef / (new_exp)
            result.coefs[new_exp] = new_coef
        return result

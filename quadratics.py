class Quadratics:
    def __init__(self, val):
        self.a = int(val[0])
        self.b = int(val[1])
        self.c = int(val[2])
        self.det = self.b**2 - 4*self.a*self.c
        self.minmax = self.det / (4*self.a)
        self.sym = -self.b / (2*self.a)
        
        if self.a > 0: self.m = 'Minimum'
        else: self.m = 'Maximum'
    
    def description(self):
        print('''
         _____                            _____      
        |                   ______________     |
        |           -b +/- / b^(2) - 4ac       |
        |      x = _________________________   |
        |                                      |
        |                     2a               |
        |_____                            _____|
''')
        if self.det > 0 or self.det == 0:
            if self.det > 0:
                print('\n\tb^(2) - 4ac has real and unequal roots.')
            else:
                print('\t\tb^(2) - 4ac has real and equal roots.')
        else:
            print('\t\tb^(2) - 4ac has not real and complex roots.')
        print(f'''
\t    Determinant of the function
\t  ___
\t |
\t | 
\t<  b^(2) - 4ac = [{self.b}]^(2) - 4[{self.a}][{self.c}]
\t |             =  {self.det}
\t |___
''')
        pass
    
    def formula(self):
        eqn_p = (-self.b + (self.b**2 - 4*self.a*self.c)**0.5)/(2*self.a)
        eqn_n = (-self.b - (self.b**2 - 4*self.a*self.c)**0.5)/(2*self.a)
        
        if self.det >= 0:
            print(f'''
              ___ {self.a}x^(2) + {self.b}x + {self.c} ___
              
              where a = {self.a},
                    b = {self.b},
                    c = {self.c} 
              
        {self.m} value : {self.minmax}
        Line of Symmetry : {self.sym}
        
        Results ::
         _____
        |
        |      x = {eqn_p} \t|\t x = {eqn_n}
        |_____
        
        ''')
            pass
        else:
            print(f'''
              ___ {self.a}x^(2) + {self.b}x +{self.c} ___
              
        Line of Symmetry : {self.sym}
        
         _____     
        |                         
        |      x = {self.sym} +/-  {(abs(self.b**2 - 4*self.a*self.c))**0.5} i
        |_____
        
        Results ::
         _____
        |
        |      x = {eqn_p} \t|\t x = {eqn_n}
        |_____
        
        ''')
        pass
    
    def rResults(self):
        eqn_p = (-self.b + (self.b**2 - 4*self.a*self.c)**0.5)/(2*self.a)
        eqn_n = (-self.b - (self.b**2 - 4*self.a*self.c)**0.5)/(2*self.a)
        
        self.results = [eqn_p, eqn_n]
        return self.results
        pass


# @Quadratics is a program that solves for the value of the variable x,
# the line of symmetry of the curve and its minimum or its maximum value or the
# value of y at the x coordinate for the line of symmetry.
#
# __ Below is a demo program to run the Quadratic Class with its different functionalities. ___
#
try:
   k = 1
   while k == 1:
       usr = input('Enter the equation [ a , b, c ]: ').split(' ')
       quad = Quadratics(usr)
       quad.formula()
       print(quad.description())
       print(quad.rResults())
       cn = input(' Do you want to quit? [ y / n]').lower().replace(' ', '')
       if cn == 'y':
           k = 0
       else: k = 1
   pass
except Exception as e:
   print(f'''Sorry. There was an error.
Please check error [ {e} ]''')
   pass
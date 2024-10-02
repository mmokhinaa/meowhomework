#Создайте класс для хранения комплексных чисел с инициализатором.
#Реализуйте методы, позволяющие представлять комплексное число в экспоненциальной форме.
#Добавьте функции, позволяющие складывать, вычитать, умножать и делить два комплексных числа, 
#результатом работы которых будет новое комплексное число (именно функции, не методы, перегружать операторы тоже не надо).
import cmath
class Complex:
    def __init__(self, Re, Im):
        ''' Инициализация комплексного числа'''
        self.Re = Re
        self.Im = Im
    
    def vis(self):
        '''Выводит комплексное число'''
        if self.Im>=0 : p = '+'
        else: p = '-'
        return f"{self.Re} {p} {abs(self.Im)} i"

    def expon(self):
        '''Выводит комплексное число в экспоненциальном виде'''
        module = abs(complex(self.Re, self.Im))
        argument = cmath.phase(complex(self.Re, self.Im))
        return f"{module} exp({argument} i)"
    
def addition(Comp1, Comp2):
    '''Сложение 2 комплексных чисел'''
    Re = Comp1.Re + Comp2.Re 
    Im = Comp1.Im + Comp2.Im
    return Complex(Re, Im)

def subtraction(Comp1, Comp2):
    '''Разность второго и первого'''
    Re = Comp1.Re - Comp2.Re 
    Im = Comp1.Im - Comp2.Im
    return Complex(Re, Im)

def multiplication(Comp1, Comp2):
    '''Умножение '''
    Re = Comp1.Re*Comp2.Re - Comp1.Im*Comp2.Im 
    Im = Comp1.Im*Comp2.Re + Comp2.Im*Comp1.Re
    return Complex(Re, Im)

def division(Comp1, Comp2):
    '''Деление первого на второе'''
    d = Comp2.Re ** 2 + Comp2.Im ** 2
    Re = Comp1.Re*Comp2.Re + Comp1.Im*Comp2.Im 
    Im = Comp1.Im*Comp2.Re - Comp2.Im*Comp1.Re
    return Complex(Re/d, Im/d)

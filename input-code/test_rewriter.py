class CheckPlusPlus:
    def check_multioperation(self):

        #caso 1: Plus Plus
        # se chequea que para cualquier operación, si se repite la variable en la izquierda
        # y es una operación binaria unica, se realiza la compresión.
        a = 10
        b = 10

        # casos donde deberia haber compresión.
        a = a + 10
        a = a - 10
        a = a * 10
        a = a / 10

        #casos donde no deberia haber compresión
        b = 10 + b
        b = 10 - b
        b = 10 * b
        b = 10 / b

        return
    
    def check_multiperation_with_self(self):
        #caso 2: Plus Plus
        # mismo caso anterior pero para variables de clase.
        self.a = 10
        self.b = 10

        # casos donde deberia haber compresión.
        self.a = self.a + 10
        self.a = self.a - 10
        self.a = self.a * 10
        self.a = self.a / 10

        #casos donde no deberia haber compresión
        self.b = 10 + self.b
        self.b = 10 - self.b
        self.b = 10 * self.b
        self.b = 10 / self.b

        return
    
    def check_limit_cases(self):
        #caso 3: Plus Plus
        # se chequean casos limites y uso de dos variables en una expresión.
        a = 10
        self.a = -10
        b = 10
        self.b = -10
        c = 20

        # casos donde deberia haber compresión.
        a = a + self.a
        a = a * self.b
        a = a - c
        a = a / a

        self.b = self.b + a
        self.b = self.b * self.a
        self.b = self.b / c
        self.b = self.b * self.b

        #casos donde no deberia haber compresión
        a = b + c
        a = self.a + b

        b = self.b - b
        b = c - b

class CheckIfWithoutElse:

    #caso 1: If Without Else
    def check_basic_if(self):
        a = 10
        if a == 20:
            return a
        else:
            pass
    
    #caso 2: If Without Else
    def check_internal_if(self):
        a = 10
        b = 20
        if a == 20:
            if a == 30:
                a = 20
                if a == 20:
                    return a
                else:
                    return b
            else:
                pass
        else:
            pass
    
    #caso 3: If Without Else
    def check_internal_if_and_elif(self):
        a = 10
        b = 20
        if a == 20:
            if a == 30:
                a = 20
                if a == 20:
                    return a
                if a == 30:
                    return b
                else:
                    return b
            
            elif b == 20:
                return b
            elif b == 30:
                return a
            else:
                pass

        elif b == 0:
            return b
        else:
            pass




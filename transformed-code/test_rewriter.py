class CheckPlusPlus:

    def check_multioperation(self):
        a = 10
        b = 10
        a += 10
        a -= 10
        a *= 10
        a /= 10
        b = 10 + b
        b = 10 - b
        b = 10 * b
        b = 10 / b
        return

    def check_multiperation_with_self(self):
        self.a = 10
        self.b = 10
        self.a += 10
        self.a -= 10
        self.a *= 10
        self.a /= 10
        self.b = 10 + self.b
        self.b = 10 - self.b
        self.b = 10 * self.b
        self.b = 10 / self.b
        return

    def check_limit_cases(self):
        a = 10
        self.a = -10
        b = 10
        self.b = -10
        c = 20
        a += self.a
        a *= self.b
        a -= c
        a /= a
        self.b += a
        self.b *= self.a
        self.b /= c
        self.b *= self.b
        a = b + c
        a = self.a + b
        b = self.b - b
        b = c - b

class CheckIfWithoutElse:

    def check_basic_if(self):
        a = 10
        if a == 20:
            return a

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
        elif b == 0:
            return b
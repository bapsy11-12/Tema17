class optimizar:
    array= []

    def __init__(self,array):
        self.array=array

    def numero(self):
        print("Introduzca un número: ")
        n= int(input())
        return n

    def add (self, n):
        self.array.append(n)

    def media(self):
        suma=0
        for i in self.array:
            suma+=i
            return suma/len(self.array)
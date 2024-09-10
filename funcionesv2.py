print("mas sobre funciones")
def suma_ab(a,b):
    s=a+b
    return s

def resta_ab(a,b):
    e=a-b
    return e

def division_ab(a,b):
    r=a/b
    return r

def multiplicacion_ab(a,b):
    t=a*b
    return t

#llamada a las funciones
n1=int(input("Ingresa el primer numero "))
n2=int(input("Ingresa el segundo numero "))
suma=suma_ab(n1,n2)
resta=resta_ab(n1,n2)
division=division_ab(n1,n2)
multiplicacion=multiplicacion_ab(n1,n2)
print(f"la suma de {n1} + {n2} es {suma}")
print(f"la resta de {n1} - {n2} es {resta}")
print(f"la division de {n1} / {n2} es {division}")
print(f"la multiplicacion de {n1} * {n2} es {multiplicacion}")



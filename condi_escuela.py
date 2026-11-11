# En una escuela, la colegiatura se cobra según el número de materias que el alumno cursa. Cada materia tiene un costo de 50 USD. Adicionalmente:
# • Si el promedio del alumno en el último periodo es mayor o igual a 9: recibe un descuento del 30 % sobre la colegiatura y no se le cobra IVA.
# • Si el promedio es menor a 9: paga la colegiatura completa más un 10 % de IVA, sin descuento.
# Solicite el número de materias que cursa el alumno y su promedio del último periodo. Calcule e imprima el valor total que debe pagar.
#2
from builtins import float, input, int, print


numero_materias =int(input("Digite la cantidad de materias "))
#9.5 8.0
promedio = float(input("Digite su promedio "))

if promedio >= 9 :
    # 100                2
    colegiatura = numero_materias * 50
    #30            100*0.3
    descuento = colegiatura * 30/100
    #70                         100          30
    total_colegiatura =  colegiatura -  descuento

else:
    #100                  2
    colegiatura =  numero_materias * 50
    #10       100*0.10
    iva= colegiatura * 10/100
    #110                      100 +10
    total_colegiatura = colegiatura + iva

print("Valor total ",  total_colegiatura)


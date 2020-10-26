#A00828359 Isaac Arredondo Padron
#A00517141 Juan Angel Mora Moreno
#proposito del programa

#funcion1  calcular área del rectángulo
def calculaArea(l1, l2):
    area = l1 * l2
    return area

#funcion2  calcular perímetro del rectángulo
def calculaPeri(l1,l2):
  l1 = l1 * 2
  l2 = l2 * 2
  peri = l1 + l2
  return peri

#instrucciones de accion
#pedir datos
print("medida de lado 1 del rectángulo")
l1 = float(input())

print("medida de lado 2 del rectángulo")
l2 = float(input())

#desplegar calculo funcion1
area = calculaArea(l1, l2)
print("El area es: ", area)

#desplegar calculo funcion 2
peri = calculaPeri(l1,l2)
print("El perímetro del rectángulo es: ", peri)

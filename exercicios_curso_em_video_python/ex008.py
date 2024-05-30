# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

d = int(input('Digite uma distância em metros: '))
print(f'A medida de {d}m corresponde a')
print(f' {d/1000}km \n {d/100}hm \n {d/10}dam \n {d*10}dm \n {d*100}cm \n {d*1000}mm')
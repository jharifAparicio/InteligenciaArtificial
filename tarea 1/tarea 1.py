import csv
import os

#inicializamos las variables
conteo_genero ={"Male":0,"Female":0}
cantidad_general=0
color_gato=[]
conteo_color={}
edades=[]

#abrimos y leemos la ruta del archivo
file_path = './cats_dataset.csv'

# Abrir y leer el archivo CSV
with open(file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # Imprimir los nombres de las columnas
    print("Columnas:", reader.fieldnames)
    # Contar los géneros
    for row in reader:
        #imprimimos los datos de los gatos
        print(*row.values(), sep=(", "))
        genero = row['Gender']
        if genero in conteo_genero:
            conteo_genero[genero] += 1
    #extraemos las edades de los gatos
        edades.append(int(row['Age (Years)']))
    #extraemos los colores de los gatos
        color_gato.append(row['Color'])

# Calcular el total de gatos
total_gatos = sum(conteo_genero.values())

# Calcular los porcentajes
porcentaje_generos = {genero: (conteo / total_gatos) * 100 for genero, conteo in conteo_genero.items()}

# Calcular la edad promedio
promedio_edades = sum(edades) / len(edades)

# Calcular la cantidad de cada color e imprimir los resultados
for color in color_gato:
    if color in conteo_color:
        conteo_color[color] += 1
    else:
        conteo_color[color] = 1

# Calcular los porcentajes de cada color
porcentaje_color = {color: (conteo / total_gatos) * 100 for color, conteo in conteo_color.items()}

# Escribir los resultados en el archivo .txt
print("Conteo de generos:")
print(f" Macho: {conteo_genero['Male']}")
print(f" Hembras: {conteo_genero['Female']}")
print(f"Total de gatos: {total_gatos}")
print("Porcentaje de géneros:")
print(f" Macho: {porcentaje_generos['Male']:.2f}")
print(f" Hembras: {porcentaje_generos['Female']:.2f}")
print(f"Edad promedio: {promedio_edades} años")
print("Porcentaje de colores:")
for color, porcentaje in porcentaje_color.items():
    print(f" {color}: {porcentaje:.2f} "+"   ")
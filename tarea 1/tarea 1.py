import csv
import os

#inicializamos las variables
conteo_genero ={"Male":0,"Female":0}
cantidad_general=0
color_gato=[]
conteo_color={}
edades=[]

#obtenenmos el directiorio actual
directorio=os.getcwd()
#creamos el archivo de salida
salida='analisis.txt'
path_salida=os.path.join(directorio,salida)

#abrimos y leemos la ruta del archivo
file_path = './cats_dataset.csv'

# Abrir y leer el archivo CSV
with open(file_path, newline='') as csvfile, open(path_salida, 'w') as salida:
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
salida.write(" Conteo de generos:\n")
salida.write(f" Macho: {conteo_genero['Male']}\n")
salida.write(f" Hembras: {conteo_genero['Female']}\n")
salida.write(f"Total de gatos: {total_gatos}\n")
salida.write("Porcentaje de géneros:\n")
salida.write(f" Macho: {porcentaje_generos['Male']:.2f}%\n")
salida.write(f" Hembras: {porcentaje_generos['Female']:.2f}%\n")
salida.write(f"Edad promedio: {promedio_edades} años\n")
salida.write("Porcentaje de colores:\n")
for color, porcentaje in porcentaje_color.items():
    salida.write(f" {color}: {porcentaje:.2f}%\n")
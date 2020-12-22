import pyproj
import csv


# Apertura de archivos
archivo_entrada = open('./tecnicos-32616.csv', 'r')
archivo_salida  = open('./tecnicos-4326.csv', 'w')


lector_lineas = csv.reader(archivo_entrada)
escritor_lineas = csv.writer(archivo_salida, delimiter=',')

p1 = pyproj.Proj(init='epsg:32616')
p2 = pyproj.Proj(init='epsg:4326')

i = 0
for linea in lector_lineas:
    linea_salida = linea

    if (i == 0):
        linea_salida.append('x_4326')
        linea_salida.append('y_4326')
    else:
        x1 = linea[10]
        y1 = linea[11]

        x2, y2 = pyproj.transform(p1,p2,x1,y1)

        linea_salida.append(x2)
        linea_salida.append(y2)

        print(x1, y1, x2, y2)

    i = i + 1

    escritor_lineas.writerow(linea_salida)


# Cierre de archivos
archivo_entrada.close()
archivo_salida.close()

# Importación de datos de técnicos de campo para el Portal Geoespacial del Proyecto Cosecha de Agua en Nicaragua
## Descripción general
Este repositorio contiene la documentación y el código fuente de un programa desarrollado para importar datos de técnicos de campo, incluyendo los productores a los cuales han sido asignados. Estos datos se utilizan para alimentar el [portal geoespacial del proyecto](https://geo-cosecha-agua.github.io/).

El programa recibe los registros contenidos en un archivo CSV, generado a partir de un archivo Excel. Fue desarrollado en el lenguaje de programación [Python](https://www.python.org/) por lo que, para su ejecución, se requiere de un interpretador de ese lenguaje. Se recomienda utilizar el interpretador de Python incluído en la plataforma [Anaconda](https://www.anaconda.com/). Para facilitar su uso y mantenimiento, el programa se ejecuta en un ambiente [Conda](https://docs.conda.io/).

Como salida, el programa genera una capa geoespacial en formato GeoJSON.

En el resto de este documento, se describen las entradas, procesamiento y salidas del programa; y se detallan los comandos necesarios para su ejecución. Se incluye también una sección con los comandos necesarios para crear el ambiente Conda en el que se ejecuta el programa.

## Entradas, procesamiento y salidas
### Entradas
- Archivo CSV

### Procesamiento
- Ejecución del programa ```geo-cosecha-agua-importacion-datos-tecnicos.py```

### Salidas
- Capa geoespacial en formato GeoJSON con datos de técnicos de campo. Se graba en el directorio principal del repositorio.

## Ejecución del programa
Los siguientes comandos deben ejecutarse en la línea de comandos del sistema operativo. Se recomienda utilizar la interfaz de línea de comandos de Anaconda. Se asume que el ambiente Conda ha sido creado de la manera que se muestra en la sección siguiente a esta.
```shell
# Activación del ambiente Conda
$ conda activate geo-cosecha-agua-importacion-datos-tecnicos

# Clonación del repositorio
$ git clone https://github.com/geo-cosecha-agua/geo-cosecha-agua-importacion-datos-tecnicos.git
$ cd geo-cosecha-agua-importacion-datos-tecnicos

# Ejecución del programa
$ python geo-cosecha-agua-importacion-datos-tecnicos.py

# Actualización del repositorio y de los archivos GeoJSON generados
$ git add .
$ git commit -m "Generar datos"
$ git push

# Desactivación del ambiente Conda
$ conda deactivate
```

## Creación y configuración del ambiente Conda
El ambiente Conda solamente debe crearse una vez. Luego puede seguir usándose de la manera que se especifica en la sección anterior.
```shell
# Actualización de Conda
$ conda update -n base -c defaults conda

# Creación del ambiente
$ conda create -n geo-cosecha-agua-importacion-datos-tecnicos

# Activación del ambiente
$ conda activate geo-cosecha-agua-importacion-datos-tecnicos

# Configuración del ambiente
$ conda config --env --add channels conda-forge
$ conda config --env --set channel_priority strict

# Instalación de paquetes
$ conda install python geopandas requests

# Desactivación del ambiente
$ conda deactivate
```

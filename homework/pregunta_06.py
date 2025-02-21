"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd # type: ignore #ignore type

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    # Cargar el archivo tbl1.tsv
    df = pd.read_csv("files/input/tbl1.tsv", sep="\t")

    # Obtener los valores únicos de la columna 'c4', convertirlos a mayúsculas y ordenarlos
    valores_unicos = sorted(df["c4"].str.upper().unique())

    return valores_unicos

# Llamar la función y mostrar el resultado
print(pregunta_06())
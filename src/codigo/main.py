
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import funciones as f


def main():
    ruta = Path(__file__).resolve().parents[1] / "data" / "mxmh_survey_results.csv"

    df = pd.read_csv(ruta)
    df_preparado = f.preparar_datos(df)

    print("ANÁLISIS DE MÚSICA Y SALUD MENTAL")
    print("-" * 40)
    print(f"Registros originales: {len(df)}")
    print(f"Dimensiones preparadas: {df_preparado.shape}")


if __name__ == "__main__":
    main()

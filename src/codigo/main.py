import pandas as pd
import funciones as f


def main():

    df = pd.read_csv("../data/mxmh_survey_results.csv")

    df_preparado = f.preparar_datos(df)

    print("ANÁLISIS DE MÚSICA Y SALUD MENTAL")
    print("-" * 40)
    print(f"Registros originales: {len(df)}")
    print(f"Dimensiones preparadas: {df_preparado.shape}")

    # Ejecutamos los análisis
    f.analizar_h1(df_preparado)
    f.analizar_h2(df_preparado)
    f.analizar_h3(df_preparado)
    f.analizar_h4(df_preparado)

if __name__ == "__main__":
    main()

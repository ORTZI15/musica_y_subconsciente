import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def preparar_datos(df):
    df = df.copy()

    
    df = df.drop(columns=["BPM"]) # Excluir variable no utilizada

    # Codificar frecuencias musicales
    mapa = {
        "Never": 0,
        "Rarely": 1,
        "Sometimes": 2,
        "Very frequently": 3
    }

    columnas = [
        col for col in df.columns
        if col.startswith("Frequency [")
    ]

    for col in columnas:
        df[col] = df[col].map(mapa)

    return df


def analizar_h1(df):

    df_h1 = df[["Hours per day", "Anxiety"]].dropna()

    plt.figure(figsize=(9, 5))

    sns.scatterplot(
        data=df_h1,
        x="Hours per day",
        y="Anxiety",
        alpha=0.4
    )

    plt.title("Relación entre horas de escucha musical y ansiedad")
    os.makedirs("graficos", exist_ok=True)
    plt.xlabel("Horas de escucha diaria")
    plt.ylabel("Nivel de ansiedad (0-10)")

    plt.tight_layout()
    plt.savefig("graficos/H1_horas_ansiedad.png", dpi=300)
    plt.show()


def analizar_h2(df):

    df_h2 = df[["Fav genre", "Depression"]].dropna()

    resumen_h2 = df_h2.groupby("Fav genre")["Depression"].agg(
        ["count", "mean"]
    )

    resumen_h2 = resumen_h2.sort_values(
        by="mean",
        ascending=False
    )

    print("\nH2 - DEPRESIÓN POR GÉNERO MUSICAL")
    print(resumen_h2.round(2))

    plt.figure(figsize=(10, 7))

    sns.barplot(
        data=resumen_h2.reset_index(),
        x="mean",
        y="Fav genre",
        color="steelblue",
        errorbar=None
    )

    plt.title("Nivel medio de depresión por género musical favorito")
    plt.xlabel("Puntuación media de depresión (0-10)")
    plt.ylabel("Género musical")

    plt.tight_layout()
    plt.savefig("graficos/H2_genero_depresion.png", dpi=300)
    plt.show()

def analizar_h3(df):

    columnas_frecuencia = [
        col for col in df.columns
        if col.startswith("Frequency [")
    ]

    indicadores = ["Anxiety", "Depression", "Insomnia", "OCD"]

    resultados = []

    for genero in columnas_frecuencia:

        grupo = df.groupby(genero)[indicadores].mean()

        if 0 in grupo.index and 3 in grupo.index:

            diferencia = grupo.loc[3] - grupo.loc[0]
            diferencia.name = genero.replace("Frequency [", "").replace("]", "")

            resultados.append(diferencia)

    resumen_h3 = pd.DataFrame(resultados)

    print("\nH3 - DIFERENCIAS SEGÚN FRECUENCIA MUSICAL")
    print(resumen_h3.round(2))

    plt.figure(figsize=(10, 8))

    sns.heatmap(
        resumen_h3,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0
    )

    plt.title("Diferencias en salud mental según frecuencia musical")
    plt.xlabel("Indicadores de salud mental")
    plt.ylabel("Género musical")

    plt.tight_layout()
    plt.savefig("graficos/H3_frecuencia_salud_mental.png", dpi=300)
    plt.show()

def analizar_h4(df):

    columnas = [
        "Music effects",
        "Anxiety",
        "Depression",
        "Insomnia",
        "OCD"
    ]

    df_h4 = df[columnas].dropna()

    resumen_h4 = df_h4.groupby("Music effects")[
        ["Anxiety", "Depression", "Insomnia", "OCD"]
    ].mean()

    print("\nH4 - EFECTOS PERCIBIDOS DE LA MÚSICA")
    print(resumen_h4.round(2))

    resumen_grafico = resumen_h4.reset_index().melt(
        id_vars="Music effects",
        var_name="Indicador",
        value_name="Puntuación media"
    )

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=resumen_grafico,
        x="Music effects",
        y="Puntuación media",
        hue="Indicador",
        errorbar=None
    )

    plt.title("Salud mental según los efectos percibidos de la música")
    plt.xlabel("Efecto percibido")
    plt.ylabel("Puntuación media (0-10)")
    plt.ylim(0, 10)

    plt.tight_layout()
    plt.savefig("graficos/H4_efectos_percibidos.png", dpi=300)
    plt.show()
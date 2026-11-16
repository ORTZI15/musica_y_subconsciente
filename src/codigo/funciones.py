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
from flask import Flask

import pandas as pd

from buk import normalizeBuk

from google import normalizeGoogle

from generateExcel import generateExcel

app = Flask(__name__)

@app.route("/Normalize")
def normalize():

    # Leo ambos documentos
    Google_df = pd.read_excel("./assets/Google.xlsx")

    Buk_df = pd.read_excel("./assets/Buk.xlsx")

    # Normalizo las tablas
    Google_df = normalizeGoogle(Google_df)

    Buk_df = normalizeBuk(Buk_df)

    # Genero documento excel
    generateExcel(Google_df, Buk_df)

    return Google_df.head().to_html()

@app.route("/Compare")
def compare():

    # Leo ambos documentos
    Google_df = pd.read_excel("./assets/Google.xlsx")

    Buk_df = pd.read_excel("./assets/Buk.xlsx")

    # Genero copia df de google
    Google_df_filled = Google_df.copy()

    # Genero columna nombre completo
    Google_df_filled['Nombre completo'] = Google_df_filled['First Name [Required]'].astype(str) + " " + Google_df['Last Name [Required]'].astype(str)

    Buk_df['Nombre completo'] = Buk_df['Empleado - Nombre'] + " " + Buk_df['Empleado - Apellido']

    # Dataframe que contiene valores de rut vacio.
    missing_rut = Google_df_filled[Google_df_filled['Employee ID'].isnull()]

    return missing_rut.head().to_html()

    # # Recorro cada fila con rut faltante.
    # for index, row in missing_rut.iterrows():

    #     match = Buk_df[Buk_df['Nombre completo'] == row['Nombre completo']]

    #     if not match.empty:

    #         Google_df_filled.at[index, 'Employee ID'] = match.iloc[0]['Empleado - RUT']

    # generadorExcel = pd.ExcelWriter('./assets/GoogleActualizado.xlsx')

    # Google_df_filled.to_excel(generadorExcel)

    # return Google_df.head().to_html()

if __name__ == "__main__":
    
    app.run()
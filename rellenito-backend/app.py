import io

from flask import Flask, request, send_file

import pandas as pd

from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/UploadFile", methods=['POST'])
def normalize():

    try:

        google_file = request.files['Google'] 

        buk_file = request.files['Buk'] 

        Google_df = pd.read_excel(google_file)

        Buk_df = pd.read_excel(buk_file)

        Google_df_copy = Google_df.copy()

        # Transformar los centro de costo a string
        Buk_df['Trabajo - Centro de Costo'] = Buk_df['Trabajo - Centro de Costo'].astype("string") # Es type object

        Google_df_copy['Cost Center'] = Google_df_copy['Cost Center'].astype("string") # Es type object

        # Transformar los rut a string
        Buk_df['Empleado - RUT'] = Buk_df['Empleado - RUT'].astype("string")

        Google_df_copy['Employee ID'] = Google_df_copy['Employee ID'].astype("string")

        # # Recorro cada fila con rut faltante.
        for index, row in Google_df_copy.iterrows():

            match = Buk_df[
            
                (Buk_df['Empleado - Email'] == row['Email Address [Required]']) & 
            
                (Buk_df['Trabajo - Centro de Costo'] == row['Cost Center']) &

                (Buk_df['Empleado - Nombre'].str.contains(row['First Name [Required]'], case=False))
            
            ]

            if not match.empty and pd.isna(Google_df.at[index, 'Employee ID']):

                Google_df.at[index, 'Employee ID'] = match.iloc[0]['Empleado - RUT']

        # Google_df.to_excel('./assets/GoogleActualizado.xlsx', index=False)  # index=False para no escribir los índices

        # Guardar el DataFrame actualizado en un archivo Excel en memoria
        buffer = io.BytesIO()

        Google_df.to_excel(buffer, index=False)

        buffer.seek(0)

        # Devolver el archivo generado como respuesta
        return send_file(

            buffer,

            as_attachment=True,
            
            download_name='GoogleActualizado.xlsx',
            
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        
        )

    except Exception as e:

        return {'error': str(e)}, 500
    
if __name__ == "__main__":
    
    app.run()
import pandas as pd

def generateExcel (df1, df2):

        # Genero documento excel
    GeneradorExcel = pd.ExcelWriter('./assets/Users Data.xlsx')

    df1.to_excel(
        
        # './assets/Users Data.xlsx', 

        GeneradorExcel,
        
        columns=[
            
            'Nombre completo', 
            
            'Nombre', 
            
            'Apellido', 
            
            'Email corporativo', 
            
            'Rut', 
            
            'Tiene rut'
            
        ], 
        
        index=False,

        sheet_name = 'Google'
        
    )

    df2.to_excel(

        GeneradorExcel,

        columns=[
            
            'Nombre completo', 
            
            'Nombre', 
            
            'Apellido', 
            
            'Email corporativo', 
            
            'Rut', 
            
            'Tiene rut',

            'Centro de costo',
            
        ], 
        
        index=False,

        sheet_name = 'Buk'

    )

    GeneradorExcel.close()
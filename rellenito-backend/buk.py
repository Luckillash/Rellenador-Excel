import numpy as np

def normalizeBuk (df):

    # Filtro solo los empleados activos.
    df = df[df['Empleado - Estado'] == 'Activo']

    # Genero columna Nombre completo.
    df['Nombre completo'] = df['Empleado - Nombre'] + " " + df['Empleado - Apellido']

    # Genero columna tiene rut.
    df['Tiene rut'] = np.where(df['Empleado - RUT'].isnull(), "No", "Yes")

    # Renombro las columnas.
    df.rename(columns= {

        'Empleado - Nombre': 'Nombre',

        'Empleado - Apellido': 'Apellido',

        'Empleado - Email': 'Email corporativo',

        'Empleado - RUT': 'Rut',

        'Trabajo - Centro de Costo': 'Centro de costo'

    }, inplace=True)

    # Ordeno las columnas por nombre completo.
    df = df.sort_values('Nombre completo')

    return df
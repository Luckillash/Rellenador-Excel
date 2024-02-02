import numpy as np

def normalizeGoogle (df):

    df['Nombre completo'] = df['First Name [Required]'].astype(str) + " " + df['Last Name [Required]'].astype(str)

    df['Tiene rut'] = np.where(df['Employee ID'].isnull(), "No", "Yes")

    df.rename(columns= {

        'First Name [Required]': 'Nombre',

        'Last Name [Required]': 'Apellido',

        'Email Address [Required]': 'Email corporativo',

        'Employee ID': 'Rut'

    }, inplace=True)

    return df
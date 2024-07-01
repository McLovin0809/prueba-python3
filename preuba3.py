
marcas = ['toyota','ford','chevrolet']
listado = []

titulo = '''
------------------------------------------------------------------------------------
marca               año de fabr.     kilometraje     cos. reparacion    impuesto    casto total
'''

def registrar():
    while True:
        try:
            marca = input(f'marca {marcas}: ').strip().lower()
            anofabri = int(input('año de fabricacion: '))
            kilometraje = int(input('kilometraje'))
            reparacion = int(input('costo de reparacion: '))
            if marca in marcas and anofabri>0 and kilometraje>0 and reparacion>0:
                 impuesto = round(reparacion*0.08)
                 total = reparacion + impuesto
                 listado.append([marca, anofabri, kilometraje, reparacion, impuesto, total])
                 input('ingresado con exito..')
                 break
            else:
                 input('falta un parametro..')
        except Exception as e:
            input(f'excep de: {str[e]}')

def listartodo():
    salida = titulo
    for fil in listado:
         salida += f'{fil[0]:10s}'
         salida += f'{fil[1]:17d}'
         salida += f'{fil[2]:17d}'
         salida += f'{fil[3]:17d}'
         salida += f'{fil[4]:17d}'
         salida += f'{fil[5]:17d}'
         salida += '\n'
    return salida

def listarmarca(marcas):
    salida = titulo
    for fil in listado:
         if marcas == fil[0]:
            salida += f'{fil[0]:10s}'
            salida += f'{fil[1]:17d}'
            salida += f'{fil[2]:17d}'
            salida += f'{fil[3]:17d}'
            salida += f'{fil[4]:17d}'
            salida += f'{fil[5]:17d}'
            salida += '\n'
    return salida

def imprimir():
    try:
        opc = input(f'imprimi [todo/{marcas}]').strip().lower()
        if opc == 'todo':
            with open('listado.txt', 'w') as archivo:
                archivo.write(listartodo())
        elif opc in marcas:
            with open('listado.txt','w') as archivo:
                archivo.write(listarmarca(opc))
        else:
            input('error ')
    except Exception as e:
        input(f'excep de: {str[e]}')

while True:
    try:
        menu = int(input('''
        1.regostrar vehiculo
        2.listar todo los vehiculos regidtrado
        3.imprimir orden de reparacion 
        4.salir          
    '''))
        if menu == 1:
             registrar()
        elif menu == 2:
            print(listartodo())
        elif menu == 3:
            imprimir()
        elif menu == 4:
            break
    except Exception as e:
        input(f'excep de: {str[e]}')
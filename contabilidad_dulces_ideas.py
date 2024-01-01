# entradas de informacion
# pesos y cantidades de productos

obleas = int(input('Cantidad de obleas:\n'))
topin = int(input('Cantidad de toppins en gramos:\n'))
sirope = int(input('Cantidad de sirope en gramos:\n'))
fruta = int(input('Cantidad de fruta en gramos:\n'))
base = int(input('Cantidad de base en gramos:\n'))
lluvia = int(input('Cantidad de lluvia en gramos:\n'))

# se muestra la cantidad de producto por la manana
print(f'''
      Se inicia la manana con:
      {obleas} unidades de obleas.
      {topin} gramos de toppin's.
      {sirope} gramos de sirope.
      {fruta} gramos de fruta.
      {base} gramos de base.
      {lluvia} gramos de lluvia.''')

# saber cuantas obleas de cuantos tipos fueron vendidas

mini_obleas = 0
normales_obleas = 0
fruty_obleas = 0
normales_obleas2 = 0
obleas_2 = 0
topin_2 = 0
base_2 = 0
lluvia_2 = 0
sirope_2 = 0
fruta_2 = 0
decoracion = 0
costo_mini_oblea = 0
costo_normal_oblea = 0
costo_fruty_oblea = 0
costo_normal_oblea2 = 0

while True:
    venta_obleas = str( input('''
    Seleccione que tipo de oblea se vendio
    1 para mini obleas
    2 para normal obleas
    3 para normal obleas 2
    4 para fruty obleas\n'''))
    
    match venta_obleas:
        case '1':
            mini_obleas = mini_obleas+1
            costo_mini_oblea = costo_mini_oblea+3000
            obleas_2 = obleas_2+2
            topin_2 = topin_2+20
            base_2 = base_2+35
            lluvia_2 = lluvia_2+25
            sirope_2 = sirope_2+20
            decoracion = decoracion+5
              
        case '2':
            normales_obleas= normales_obleas+1
            costo_normal_oblea = costo_normal_oblea+3000   
            obleas_2 = obleas_2+2
            topin_2 = topin_2+30
            base_2 = base_2+50
            lluvia_2 = lluvia_2+30
            sirope = sirope+30
            decoracion = decoracion+5
            
        case '3':
            normales_obleas2= normales_obleas2+1
            costo_normal_oblea2 = costo_normal_oblea2+3000   
            obleas_2 = obleas_2+2
            topin_2 = topin_2+15
            fruta_2 = fruta_2+15
            base_2 = base_2+50
            lluvia_2 = lluvia_2+30
            sirope = sirope+30
            decoracion = decoracion+5
            
        case '4':
            fruty_obleas= fruty_obleas+1
            costo_fruty_oblea = costo_fruty_oblea+3000
            obleas_2 = obleas_2+2
            topin_2 = topin_2+30
            base_2 = base_2+50
            fruta_2 = fruta_2+50 
            lluvia_2 = lluvia_2+30
            sirope_2 = sirope_2+30
            decoracion = decoracion+5
    
      
      
    print(f'''
          precionar ESPACIO para mostrar resultados
          y ENTER para seguir sumando''')
    resp=input(' ')
    if resp == ' ':
          break

# procesos de cuentas

obleas_total=obleas-obleas_2
topin_total=topin-(topin_2+decoracion)
base_total=base-base_2
lluvia_total=lluvia-lluvia_2
sirope_total=sirope-sirope_2
fruta_total=fruta-fruta_2
total_costo=costo_mini_oblea+costo_normal_oblea+costo_fruty_oblea+normales_obleas2

# resultados por la tarde   
print(f'''
      total de obleas minis vendidas: {mini_obleas} unidades.
      dinero obtenido por la venta de mini obleas:{costo_mini_oblea}
      
      total de obleas normales vendidas: {normales_obleas} unidades.
      dinero obtenido por la venta de normales obleas: {costo_normal_oblea}
      
      total de obleas normales vendidas: {normales_obleas2} unidades.
      dinero obtenido por la venta de normales obleas: {costo_normal_oblea2}
      
      total de obleas fruty vendidas: {fruty_obleas} unidades.
      dinero obtenido por la venta de fruty obleas: {costo_fruty_oblea}
      
      sumatoria de tosdas las ventas:{total_costo}
      
      
      total de obleas restantes: {obleas_total} unidades.
      total de toppin's restante: {topin_total} gramos.
      total de base restante: {base_total} gramos.
      total de lluvia restante: {lluvia_total} gramos.
      total de sirope restante: {sirope_total} gramos
      total de fruta restante: {fruta_total} gramos''')    
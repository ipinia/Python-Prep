from operator import truediv


mi_var1 = 4
print ( mi_var1)
type (8.5)
nombre = 'José'
complejo = 45 +3j
print(type(complejo))
print (complejo)
pi= 3.1416
mi_var2 = True
mi_var3 = False
print(mi_var2, mi_var3)
suma1= 5+2j
print (complejo + suma1)
print(mi_var1 + complejo)
print (mi_var1 *2)
print( 2**8)
cociente = 27//4
print(cociente)
resto = 27%4
print( resto)
print(4*cociente+resto)
mi_var4 = 'tecno'
mi_var5 = 'new3'
print(mi_var4+ ' ' +mi_var5)
comp1= '2'
comp2= 2
print ( comp1 == comp2 )
#el resultado es 'false', porque una variable es string y otra int
print(int(comp1)==comp2)
#arroja error por el uso de la coma en vez del punto
mi_var6 = 3
mi_var6-=2
print(mi_var6 )
mi_var7 = 1 << 2
print(mi_var7)
#es el resultado de mover lo bits 2 veces hacia la derecha. El sistema binario es un sistema de numeración que solo usa dos dígitos.
#print(2 +'2')
#No está permitido porque los datos son de tipo distinto, y no, el resultado no sería el mismo si los datos fuesen del mismo tipo, porque con int sería una operación, y con string sería una concatenación.
mi_var8 = 'Siete es: '
mi_var9 = 7
print(mi_var8 + str (mi_var9))
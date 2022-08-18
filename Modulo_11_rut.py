primero = ('a')
segundo = ('b')
tercero = ('c')
cuarto = ('d')
quinto = ('e')
sexto = ('f')
septimo = ('g')
octavo = ('h')
print ('escribir rut')
a = int(input('escribe el primer numero '))
b = int(input('escribe el segundo numero '))
c = int(input('escribe el tercer numero '))
d = int(input('escribe el cuarto numero '))
e = int(input('escribe el quinto numero '))
f = int(input('escribe el sexto numero '))
g = int(input('escribe el septimo numero '))
h = int(input('escribe el octavo numero '))
i = h * 2
j = g * 3
k = f * 4
l = e * 5
m = d * 6
n = c * 7
o = b * 2
p = a * 3
q =  i + j + k + l + m + n + o + p
r = q//11
s = q - 11*r
t = 11 - s
if t == 11:
    print (f'el rut es {a}{b}{c}{d}{e}{f}{g}{h}-0')
if t == 10:
    print (f'el rut es {a}{b}{c}{d}{e}{f}{g}{h}-K')
else:
    print (f'el rut es {a}{b}{c}{d}{e}{f}{g}{h}-{t}')

#Si el resultado es 11, el dígito verificador será 0 (cero).
#Si el resultado es 10, el dígito verificador será K.
#En otro caso, el resultado será el propio dígito verificador.
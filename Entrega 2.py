
import csv
from dataclasses import dataclass

norli = []
nors = []
norgas = []
refsol=[]
refliq = []
refgas = []
infli = []
inf3 = []

#lista = [[nor1],[nor2],[nor3],[ref1],[ref2],[ref3],[inf1],[inf2],[inf3]]

@dataclass
class contenedor_G:
    lista = []
    id_producto: str
    nombre_producto:str
    tipo:str
    masa:str
    peso:int
    tamano: str="Grande"
@dataclass
class contenedor_P(contenedor_G):
    tamano: str = "Pequeño"

@dataclass
class Tren(contenedor_G):
    tamano: str = "Grande"

@dataclass
class estanque_P(contenedor_G):
    tamano: str = "Pequeño"

@dataclass
class estanque_G(contenedor_G):
    tamano: str = "Grande"

z = contenedor_P

def read_csv(x):
    with open(x, 'r') as c:
        line = csv.reader(c)
        lista = list(line)
    return(lista)

lista = read_csv("ejemplo_lista.csv")

#print(lista)
Contenedor1=contenedor_G(lista[7][0],lista[7][1],"solida", "refrigerado", lista[7][4])
Contenedor1.lista.append(norli)
#print(Contenedor1)
xd=0
lolo=[]
for y in range(len(lista)):
    if lista[y][3]=='liquido':
        if lista[y][2]=='normal':
          norli.append(lista[y][4])
#print(norli)
#print("")
#print(Contenedor1.lista)
for s in Contenedor1.lista[0]:
     xd+=int(s)
#print(xd)

Tonelaje=int()
Tonelaje=(xd/1000)

ContenedorPequeño2=int()

if Tonelaje>20:
    ContenedorPequeño2=contenedor_P(lista[1][0],lista[1][1],lista[1][2],lista[1][3],lista[1][4])
    RestosSR=int(Tonelaje-20)
print(ContenedorPequeño2)

EstanqueGrande1=int()
if Tonelaje>24:
    EstanqueGrande1=estanque_G(lista[8][0],lista[8][1],lista[8][2],lista[8][3],24)
    Tonelaje=int(Tonelaje-24)
else:
    EstanqueGrande1=estanque_G(lista[8][0],lista[8][1],lista[8][2],lista[8][3],Tonelaje)
print(EstanqueGrande1)
#print(Tonelaje)

EstanqueGrande2=int()
if Tonelaje>24:
    EstanqueGrande2=estanque_G(lista[8][0],lista[8][1],lista[8][2],lista[8][3],24)
    Tonelaje=int(Tonelaje-24)
else:
    EstanqueGrande2=estanque_G(lista[8][0],lista[8][1],lista[8][2],lista[8][3],Tonelaje)
print(EstanqueGrande2)
#print(Tonelaje)

EstanqueGrande3=int()
if Tonelaje>24:
    EstanqueGrande3=estanque_G(lista[8][0],lista[8][1],lista[8][2],lista[8][3],24)
    Tonelaje=int(Tonelaje-24)
else:
    EstanqueGrande3=estanque_G(lista[8][0],lista[8][1],lista[8][2],lista[8][3],Tonelaje)
print(EstanqueGrande3)
#print(Tonelaje)

EstanqueGrande4=int()

if Tonelaje>24:
    EstanqueGrande4=estanque_G(lista[8][0],lista[8][1],lista[8][2],lista[8][3],24)
    Tonelaje=int(Tonelaje-24)
else:
    EstanqueGrande4=estanque_G(lista[8][0],lista[8][1],lista[8][2],lista[8][3],Tonelaje)
print(EstanqueGrande4)
#print(Tonelaje)

EstanquePequeño1=int()
if Tonelaje>12:
    EstanquePequeño1=estanque_P(lista[8][0],lista[8][1],lista[8][2],lista[8][3],12)
    Tonelaje=int(Tonelaje-24)
else:
    EstanquePequeño1=estanque_P(lista[8][0],lista[8][1],lista[8][2],lista[8][3],Tonelaje)
print(EstanquePequeño1)
Tonelaje=0

for y in range(len(lista)):
    if lista[y][3]=='liquido':
        if lista[y][2]=='refrigerado':
          refliq.append(lista[y][4])


#print(refliq

Numero=int(refliq[0])
TonelajeLR=int(Numero/1000)
#print(TonelajeLR)

Contenedor8LR=(contenedor_G)(lista[7][0],lista[7][1],lista[7][2],lista[7][3],TonelajeLR)
print(Contenedor8LR)

for y in range(len(lista)):
    if lista[y][3]=='liquido':
        if lista[y][2]=='inflamable':
          infli.append(lista[y][4])

Numero1=int(infli[0])
#print(Numero1)
TonelajeIL=int(Numero1/1000)

ContenedorPequeño3=(contenedor_P)(lista[4][0],lista[4][1],lista[4][2],lista[4][3],TonelajeIL)
print(ContenedorPequeño3)

for y in range(len(lista)):
    if lista[y][0]=='2':
        if lista[y][3]=="solida":
            if lista[y][2]=='refrigerado':
                nors.append(lista[y][4])

#print(nors)

Numero2=int(nors[0])
TonelajeSR=int(Numero2/1000)

Contenedor9SR=(contenedor_P)(lista[2][0],lista[2][1],lista[2][2],lista[2][3],TonelajeSR)
print(Contenedor9SR)

for y in range(len(lista)):
    if lista[y][0]=='3':
        inf3.append(lista[y][4])

Numero3=int(inf3[0])
TonelajeGI=int(Numero3/1000)

EstanqueGrande5=(estanque_G)
EstanquePequeño2=(estanque_P)
if TonelajeGI>24:
    EstanqueGrande5=(estanque_G)(lista[3][0],lista[3][1],lista[3][2],lista[3][3],24)
    RestosGI=int(TonelajeGI-24)
    EstanquePequeño3=(estanque_P)(lista[3][0],lista[3][1],lista[3][2],lista[3][3],RestosGI)
print(EstanqueGrande5)
print(EstanquePequeño3)

#print(refliq)
Numero4=int(refliq[0])
TonelajeRL=int(Numero4/1000)

EstanqueGrande6=(estanque_G)(lista[5][0],lista[5][1],lista[5][2],lista[5][3],TonelajeRL)
print(EstanqueGrande6)

for y in range(len(lista)):
    if lista[y][0]=='6':
        refsol.append(lista[y][4])

#print(refsol)

Numero5=int(refsol[0])
TonelajeRS=int(Numero5/1000)

Contenedor10SR=(contenedor_G)(lista[6][0],lista[6][1],lista[6][2],lista[6][3],TonelajeRS)
print(Contenedor10SR)

for y in range(len(lista)):
    if lista[y][0]=='9':
        norgas.append(lista[y][4])
#print(norgas)

Numero6=int(norgas[0])
TonelajeNG=int(Numero6/1000)

EstanquePequeño4=(estanque_P)(lista[9][0],lista[9][1],lista[9][2],lista[9][3],TonelajeNG)
print(EstanquePequeño4)
































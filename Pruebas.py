import mysql.connector
import csv
from dataclasses import dataclass

norli = []
norsol = []
norgas = []
refsol=[]
refliq = []
refgas = []
infli = []
infsol = []
infgas = []

#Las clases de contenedores y estanques + un vehiculo
@dataclass
class contenedor_G:
    lista = []
    id_producto: str
    nombre_producto:str
    tipo:str
    masa:str
    peso:int
    tamano: str="Grande"
#@dataclass
#class contenedor_G:
 #   def __init__(self,id_producto,nombre_producto,tipo,masa,peso):
 #       self.lista = []
 #       self.id_producto="id_producto"
 #       self.nombre_producto="nombre_producto"
 #       self.tipo="tipo"
 #       self.masa="masa"
 #       self.peso="peso"
 #       self.tamano="Grande"
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

#Funcion para leer la lista de datos 
def read_csv(x):
    with open(x, 'r') as c:
        line = csv.reader(c)
        lista = list(line)
    return(lista)

lista = read_csv("ejemplo_lista.csv")

class datitos:
    def __init__(self, id_producto, nombre_producto, tipo, masa, peso):
        self.id_producto= id_producto
        self.nombre_producto= nombre_producto
        self.tipo= tipo
        self.masa= masa
        self.peso= peso

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="basesita"
)

mycursor = mydb.cursor()

sql = "DELETE FROM datitosxd1"
mycursor.execute(sql)

for y in range(len(lista)):
    if lista[y][3]=='liquido':
        if lista[y][2]=='normal':
            norli.append(int(lista[y][4]))
            Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], lista[y][4])
            #print(Contenedor)
            if (int(lista[y][4]))>=24000:
                Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], 24000)
                print(Contenedor)
                restos=(int(lista[y][4])-24000)
                sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],24000)
                mycursor.execute(sql,val)
                mydb.commit()
                if restos>=24000:
                    Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], 24000)
                    print(Contenedor)
                    restos=(int(lista[y][4])-48000)
                    sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                    val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],24000)
                    mycursor.execute(sql,val)
                    mydb.commit()
                    if restos>=24000:
                        Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], 24000)
                        print(Contenedor)
                        restos=(int(lista[y][4])-72000)
                        sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                        val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],24000)
                        mycursor.execute(sql,val)
                        mydb.commit()
                        if restos>=24000:
                            Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], 24000)
                            print(Contenedor)
                            restos=(int(lista[y][4])-96000)
                            sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                            val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],24000)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            if restos>=24000:
                                Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], 24000)
                                print(Contenedor)
                                sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                                val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],24000)
                                mycursor.execute(sql,val)
                                mydb.commit()  
                            else:
                                Contenedor=contenedor_P(lista[y][0], lista[y][1],lista[y][2], lista[y][3], restos)
                                print(Contenedor)             
                                sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                                val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],restos)
                                mycursor.execute(sql,val)
                                mydb.commit()   
                        else:
                            Contenedor=contenedor_P(lista[y][0], lista[y][1],lista[y][2], lista[y][3], restos)
                            print(Contenedor)
                            sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                            val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],restos)
                            mycursor.execute(sql,val)
                            mydb.commit()  
                    else:
                                Contenedor=contenedor_P(lista[y][0], lista[y][1],lista[y][2], lista[y][3], restos)
                                print(Contenedor)            
                else:
                    Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], restos)
                    print(Contenedor)
                    sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                    val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],restos)
                    mycursor.execute(sql,val)
                    mydb.commit()    

        elif lista[y][2]=='inflamable':
            infli.append(int(lista[y][4]))
            Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], lista[y][4])
            #print(Contenedor)
            if (int(lista[y][4]))>=24000:
                Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], 24000)
                print(Contenedor)
                sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],24000)
                mycursor.execute(sql,val)
                mydb.commit()  
                restos=(int(lista[y][4])-24000)
                if restos>=24000:
                    Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], 24000)
                    print(Contenedor)
                    restos=(int(lista[y][4])-48000)
                    sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                    val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],24000)
                    mycursor.execute(sql,val)
                    mydb.commit()  
                    if restos>=24000:
                        Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], 24000)
                        print(Contenedor)
                        restos=(int(lista[y][4])-72000)
                        sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                        val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],24000)
                        mycursor.execute(sql,val)
                        mydb.commit()  
                        if restos>=24000:
                            Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], 24000)
                            print(Contenedor)
                            restos=(int(lista[y][4])-96000)
                            sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                            val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],restos)
                            mycursor.execute(sql,val)
                            mydb.commit()  
                            if restos>=24000:
                                Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], 24000)
                                print(Contenedor)
                                sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                                val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],24000)
                                mycursor.execute(sql,val)
                                mydb.commit()  
                            else:
                                Contenedor=contenedor_P(lista[y][0], lista[y][1],lista[y][2], lista[y][3], restos)
                                print(Contenedor)
                                sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                                val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],restos)
                                mycursor.execute(sql,val)
                                mydb.commit()  
                        else:
                            Contenedor=contenedor_P(lista[y][0], lista[y][1],lista[y][2], lista[y][3], restos)
                            print(Contenedor)
                            sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                            val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],restos)
                            mycursor.execute(sql,val)
                            mydb.commit()  
                    else:
                                Contenedor=contenedor_P(lista[y][0], lista[y][1],lista[y][2], lista[y][3], restos)
                                print(Contenedor)
                                sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                                val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],restos)
                                mycursor.execute(sql,val)
                                mydb.commit()              
                else:
                    Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], lista[y][4])
                    print(Contenedor)
                    sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                    val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],lista[y][4])
                    mycursor.execute(sql,val)
                    mydb.commit()  
            else:
                if (int(lista[y][4]))>=12000:
                    Contenedor=contenedor_P(lista[y][0], lista[y][1],lista[y][2], lista[y][3], 12000)
                    restos=(int(lista[y][4])-12000)
                    print(Contenedor)
                    sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                    val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],12000)
                    mycursor.execute(sql,val)
                    mydb.commit()
                    if restos!=0:  
                        Contenedor=contenedor_P(lista[y][0], lista[y][1],lista[y][2], lista[y][3], restos)
                        print(Contenedor)
                        sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                        val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],restos)
                        mycursor.execute(sql,val)
                        mydb.commit()  
                else:
                    Contenedor=contenedor_P(lista[y][0], lista[y][1],lista[y][2], lista[y][3], lista[y][4])
                    print(Contenedor)
                    sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                    val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],lista[y][4])
                    mycursor.execute(sql,val)
                    mydb.commit()  
        elif lista[y][2]=='refrigerado':
            refliq.append(int(lista[y][4]))
            Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], lista[y][4])
            #print(Contenedor)
            if (int(lista[y][4]))>=24000:
                Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], 24000)
                print(Contenedor)
                sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],24000)
                mycursor.execute(sql,val)
                mydb.commit()
                restos=(int(lista[y][4])-24000)
                if restos>=24000:
                    Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], 24000)
                    print(Contenedor)
                    restos=(int(lista[y][4])-48000)
                    sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                    val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],24000)
                    mycursor.execute(sql,val)
                    mydb.commit()
                    if restos>=24000:
                        Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], 24000)
                        print(Contenedor)
                        restos=(int(lista[y][4])-72000)
                        sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                        val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],24000)
                        mycursor.execute(sql,val)
                        mydb.commit()
                        if restos>=24000:
                            Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], 24000)
                            print(Contenedor)
                            restos=(int(lista[y][4])-96000)
                            sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                            val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],24000)
                            mycursor.execute(sql,val)
                            mydb.commit()
                            if restos>=24000:
                                Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], 24000)
                                print(Contenedor)
                                sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                                val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],24000)
                                mycursor.execute(sql,val)
                                mydb.commit()
                            else:
                                Contenedor=contenedor_P(lista[y][0], lista[y][1],lista[y][2], lista[y][3], restos)
                                print(Contenedor)
                                sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                                val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],restos)
                                mycursor.execute(sql,val)
                                mydb.commit()
                        else:
                            Contenedor=contenedor_P(lista[y][0], lista[y][1],lista[y][2], lista[y][3], restos)
                            print(Contenedor)
                            sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                            val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],restos)
                            mycursor.execute(sql,val)
                            mydb.commit()
                    else:
                                Contenedor=contenedor_P(lista[y][0], lista[y][1],lista[y][2], lista[y][3], restos)
                                print(Contenedor)
                                sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                                val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],restos)
                                mycursor.execute(sql,val)
                                mydb.commit()            
                else:
                    Contenedor=contenedor_G(lista[y][0], lista[y][1],lista[y][2], lista[y][3], lista[y][4])
                    print(Contenedor)
                    sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                    val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],lista[y][4])
                    mycursor.execute(sql,val)
                    mydb.commit()
            else:
                if (int(lista[y][4]))>=12000:
                    Contenedor=contenedor_P(lista[y][0], lista[y][1],lista[y][2], lista[y][3], 12000)
                    restos=(int(lista[y][4])-12000)
                    print(Contenedor)
                    sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                    val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],12000)
                    mycursor.execute(sql,val)
                    mydb.commit()
                    Contenedor=contenedor_P(lista[y][0], lista[y][1],lista[y][2], lista[y][3], restos)
                    print(Contenedor)
                    sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                    val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],restos)
                    mycursor.execute(sql,val)
                    mydb.commit()
                else:
                    Contenedor=contenedor_P(lista[y][0], lista[y][1],lista[y][2], lista[y][3], lista[y][4])
                    print(Contenedor)
                    sql = "INSERT INTO datitosxd1 (id_producto, nombre_producto, tipo, masa, peso) VALUES (%s, %s, %s, %s, %s)"
                    val = (lista[y][0],lista[y][1],lista[y][2],lista[y][3],lista[y][4])
                    mycursor.execute(sql,val)
                    mydb.commit()
import csv 

def cargar_ofertas(ruta):
    lista_ofertas = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            lista_ofertas.append(fila)
    return lista_ofertas

ofertas = cargar_ofertas("data/empleos_tech_ia_web.csv")
print(f"Total de ofertas cargadas {len(ofertas)}")

if ofertas:
    print("Ejemplo de primera oferta:", ofertas[0])



contador = {}

for hueco in ofertas:
    texto_stack = hueco["stack_tecnologico"]
    lista_techs = texto_stack.split(",")
    for tecnologia in lista_techs:
        tecno = tecnologia.strip().lower()
        if tecno in contador:
            contador[tecno] = contador[tecno] + 1

        else:
            contador[tecno] = 1

print(contador)

ranking = sorted(contador.items(), key=lambda par: par[1], reverse=True)

print(ranking[0][0], ranking[0][1])
posicion = 1
for par in ranking[:10]:
    
    print(f"{posicion}. {par[0]} - {par[1]} ofertas")
    posicion = posicion + 1

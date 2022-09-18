'''
Crear una biblioteca de juegos y ordenarlos mediente
listas y diccionarios 
'''
biblioteca = [ 
    {
        "categoria":"Deporte",
        "juegos": ["FIFA", "F1", "MotoGP", "NBA"]
    },
    {
        "categoria":"Accion",
        "juegos": ["GTA", "Call of duty", "Rust", "Valorant"]  
    },
    {
        "categoria":"Aventura",
        "juegos":["Zelda", "Elden Ring", "Its Take Two"]
    }
]

#print(biblioteca)
for categoria in biblioteca:
    print(f"---------{categoria['categoria']}---------")
    for juegos in categoria["juegos"]:
        posicion = categoria["juegos"].index(juegos) + 1
        print(f"{posicion}. {juegos}")

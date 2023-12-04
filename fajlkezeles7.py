def hetedik():
    lista = []
    beFajl = open("fileok/dal.txt", "r", encoding="utf-8")
    for sor in beFajl:
        lista.append(sor.strip())
    beFajl.close()

    # lista visszafele kiírása
    kiFajl = open("fileok/hetedik.txt", "w", encoding="utf-8")
    for index in range(len(lista)-1, -1, -1):
        print(lista[index])
        print(lista[index], file=kiFajl)
    kiFajl.close()

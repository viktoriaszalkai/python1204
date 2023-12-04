def negyedik():
    # beolvasás
    lista = []
    beFajl = open("fileok/dal.txt", "r", encoding="utf-8")
    for sor in beFajl:
        lista.append(sor.strip())
    beFajl.close()

    # lista kiírása
    kiFajl = open("fileok/negyedik.txt", "w", encoding="utf-8")
    for index in range(0, len(lista), 1):
        # a sorokat eldarabolom a szóközök mentén
        daraboltSor = lista[index].split(" ")
        # a lista 0. elemét írom a fájlba
        print(daraboltSor[0], file=kiFajl)
        # kiFajl.erite(lista[index])
    kiFajl.close()

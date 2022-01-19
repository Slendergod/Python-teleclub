archivo = open("Teleclub","w")
#Input
lista1 = input("Inserte lista 1: ")
lista2 = input("Inserte lista 2: ")

#Lista 1
archivo.write("#""EXTINF:0, Teleclub (Opcion 1) " + '\n')
archivo.write(lista1 + '\n')

#Lista 2
archivo.write("#""EXTINF:0, Teleclub (Opcion 2) " + '\n')
archivo.write(lista2 + '\n')

archivo.close()
#Abrir navegador 
import webbrowser

urls = ['https://teleclub.xyz/listas']

aux = 0
for x in urls:
    webbrowser.register('windows-default', None, webbrowser.BackgroundBrowser(
        "C://Program Files (x86)//Microsoft//Edge//Application//msedge"))

    webbrowser.get('windows-default').open(urls[aux])
    aux += 1
#Abrir archivo TELE
archivo = open("Teleclub","w")

archivo.write("#""EXTM3U" + '\n')
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

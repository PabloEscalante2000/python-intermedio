import math
import random
import os


dic_vocales = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u'}
dic_vocales_inv = {'a':'á', 'e':'é', 'i':'í', 'o':'ó', 'u':'ú'}

juego_terminado = """
            ░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░
            ██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗
            ██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
            ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
            ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
            ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝"""

continuar = """
            █▀▀ █▀█ █▄░█ ▀█▀ █ █▄░█ █░█ ▄▀█ █▀█   ▀█   █▄█   ░░▄▀   █▄░█
            █▄▄ █▄█ █░▀█ ░█░ █ █░▀█ █▄█ █▀█ █▀▄   ░▄   ░█░   ▄▀░░   █░▀█
                                    
                                            """

hangman = """ 
        ██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
        ██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
        ███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
        ██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
        ██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
        ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝ """

ganaste = """
        ░██████╗░░█████╗░███╗░░██╗░█████╗░░██████╗████████╗███████╗██╗██╗██╗
        ██╔════╝░██╔══██╗████╗░██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██║██║██║
        ██║░░██╗░███████║██╔██╗██║███████║╚█████╗░░░░██║░░░█████╗░░██║██║██║
        ██║░░╚██╗██╔══██║██║╚████║██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░╚═╝╚═╝╚═╝
        ╚██████╔╝██║░░██║██║░╚███║██║░░██║██████╔╝░░░██║░░░███████╗██╗██╗██╗
        ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝╚═╝╚═╝"""

text_dificultad = """       sᴇʟᴇᴄᴄɪᴏɴᴀʀ ɴɪᴠᴇʟ ( 1 / 2 / 3)
        """


def dificultad():
    print(hangman)
    dif = input(text_dificultad)
    itera = True

    while (itera):
        try: 
            if dif.isnumeric():
                if int(dif) == 1:
                    itera = False
                    return 0 
                elif int(dif) == 2:
                    itera = False
                    return 2
                elif int(dif) == 3:
                    itera = False
                    return 4
                else:
                    os.system("cls")
                    print(hangman)
                    dif = input(text_dificultad)
            else:
                raise ValueError("Tienes que ingresar un numero (1 , 2 , 3)")
        except ValueError as ve:
            os.system("cls")
            print(ve)
            print(hangman)
            dif = input(text_dificultad)

    
    

def dar_nombre():
    names = []
    with open('./archivos/data.txt', 'r', encoding='utf-8') as f:
        names = [line.replace('\n',"") for line in f]
    name = names[random.randrange(0,len(names))]
    name = name.lower()
    
    return name


def juego(name,faltas):

    lista = []

    nombre = ""


    while(True):

        nombre = ""

        if faltas == 5:
            os.system("cls")
            print(juego_terminado)
            print("             el nombre era: " + name)
            break

        if len(lista) != 0:

            for l in name:
                if l in lista:
                    nombre = nombre + l.upper() + " "
                elif l in dic_vocales.keys():
                    if dic_vocales.get(l) in lista:
                        nombre = nombre + l.upper() + " "
                    else:
                        nombre = nombre + "_ "

                elif l in dic_vocales_inv.keys():
                    if dic_vocales_inv.get(l) in lista:
                        nombre = nombre + l.upper() + " "
                    else:
                        nombre = nombre + "_ "
                else:
                    nombre = nombre + "_ "
        else:
            for l in name:
                nombre = nombre + "_ "   

        if not "_" in nombre:
            print(ganaste)
            print("             el nombre es: " + nombre)
            break

        print(nombre)

        letra = input(""" 
            █▀▄ █ █▀▄▀█ █▀▀   █░█ █▄░█ ▄▀█   █░░ █▀▀ ▀█▀ █▀█ ▄▀█
            █▄▀ █ █░▀░█ ██▄   █▄█ █░▀█ █▀█   █▄▄ ██▄ ░█░ █▀▄ █▀█
                                    
                                    """)
        if letra.isalpha() == False:
            os.system("cls")
            print(hangman)
            print(nombre) 
            print(""" 
            █▀ █▀█ █░░ █▀█   █▀█ █░█ █▀▀ █▀▄ █▀▀ █▀   █ █▄░█ █▀▀ █▀█ █▀▀ █▀ ▄▀█ █▀█   █░░ █▀▀ ▀█▀ █▀█ ▄▀█ █▀
            ▄█ █▄█ █▄▄ █▄█   █▀▀ █▄█ ██▄ █▄▀ ██▄ ▄█   █ █░▀█ █▄█ █▀▄ ██▄ ▄█ █▀█ █▀▄   █▄▄ ██▄ ░█░ █▀▄ █▀█ ▄█ """)

            
        elif len(letra) != 1:
            os.system("cls")
            print(hangman)
            print(nombre) 
            print(""" 
            █▀ █▀█ █░░ █▀█   █░█ █▄░█ ▄▀█   █░░ █▀▀ ▀█▀ █▀█ ▄▀█
            ▄█ █▄█ █▄▄ █▄█   █▄█ █░▀█ █▀█   █▄▄ ██▄ ░█░ █▀▄ █▀█ """)

        elif letra in lista or letra == " ":
            os.system("cls")
            print(hangman)
            print(nombre) 
            print(""" 
            █░░ █▀▀ ▀█▀ █▀█ ▄▀█   █░█ █▄░█ █ █▀▀ ▄▀█
            █▄▄ ██▄ ░█░ █▀▄ █▀█   █▄█ █░▀█ █ █▄▄ █▀█""")
        
        else:
            letra = letra.lower()

            lista.append(letra)

            if letra in name:
                pass
            elif letra in dic_vocales.keys():
                if dic_vocales.get(letra) in name:
                    pass
            elif letra in dic_vocales_inv.keys():
                if dic_vocales_inv.get(letra) in name:
                    pass
            else:
                faltas = faltas + 1  
                print("te quedan: " + str(5-faltas) + " más")
                

        


def run():
    dif = dificultad()
    os.system("cls")
    name = dar_nombre()
    juego(name,dif)

if __name__ == '__main__':
    run()
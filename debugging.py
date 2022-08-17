def numeros(n):
    lista = []
    for i in range(1,n+1):
        lista.append(i)
    return lista


def run():
    try:
        mi_num = int(input("dime el numero: "))
        if mi_num < 1:
            raise ValueError("el número tiene que ser un entero positivo tontito")
        lista = list(filter(lambda n: mi_num % n == 0,numeros(mi_num)))
        print(lista)
    except ValueError as ve:
        print(ve)
        run()


if __name__ == '__main__':
    run()
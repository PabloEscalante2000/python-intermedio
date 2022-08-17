def numeros(n):
    lista = []
    for i in range(1,n+1):
        lista.append(i)
    return lista


def run():
    mi_num = input("Dame un número tontito: ")
    assert mi_num.isnumeric(), "Tienes que ingresar un número"
    lista = list(filter(lambda n: mi_num % n == 0,numeros(int(mi_num))))
    print(lista)


if __name__ == '__main__':
    run()
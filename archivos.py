from tkinter.font import names


def read():
    my_nums = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            my_nums.append(int(line))

    print(my_nums)

def write():
    names = ['a','b','c','d','e','•','☻']
    with open('./archivos/names.txt', 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')

def run():
    write()

if __name__ == '__main__':
    run()
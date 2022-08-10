import math

def run():
    my_dic={i:math.sqrt(i) for i in range(1,101) if math.sqrt(i).is_integer()}
    print(my_dic)

if __name__ == "__main__":
    run()
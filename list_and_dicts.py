def run():
    my_list = [1,"hello", True, 4.5]
    my_dict = {"firstname": "Pablo", "lastname": "Escalante"}

    super_list = [
        {"firstname": "a", "lastname": "az"},
        {"firstname": "b", "lastname": "bz"},
        {"firstname": "c", "lastname": "cz"},
        {"firstname": "d", "lastname": "dz"}
    ]

    super_dic = {
        "lista1" : [1,2,3,4,5],
        "lista2" : ["a","b","c","d","e"]
    }

    for key,data in super_dic.items():
        print(key)
        print(data)

    for i in super_list:
        print(i)

if __name__ == '__main__':
    run()
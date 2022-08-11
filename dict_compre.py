import cmath

def run():
    # my_dict = {}

    # for i in range(1, 101):
    #     if i % 3 !=0:
    #         my_dict[i] = i**2

    # print(my_dict)
    
    
    

    my_dict = {i: cmath.sqrt(i) for i in range(1, 101)}
    print(my_dict)


if __name__ == "__main__":
    run()
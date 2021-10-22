from MyList import CalcList
from MetaCust import CustomClass

if __name__ == '__main__':
    my_l = CalcList([4, 10, -4])
    l2 = [7, 1, -8, 10]
    l3 = l2 + my_l
    print(l3)
    l4 = l2 + l3
    print(l4)
    print(isinstance(my_l, list))
    my_list = CalcList([5, 10, 4, -8, 2.0])
    dop_list = [12, 0, -7, 1, -6, 7.0]
    print(my_list - dop_list)
    inst = CustomClass()
    print(inst.custom_x)
    print(inst.custom_line())

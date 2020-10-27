from DLL import DLL
from Node import Node


dll = DLL()

flag = True
print("Þú getur sett inn hluti eins og 'append 5', 'push 10', 'find 0' inn í inputið til að gera aðgerðirnar")
while flag:
    inp = input("Hvað viltu gera: [append,push,delete,print,find,stop]: ")
    values = inp.split(' ')
    val = values[0]
    if len(values) > 1:
        val2 = values[1]
    else:
        val2 = None

    if val == 'append':
        if val2 == None:
            print('Þú þarft að gefa value')
        else:
            dll.append(val2)

    elif val == 'push':
        if val2 == None:
            print('Þú þarft að gefa value')
        else:
            dll.push(val2)

    elif val == 'delete':
        if val2 == None:
            print('Þú þarft að gefa value')
        else:
            dll.delete(val2)

    elif val == 'print':
        dll.printList()
        print()

    elif val == 'find':
        if val2 == None:
            print('Þú þarft að gefa value')
        else:
            if dll.find(val2):
                print('Fann það')
            else:
                print('Fann það ekki')

    elif val == 'stop':
        flag = False
    else:
        print('Þetta er ekki gilt val')
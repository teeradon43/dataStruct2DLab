"""
    Use Singly LinkedLists to play Scramble (Card)
"""
from SinglyLinkedLists import LinkedLists

def lift(num, L):
    L1 = LinkedLists()
    num = num / 10
    t = L.head
    # print(t.next)
    count = 0
    while count != num:
        L1.append(L.removeHead())
        t = t.next
        count += 1
    # print(L1)
    L2 = LinkedLists()
    while count != 10:
        L2.append(L.removeHead())
        t = t.next
        count += 1
    # print(L2)
    return L1,L2
def BottomUp(percent,L):
    #สับล่างขึ้นบน
    L1, L2 = lift(percent,L)
    while not L2.isEmpty():
        L.append(L2.removeHead())
    while not L1.isEmpty():
        L.append(L1.removeHead())
    return L
def deBottomUp(percent,L):
    #สลับกลับ
    pass
def riffleShuffle():
    #กรีดไพ่
    pass
def deRiffle():
    #กรีดกลับ
    pass

if __name__ == '__main__':
    L = LinkedLists()
    bu_lists = []
    rs_lists = []
    sub1 = LinkedLists()
    sub2 = LinkedLists()
    for i in range(1,11):
        L.append(str(i))
    inp = input('Enter Input : ').split(',')
    #BU = BottomUp , DB = deBottomUp, RS = riffleShuffle, DR = deRiffle
    for txt in inp:
        command = txt[:2]
        if command == 'BU':
            bu_lists.append(txt[3:])
            L = BottomUp(txt[3:],L)
        elif command == 'DB':
            if len(bu_lists) > 0:
                L = deBottomUp(txt[3:],L)
                bu_lists.pop(0)
            else:
                print("haven't bottom up yet")
        elif command == 'RS':
            rs_lists.append(txt[3:])
            L = riffleShuffle(txt[3:],L)
        elif command == 'DR':
            if len(rs_lists) > 0:
                L = deRiffle(txt[3:],L)
                rs_lists.pop(0)
            else:
                print("haven't riffle yet")
        else:
            print('Error Command',command,' not define')
    print(L)
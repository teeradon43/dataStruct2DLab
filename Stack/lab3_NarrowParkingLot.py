from lab1_stack import Stack

if __name__ == '__main__':

    s = Stack() # main
    d = Stack() # dummy
    # init available parking space
    space = 4

    inp = input('Enter input : ').split(',') # A = Arrive, D = Depart
    for i in inp:
        lot = space - s.size()
        if i[0] == 'A': # Arrive
            if lot > 0:
                s.push(i[1])
                print('car',i[1],'arrive\t',end='')
            else:
                print('car',i[1],'cannot arrive\t',end='')
        elif i[0] == 'D': # Depart
            if not s.isEmpty():
                while not s.isEmpty():
                    if s.peek() == i[1]:
                        print('Depart car',s.pop(),'\t',end='')
                        break
                    else:
                        d.push(s.pop())
                while not d.isEmpty():
                    s.push(d.pop())
                if lot == space - s.size():
                    print('Cannot Depart : No car',i[1],'in Parking Lot.')
            else:
                print('Cannot Depart : Parking Lot is Empty.')
        else:
            print('Unknown format.')
        
        print('space left :',space - s.size(),'\t',s.items)
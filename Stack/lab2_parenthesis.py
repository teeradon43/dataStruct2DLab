from lab1_stack import Stack

def match(op,close):
    if op == '(':
        return close == ')'
    elif op == '{':
        return close == '}'
    elif op == '[':
        return close == ']'
    else:
        print('error open paren undefined')
        return -1
        
s = Stack()
txt = input('Enter input : ')
error = False
for i in txt:
    if i in '({[':
        s.push(i)
    if i in ')}]':
        if s.isEmpty():
            error = True    # lack of open paren
        else:
            op = s.pop()
            if not match(op,i):
                error = True    # open & close paren not match

if error:
    print('MISMATCH')
else:
    if not s.isEmpty():
        print('MISMATCH open pared exceed')
    else:
        print('MATCH')
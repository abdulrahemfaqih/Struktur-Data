def stack():
    s = []
    return s


def push(s, data):
    s.append(data)


def pop(s):
    return s.pop()


def peek(s):
    return s[len(s) - 1]


def isEmpty(s):
    return s == []


def size(s):
    return len(s)


st = stack()
push(st, 1)
push(st, 2)
push(st, 3)
print(st)
print(peek(st))


""""
s = stack kosong
while (seluruh string belum dibaca) {
    baca simbol 
}



"""

def stack(): 
    s = []
    return s
def push(s, data):
    s.append(data)
def pop(s):
    data = s.pop()
    return data
def peek(s):
    return s[len(s) - 1]
def isEmpty(s):
    return s == []
def size(s):
    return len(s)

def evaluatePost(postStr):
    operandStack = stack()
    operator = "+-/*"
    for i in postStr:
        if i not in operator:
            push(operandStack, i)
        else:
            operand2 = pop(operandStack)
            operand1 = pop(operandStack)
            if i == "+":
                result = float(operand1) + float(operand2)
            elif i == "-":
                result = float(operand1) - float(operand2)
            elif i == '/':
                result = float(operand1) / float(operand2)
            else:
                result = float(operand1) * float(operand2)
            push(operandStack,result)
    return (pop(operandStack))

print(evaluatePost('45-6*'))

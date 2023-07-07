
def stack():
    s = []
    return s
def push(s, data):
    s.append(data)
def pop(s):
    return s.pop()
def size(s):
    return len(s)
def peek(s):
    return s[len(s)-1]
def isEmpety(s):
    return s == []

openOperand = "({["
closeOperand = ")}]"

def is_operator(c):
    return c == "+" or c == "-" or c == "*" or c == "/" 

def precedence(c):
    if c == "*" or c == "/":
        return 2
    elif c == "+" or c == "-":
        return 1
    else:
        return 0


def paranthesesCheck(strMath):
    operandStack = stack()
    lenMath = size(strMath)
    i = 0
    Matched = True
    while i < (lenMath):
        if strMath[i] in openOperand:
            push(operandStack, strMath[i])
        elif strMath[i] in closeOperand:
            if not (isEmpety(operandStack)):
                top = pop(operandStack)
                if openOperand.index(top) == closeOperand.index(strMath[i]):
                    Matched = Matched and True
                else:
                    Matched = Matched and False
                    print("Kurung Buka dan Kurung Tutup tidak Cocok")
            else:
                Matched = Matched and False
                print("Jumlah Kurung Tutup lebih banyak")
        i = i + 1
    if not (isEmpety(operandStack)):
        Matched = False
        print("Jumlah Kurung Buka Lebih banyak")
    return Matched


def infixToPostfix(strMath):
    operandStack = stack()
    postfix = ""
    for i in strMath:
        if i in openOperand:
            push(operandStack, i)
        elif i in closeOperand:
            while peek(operandStack) not in openOperand:
                postfix += pop(operandStack)
            pop(operandStack)
        elif is_operator(i):
            while (
                size(operandStack)!= 0
                and peek(operandStack) not in openOperand
                and precedence(i) <= precedence(peek(operandStack))
            ):
                postfix += pop(operandStack)
            push(operandStack, i)
        else:
            postfix += i
    while size(operandStack) != 0:
        postfix += pop(operandStack)
    return postfix

    

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

def main():
    repeat = 4
    for i in range(repeat):
        expression = input('Masukkan string operasi aritmatika =  ')
        parentheses_check = paranthesesCheck(expression)
        if parentheses_check == True:
            postfix_expression = infixToPostfix(expression)
            result = evaluatePost(postfix_expression)
            print(f'infix: {expression} ; postfix: {postfix_expression} = {result} ')
        else:
            pass
main()
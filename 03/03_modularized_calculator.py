#! /usr/bin/python3

def read_number(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        decimal = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * decimal
            decimal /= 10
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index

def read_plus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1

def read_minus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def read_times(line,index):
    token = {'type': 'TIMES'}
    return token, index + 1

def read_divide(line,index):
    token = {'type': 'DIVIDE'}
    return token, index + 1

def read_paren(line,index):
    token = {'type': 'PAREN'}
    return token, index + 1

def read_abs(line,index):
    token = {'type': 'ABS'}
    return token, index + 4

def read_int(line,index):
    token = {'type': 'INT'}
    return token, index + 4

def read_round(line,index):
    token = {'type': 'ROUND'}
    return token, index + 6

def read_close(line,index):
    token = {'type': 'CLOSE'}
    return token, index + 1

def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = read_number(line, index)
        elif line[index] == '+':
            (token, index) = read_plus(line, index)
        elif line[index] == '-':
            (token, index) = read_minus(line, index)
        elif line[index] == '*':
            (token, index) = read_times(line, index)
        elif line[index] == '/':
            (token, index) = read_divide(line, index)
        elif line[index] == '(':
            (token, index) = read_paren(line, index)
        elif line[index] == ')':
            (token, index) = read_close(line, index)
        elif line[index:index+4] == 'abs(':
            (token, index) = read_abs(line, index)
        elif line[index:index+4] == 'int(':
            (token, index) = read_int(line, index)
        elif line[index:index+6] == 'round(':
            (token, index) = read_round(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens

def calc_abs(num):#絶対値
    if num<0:
        return -num
    else:
        return num

def calc_int(num):#小数点切り捨て
    if num >= 0:
        return num // 1
    else:
        return (num // 1) + (num % 1 != 0)

def calc_round(num):#小数点四捨五入
    if num >= 0:
        return calc_int(num+0.5)
    else:
        return calc_int(num-0.5)

def evaluate(tokens):
    #print(tokens)
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token


    #優先順位1:各種()の計算...一重括弧までしか対応していない
    index = 1
    while index < len(tokens):#()内の計算

        if tokens[index]['type'] == 'PAREN'or tokens[index]['type'] == 'ABS' or tokens[index]['type'] == 'INT' or tokens[index]['type'] == 'ROUND':
            open_type = tokens[index]['type']
            count_open = 1
            count_close = 0
            tokens.pop(index)

            new_tokens = []#()内を新しいトークンリストに移す
            while count_open>count_close:
                if tokens[index]['type'] == 'PAREN'or tokens[index]['type'] == 'ABS' or tokens[index]['type'] == 'INT' or tokens[index]['type'] == 'ROUND':
                    count_open += 1
                elif tokens[index]['type'] == 'CLOSE':
                    count_close += 1
                popped_item = tokens.pop(index)
                new_tokens.append(popped_item)
                #print("open-close",count_open,count_close)
            new_tokens.pop(-1)
            if open_type == 'PAREN':
                tokens.insert(index,{'type':'NUMBER', 'number': evaluate(new_tokens)})
            elif open_type == 'ABS':
                tokens.insert(index,{'type':'NUMBER', 'number': calc_abs(evaluate(new_tokens))})
            elif open_type == 'INT':
                tokens.insert(index,{'type':'NUMBER', 'number': calc_int(evaluate(new_tokens))})                
            elif open_type == 'ROUND':
                tokens.insert(index,{'type':'NUMBER', 'number': calc_round(evaluate(new_tokens))})

        index += 1

    #優先順位2:掛け算，割り算の計算
    index = 1
    while index < len(tokens)-1:
        if tokens[index]['type'] == 'TIMES':
            if tokens[index - 1]['type'] == 'NUMBER' and tokens[index + 1]['type'] == 'NUMBER':
                times = tokens[index-1]['number']*tokens[index+1]['number']
                tokens.insert(index-1,{'type':'NUMBER', 'number': times})
                for i in range(3):
                    tokens.pop(index)
            else:#演算子の前後が数字ではない時はエラーメッセージ
                print('Invalid syntax')
                exit(1)                
        elif tokens[index]['type'] == 'DIVIDE':
            if tokens[index - 1]['type'] == 'NUMBER' and tokens[index + 1]['type'] == 'NUMBER':
                times = tokens[index-1]['number']/tokens[index+1]['number']
                tokens.insert(index-1,{'type':'NUMBER', 'number': times})
                for i in range(3):
                    tokens.pop(index)
            else:
                print('Invalid syntax')
                exit(1)   

        index += 1

    #優先順位3:足し算，引き算の計算
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print('Invalid syntax')
                exit(1)
        index += 1

    return answer

def test(line):
    tokens = tokenize(line)
    actual_answer = evaluate(tokens)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))

# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")
    test("1+2")
    test("1.0+2.1-3")
    test("1.0+2.1-3+(4+5)")
    test("(1.0+2.1)-3+(4+5)")
    test("3*2")
    test("10-3*2")
    test("4/2")
    test("4/2-1")
    test("4/(2-1)")
    test("4/((2-1))")
    test("(3.0+4*(2-1))/5")
    test("12+abs(int(round(-1.55)+abs(int(-2.3+4))))")
    test("12+abs(-10)")
    print("==== Test finished! ====\n")

run_test()

while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)

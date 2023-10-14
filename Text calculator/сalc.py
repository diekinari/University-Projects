import os


# девять плюс скобка открывается пять плюс один плюс четыре умножить на скобка открывается два плюс три скобка закрывается скобка закрывается
# двадцать пять разделить на шесть минус четыре
# скобка открывается скобка открывается девяносто восемь разделить на шесть скобка закрывается плюс четыре умножить на скобка открывается семьдесят два минус восемнадцать скобка закрывается скобка закрывается умножить на три минус пятьдесят семь и семьдесят четыре сотых

def clean():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def getAndCheckTheCommand(db):
    symbols = ["плюс", "минус", "умножить", "разделить", "скобка", "открывается", "закрывается"]
    fraction_db = [['десятых', "десятая", "сотых", "сотая", "тысячных", "тысячная", ], {'одна': 1, "две": 2}]
    isAllowed = False
    # Flag for making a separated fraction input
    fractionMode = False
    transformedCommand = []
    # helping element for fraction
    previousElement = 0
    # for multi brackets input
    bracketsCount = 0
    while True:
        command = input('Введите математическую задачу: ').lower().split()
        for i in range(len(command)):
            # print(command[i])
            # all checkpoints after a dot
            if fractionMode:
                # if a number
                if command[i] in db or command[i] in fraction_db[1]:
                    # transformedElement = 0

                    # convert special ending into number via dicts
                    if command[i] in fraction_db[1]:
                        transformedElement = fraction_db[1][command[i]]
                    else:
                        transformedElement = db[command[i]]

                    # adding fist number after dot (in string command)
                    if command[i - 1] == 'и':
                        if len(str(transformedElement)) == 3:
                            transformedCommand[-1] += (transformedElement / 1000)
                            previousElement = transformedElement

                        # ... и двадцать (пять) тысячных || ... и двадцать (пять) сотых || ... и двадцать (пять) десятых
                        elif len(str(transformedElement)) == 2:
                            previousElement = transformedElement
                            if command[i + 1] in \
                                    [fraction_db[0][0], fraction_db[0][1], fraction_db[0][2], fraction_db[0][3]] \
                                    or command[i + 2] \
                                    in [fraction_db[0][0], fraction_db[0][1], fraction_db[0][2], fraction_db[0][3]]:
                                transformedCommand[-1] += (transformedElement / 100)
                            elif command[i + 1] in [fraction_db[0][4], fraction_db[0][5]] \
                                    or command[i + 2] in [fraction_db[0][4], fraction_db[0][5]]:
                                transformedCommand[-1] = round(transformedCommand[-1] + (transformedElement / 1000), 4)

                        else:
                            previousElement = transformedElement
                            if command[i + 1] in [fraction_db[0][0], fraction_db[0][1]]:
                                transformedCommand[-1] += (transformedElement / 10)
                            elif command[i + 1] in [fraction_db[0][2], fraction_db[0][3]]:
                                transformedCommand[-1] += (transformedElement / 100)
                            elif command[i + 1] in [fraction_db[0][4], fraction_db[0][5]]:
                                transformedCommand[-1] += (transformedElement / 1000)

                    # adding second number after dot (in string command)
                    elif command[i - 2] == 'и':
                        # 0.20 + 0.05 || 0.020 + 0.005
                        if len(str(transformedElement)) == 1 and previousElement >= 20 and previousElement % 10 == 0:
                            previousElement = transformedElement
                            if command[i + 1] in [fraction_db[0][2], fraction_db[0][3]]:
                                transformedCommand[-1] = round(transformedCommand[-1] + (transformedElement / 100), 4)
                            elif command[i + 1] in [fraction_db[0][4], fraction_db[0][5]]:
                                transformedCommand[-1] += (transformedElement / 1000)

                        # 0.200 + 0.50 (+ 0.1)
                        elif len(str(transformedElement)) == 2 and previousElement >= 100 \
                                and previousElement % 100 // 10 == 0:
                            transformedCommand[-1] = round(transformedCommand[-1] + (transformedElement / 1000), 4)
                            previousElement = transformedElement
                        else:
                            transformedCommand = []
                            fractionMode = False
                            isAllowed = False
                            clean()
                            print('Неккоректный ввод!')
                            break

                    # adding third number after dot (in string command)
                    elif command[i - 3] == 'и':
                        if len(str(transformedElement)) == 1 and 20 <= previousElement < 100:
                            transformedCommand[-1] = round(transformedCommand[-1] + (transformedElement / 1000), 4)
                            previousElement = 0
                        else:
                            transformedCommand = []
                            fractionMode = False
                            isAllowed = False
                            clean()
                            print('Неккоректный ввод!')
                            break

                    else:
                        transformedCommand = []
                        fractionMode = False
                        isAllowed = False
                        clean()
                        print('Неккоректный ввод!')
                        break

                # if an ending of fraction
                elif command[i] in fraction_db[0] and command[i - 1] != 'и':
                    # find count of digits after dot
                    decimalPlaces = int(len(str(transformedCommand[-1]).split('.')[1]))

                    if (decimalPlaces == 1 and (
                            command[i] in [fraction_db[0][0], fraction_db[0][1]])) or (
                            decimalPlaces == 2 and (
                            command[i] in [fraction_db[0][2], fraction_db[0][3], fraction_db[0][4],
                                           fraction_db[0][5]])) or (
                            decimalPlaces == 3 and (
                            command[i] in [fraction_db[0][4], fraction_db[0][5]])):

                        if (str(transformedCommand[-1])[-1] == '1'
                            and command[i] in [fraction_db[0][1], fraction_db[0][3], fraction_db[0][5]]) or (
                                str(transformedCommand[-1])[-1] != '1'
                                and command[i] in [fraction_db[0][0], fraction_db[0][2], fraction_db[0][4]]):
                            fractionMode = False
                            continue
                        else:
                            transformedCommand = []
                            fractionMode = False
                            isAllowed = False
                            clean()
                            print('Неккоректный ввод!')
                            break
                    else:
                        transformedCommand = []
                        fractionMode = False
                        isAllowed = False
                        clean()
                        print('Неккоректный ввод!')
                        break
                else:
                    transformedCommand = []
                    fractionMode = False
                    isAllowed = False
                    clean()
                    print('Неккоректный ввод!')
                    break

            # whole numbers and operators check
            elif command[i] in db or command[i] in symbols:
                # brackets check
                if command[i] in symbols[4: 7]:

                    # 'скобка'
                    if command[i] == symbols[4] and 0 <= i < len(command) - 1:
                        pass
                    # "("
                    elif command[i] == symbols[5] and 0 < i < len(command) - 5 and command[i - 1] == symbols[4]:
                        transformedCommand.append('(')
                        bracketsCount += 1
                    # ")"
                    elif command[i] == symbols[6] and 5 < i and bracketsCount >= 1 \
                            and command[i - 1] == symbols[4] \
                            and (type(transformedCommand[-1]) in [int, float] or transformedCommand[-1] == ')'):
                        transformedCommand.append(')')
                        bracketsCount -= 1
                    else:
                        transformedCommand = []
                        bracketsCount = 0
                        isAllowed = False
                        clean()
                        print('Неккоректный ввод!')
                        break

                    # and (command[i - 2] in db or command[i - 2] in fraction_db[0] or command[i - 2] in symbols):

                # check for correct operator input: 'digit + symbol'
                elif command[i] in symbols and i > 0 and \
                        (command[i - 1] in db or command[i - 1] in fraction_db[0] or command[i - 1] in symbols[6]):

                    # if mult or div check that operator is not at the end
                    if (command[i] == symbols[2] or command[i] == symbols[3]) and len(command) - 2 > i:
                        transformedCommand.append(command[i])

                    # if + or - check that operator is not at the end
                    elif (command[i] == symbols[0] or command[i] == symbols[1]) and len(command) - 1 > i:
                        transformedCommand.append(command[i])

                    else:
                        transformedCommand = []
                        bracketsCount = 0
                        isAllowed = False
                        clean()
                        print('Неккоректный ввод!')
                        break

                # check for correct numbers input
                elif command[i] in db:
                    # check correct subsequence number - 25, 12...
                    if i > 0 and type(transformedCommand[-1]) == int \
                            and transformedCommand[-1] >= 20 and 10 > db[command[i]] \
                            and transformedCommand[-1] % 10 == 0:
                        transformedCommand[-1] += db[command[i]]
                    # check correct 'symbol + number' input
                    elif i > 0 and type(transformedCommand[-1]) == str:
                        transformedCommand.append(db[command[i]])
                        isAllowed = True
                    # just add first symb (if a number!)
                    elif i == 0:
                        transformedCommand.append(db[command[i]])
                    else:
                        transformedCommand = []
                        bracketsCount = 0
                        isAllowed = False
                        clean()
                        print('Неккоректный ввод!')
                        break

            # check if it's right div or mult addition
            elif (len(command) - 1) > i > 1 and command[i] == 'на' and (
                    command[i - 1] == "умножить" or command[i - 1] == "разделить") and (
                    command[i + 1] in db or command[i + 1] == symbols[4]) and not (
                    command[i + 1] == 'ноль' and command[i - 1] == "разделить"):
                pass

            # check if it's right entrance to the fraction mode
            elif command[i] == 'и' and len(command) - 2 > i > 0 and command[i - 1] in db:
                fractionMode = True

            else:
                transformedCommand = []
                bracketsCount = 0
                isAllowed = False
                clean()
                print("Неккоректный ввод!")
                break
        # check for too short input
        if len(transformedCommand) <= 2 or bracketsCount != 0:
            transformedCommand = []
            bracketsCount = 0
            isAllowed = False
            clean()
            print('Неккоректный ввод!')
            continue
        elif isAllowed:
            return transformedCommand
        else:
            continue


def getPostfixTypedCommand(command):
    priorities = {'умножить': 2, "разделить": 2, "плюс": 1, "минус": 1, '(': 0}
    postfixCommand = []
    stack = []
    # convert into postfix type
    for el in command:
        if el == ')':
            for op in stack[::-1]:
                if op != '(':
                    postfixCommand.append(op)
                    stack.pop()
                else:
                    stack.remove(op)
                    break
        elif type(el) in [int, float]:
            postfixCommand.append(el)
        elif el == '(':
            stack.append(el)
        else:
            if len(stack) == 0:
                stack.append(el)
            else:
                if priorities[el] > priorities[stack[-1]]:
                    stack.append(el)
                else:
                    for op in stack[::-1]:
                        if priorities[op] >= priorities[el]:
                            postfixCommand.append(op)
                            stack.pop()
                        else:
                            break
                    stack.append(el)
    postfixCommand += [stack[i] for i in range(len(stack) - 1, -1, -1)]
    return postfixCommand


def calculate(postfixCommand):
    operator = {'плюс': lambda x, y: x + y,
                'минус': lambda x, y: x - y,
                'умножить': lambda x, y: x * y,
                'разделить': lambda x, y: x / y}
    # calculate the command
    resultStack = []
    for element in postfixCommand:
        if type(element) in [int, float]:
            resultStack.append(element)
        else:
            resultStack.append(operator[element](resultStack[-2], resultStack[-1]))
            resultStack.pop(-2)
            resultStack.pop(-2)

    # delete extra dot in fake-integer numbers & round float numbers (12.0 -> 12 | 12.333333 -> 12.333)
    if round(resultStack[0], 3) == round(resultStack[0]):
        answer = round(resultStack[0])
    else:
        answer = round(resultStack[0], 3)
    return answer


def getTextedAnswer(answer, db):
    def transformIntoList(number):
        ones = number % 10
        tens = (number // 10) % 10 * 10
        hundreds = number // 100 * 100

        if tens == 10:
            return [hundreds, tens + ones]
        else:
            return [hundreds, tens, ones]

    def translateIntoText(number):
        separatedDigits = transformIntoList(number)
        textedAnswer = ''
        for el in separatedDigits:
            if el != 0:
                textedAnswer += " " + swappedDb[el]
        return textedAnswer.strip()

    swappedDb = {v: k for k, v in db.items()}
    textedAnswer = ''
    if str(answer)[0] == '-':
        textedAnswer += 'минус'
        answer = abs(answer)

    if type(answer) == int:
        textedAnswer += translateIntoText(answer)
        return textedAnswer

    else:
        intPart, realPart = map(int, str(answer).split('.'))
        textedIntPart = translateIntoText(intPart)
        textedRealPart = translateIntoText(realPart)
        isLastDigEqualsOne = (realPart % 10 == 1)
        if len(str(realPart)) == 3:
            if isLastDigEqualsOne:
                finalWord = 'тысячная'
            else:
                finalWord = 'тысячных'
        elif len(str(realPart)) == 2:
            if isLastDigEqualsOne:
                finalWord = 'сотая'
            else:
                finalWord = 'сотых'
        elif len(str(realPart)) == 1:
            if isLastDigEqualsOne:
                finalWord = 'десятая'
            else:
                finalWord = 'десятых'
        return textedAnswer + textedIntPart + ' и ' + textedRealPart + ' ' + finalWord


def main():
    db = {'ноль': 0, 'один': 1, "два": 2, "три": 3, "четыре": 4, "пять": 5, "шесть": 6, "семь": 7,
          "восемь": 8, "девять": 9, "десять": 10, "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13,
          "четырнадцать": 14, "пятнадцать": 15, "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18,
          "девятнадцать": 19, "двадцать": 20, "тридцать": 30, "сорок": 40, "пятьдесят": 50, "шестьдесят": 60,
          "семьдесят": 70, "восемьдесят": 80, "девяносто": 90, "сто": 100,
          "двести": 200, "триста": 300, "четыреста": 400, "пятьсот": 500, "шестьсот": 600, "семьсот": 700,
          "восемьсот": 800, "девятьсот": 900}
    command = getAndCheckTheCommand(db)
    postfixCommand = getPostfixTypedCommand(command)
    answer = calculate(postfixCommand)
    while abs(answer) >= 1000:
        clean()
        print('Получилось запредельное число - модуль больше тысячи. Попробуйте пример попроще')
        command = getAndCheckTheCommand(db)
        postfixCommand = getPostfixTypedCommand(command)
        answer = calculate(postfixCommand)
    textedAnswer = getTextedAnswer(answer, db)
    print(textedAnswer)


main()

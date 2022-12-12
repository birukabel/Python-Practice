# This is a sample Python script.
from ProgrammingFunctions import ProgrammingFunctions


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(r'c:\tes\'t')

    # indexing in python

    word = 'Python'
    print(word[0])
    print(word[len(word)-1])
    print(word[-2])
    print(word[-0])
    # slice
    print(word[0:2])
    print(word[2:5])
    print(word[:2])
    print(word[4:])
    print(word[-2:])
    print(word[42:])
    print(word[:])
    print(word[:0])

    for i in word:
        print(i)
        print(word.index(i))

    nums = [1, 2, 3, 4, 5]
    for y in nums:
        print(y)
        print(nums.index(y))

    squares = [1, 4, 9, 16, 25]
    squares + [36, 49, 64, 81, 100]

    print(squares[:])
    print(squares[:] + [36, 49, 64, 81, 100])

    print(4**3)

    list = [1]
    list.append(2)
    print(list[:])
    list[:] = []

    print(list)
    x = [squares, [36, 49, 64, 81, 100]]
    print(x)
    print(x[0])
    print(x[0][1])
    for i in x:
        for r in i:
            print(r)

    #Fibonachi Series
    first = 0
    second = 1
    counter = 8
    steps = 2
    fib = []
    while steps < counter:
        fib.append(first)
        fib.append(second)
        steps = steps + 1
        first = first + second
        second = first + second
    print(fib)
    xs = [8, 23, 45]
    for idx, xr in enumerate(xs):
        print(idx, xr)

    for a in range(len(xs)):
        print(a, xs[a])
    for f in range(5):
        print(f)
    _te = 2
    print(_te)

    stack = ['Biruk', 'Abel', 'Taffese', 'Tessema']
    print(stack.pop())
    stack.append('Python')
    print(stack[:])

    from collections import deque
    queue = deque(['Biruk', 'Abel', 'Taffese', 'Tessema'])
    queue.append('Python')
    print(queue)
    print(queue.popleft())
    print(queue)
    tup = ('this', 'is', 'a tuple', 1)
    for ind, item in enumerate(tup):
        print(f'index{ind} item {item}')

    se = set('thisis a a set')
    for ind, item in enumerate(se):
        print(f'index={ind} item={item}')

    dic = {1: 'Apple', 2: 'Orange', 3: 'Papaya', 4: 'Banana'}
    for ke, val in dic.items():
        print(f'Key={ke} Value={val}')

    #pf = ProgrammingFunctions()
    #pf.romantoint('II')

    li = ["Hello", "Biruk", "Abel", "Hello"]
    print([item for ind, item in enumerate(li) if item == "Hello"])
    import numpy as np
    indexes = np.where(np.array(li) == "Hello")
    print(indexes)

    from ProgrammingFunctions import ProgrammingFunctions as pr
    ins = pr()
    ins.charfrequency("accdb")

    ins.printduplicateitemsinList(['a', 'b', 'c', 'a', 'b'])

    duplicates = ins.findDuplicates(['a', 'b', 'c', 'a', 'b'])
    print(duplicates)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


'''def romantoint(self, s: str) -> int:
    dicSingels = {'I': 1, 'V': 5, 'X': 10, 'L': '50', 'C': 100, 'D': 500, 'M': 1000}
    dicDoubles = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    returnedValue = counter = 0

    while counter < len(s):
        if counter == 0:
            returnedValue = returnedValue + dicSingels[s[counter]]
            counter = counter + 1
        else:
            if s[counter:counter + 2] in dicDoubles:
                returnedValue = returnedValue + dicDoubles[s[counter:counter + 2]]
                counter = counter + 2
            else:
                returnedValue = returnedValue + dicSingels[s[counter]]
                counter = counter + 1
    return returnedValue'''

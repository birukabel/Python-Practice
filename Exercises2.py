import collections
from  functools import reduce

class Exercises2:
    #reverse each word of a string
    def reverse_each_word_string(self, s: str) -> str:
        s_splited = s.split(' ')
        s_returned = ''
        for i in s_splited:
            le = len(i)
            le = le - 1
            while le >= 0:
                s_returned = s_returned + i[le]
                le = le-1
            s_returned = s_returned + ' '
        s_returned[len(s_returned) - 1].replace(' ', '')
        return s_returned

    def reverse_each_word_string_slicing(self, s: str) -> str:
        s_splited = s.split(' ')
        s_returned = ''
        for i in s_splited:
            #General syntax of  string  slicing is string[start:end:jump]
            s_returned = s_returned + i[::-1]
            s_returned = s_returned + ' '
        s_returned[len(s_returned)-1].replace(' ', '')
        return s_returned

    #remove all items in list larger than a value
    def remove_items_from_list(self, li: [], treashold: int) -> []:
        for i in li:
            if i > treashold:
                li.remove(i)
        return li

    #reverse dictionary mapping {'A': 65, 'B': 66, 'C': 67, 'D': 68} to {65: 'A', 66: 'B', 67: 'C', 68: 'D'}
    def reverse_dictionary_mapping(self,dic: {}) -> {}:
        returnedValue = {}
        for idx,item in dic.items():
            returnedValue[item] = idx
        return  returnedValue

    #remove duplicate items in list
    def remove_duplicate_items_fromlist(self, li: []) -> []:
        lis = [item for item in li if li.count(item) == 1]
        return  lis

    #keep duplicate items in list
    def keep_duplicates_inlist(self, li: []) -> []:
        #list comprehension
        lis = [x for x in li if li.count(x) > 1]
        return lis

    #remove deuplicates using collections
    def remove_duplicate_using_collec(self, li: []) -> []:
        lis = []
        for item,con in collections.Counter(li).items():
            if con == 1:
                lis.append(item)
        return  lis

    #filter dicionary items contained in list
    def filter_dic_bylist(self, dic: {}, li: []) -> {}:
        #dcitionary comprehenion
        dicreturn = {key: dic[key] for key in li}
        return  dicreturn

    def doubleNumber(self, n: int)-> int:
        return n*2

    #function to double each element of a list using lambda function
    def mapDoubleUsingLambda(self,li: list) -> []:
        return map(lambda n: n*2, li)

    # function to double each element of a list using user deifined function
    def mapDoubleUsingFunction(self,li: list) -> []:
        return map(Exercises2.doubleNumber, li)

    def isEven(self, n: int) -> bool:
        return  n % 2 == 0

    # function to filer and return Even numbers from list using filter function
    def filterEvensFromListUsingLambda(self, li: list) -> []:
        return  filter(lambda n: n%2==0,li)

    #function to filer and return Even numbers from list using user defined function
    def filterEvensFromListUsingUserDefinedFunctions(self,li:list) -> []:
        return  filter(Exercises2.isEven,li)

    def sumOfElements(self,ls: list)->int:
        sum = 0
        for item in ls:
            sum += item[1]
        return  sum

    #function to get sum of elements in a tuple using lambda
    def reduceUsingLambdaToGetSum(self, tup: tuple)->int:
        return  reduce(lambda a, b: a[1]+b[1],tup)

    # function to get sum of elements in a tuple using user defined function
    def reduceUsingFunctionToGetSum(self,tup: tuple)->int:
        return  reduce(Exercises2.sumOfElements,tup)

    def addition(self,n: int)->int:
        return n + n





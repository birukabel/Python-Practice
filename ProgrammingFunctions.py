class ProgrammingFunctions:
    def romantoint(self, s: str) -> int:
        dicSingels = {'I': 1, 'V': 5, 'X': 10, 'L': '50', 'C': 100, 'D': 500, 'M': 1000}
        dicDoubles = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        '''print(dicSingels[s[0]])
        for ind, item in dicSingels.items():
            print(item)
            print(item+1)
        return 1'''

        returnedValue = counter = 0

        while counter < len(s):
            if counter == 0:
                # print(dicSingels[s[counter]])
                returnedValue = returnedValue + dicSingels[s[counter:counter + 1]]
                counter = counter + 1
            else:
                if s[counter:counter + 2] in dicDoubles:
                    returnedValue = returnedValue + dicDoubles[s[counter:counter + 2]]
                    counter = counter + 2
                else:
                    returnedValue = returnedValue + dicSingels[s[counter]]
                    counter = counter + 1
        return returnedValue

    #counter char frequency in a string
    def charfrequency(self, s: str) -> None:
        diccharCount={}
        for i in s:
            if i not in diccharCount:
                diccharCount[i] = 1
            else:
                val = diccharCount[i]
                val = val + 1
                diccharCount[i] = val
        print(diccharCount)

    def printduplicateitemsinList(self, ls: []) -> None:
        lsVisited = []
        for index, item in enumerate(ls):
            if item in lsVisited:
                continue
            else:
                for index2, item2 in enumerate(ls):
                    if item2 == item and index2 != index:
                        print(item2)
                        if item2 not in lsVisited:
                            lsVisited.append(item2)

    #find duplicates in list
    def findDuplicates(self, nums: [int]) -> [int]:
        # lsVisited = []
        duplicates = []
        for item in nums:
            if item not in duplicates:
                if nums.count(item) > 1:
                    duplicates.append(item)
        return duplicates

    def productorsum(self, num1: int, num2: int) -> int:
        if num1 * num2 <= 1000:
            return num1 * num2
        else:
            return num1 + num2

    #calculate square of user input
    def calculate_square_number(self) -> None:
        x = input("please enter an integer number")
        print(f'Square of the number = {pow(int(x),2)}')

    #sum of current and previous number from 1 to 10
    def print_current_previous_sum(self) -> None:
        for i in range(1, 11):
            previous = i - 1
            print(f'Current number:{i} previous number {previous} thier sum {previous + i}')

    # print characters with even index in a tring using enumerate
    def print_char_even_index(self, s: str) -> None:
        for idx, item in enumerate(s):
            if idx % 2 == 0:
                print(f'character at even index:{item}')

    #print characters with even index in a tring using slice
    def print_char_even_index_slicing(self, s: str) -> None:
        print('Print chars at even index using slicing')
        for item in s[0::2]:
            print(f'character at even index:{item}')

    #validate user input
    def check_user_input(self, s: str) -> None:
        print(type(s))
        try:
            val = float(s)
            print('input is float')
        except ValueError:
            print('Value is not float')
            try:
                val = int(s)
                print('value is int')
            except ValueError:
                print('Value is neither float or int')


    #Remove first n characters from a string
    def remove_chars(self,s: str, length: int) -> str:
        if length < len(s):
            return  s.replace(s[0:length],'')
        return ''





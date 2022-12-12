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

    def findDuplicates(self, nums: [int]) -> [int]:
        # lsVisited = []
        duplicates = []
        for item in nums:
            if item not in duplicates:
                if nums.count(item) > 1:
                    duplicates.append(item)
        return duplicates

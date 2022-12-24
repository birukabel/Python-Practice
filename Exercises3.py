import random
from statistics import mean
from functools import reduce
import  operator

import numpy


class Exercises3:

    def generateRandom(self,li: []) -> str:
        return random.choice(li)

    def sortByThirdWordAndSecondCharcter(self, li: []) -> []:
        #phrases = ['when in rome', 'what goes around comes around', 'all is fair in love and war']
        li.sort(key=lambda x: x.split()[2][1],reverse=True)
        return  li

    def getTopFiveRunnersUsingSort(self, li: []) -> []:
        li.sort(key=lambda x:getattr(x,'duration'))
        return  li[:5]

    def getTopFiveRunnersUsingSorted(self,li: []) -> []:
        li2 = sorted(li,key=lambda x:getattr(x,'duration'))
        return  li2[:5]

    def findAverageMeanOfList(self,li: []) -> int:
        return  round(mean(li),3)

    def findAverageUsingSumNLen(self,li: []) -> int:
        return round(sum(li)/len(li),4)

    def findAverageUSingReduceNLambda(self,li: []) -> int:
        return  reduce(lambda a,b:a+b,li)/len(li)

    def findAverageUsingOperatorAdd(self,li: []) -> int:
        return reduce(operator.add,li)/len(li)

    def findAverageUsingNumpy(self,li: []) -> int:
        return round(numpy.average(li),3)

    def convertStringToLower(self,s: str) -> str:
        return  s.lower()

    def convertStringToUpper(self, s: str) -> str:
        return s.upper()

    def captializeAString(self, s:str) -> str:
        return  s.capitalize()

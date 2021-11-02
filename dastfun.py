#!/use/bin/python3
import math
import numpy as np


class Hisoblash:
    def __init__(self,*age,**kwargs):
        self.age=age     #age bu yerda list Xn qiymatlari turadi
        self.kwargs=kwargs
        self.n=0
        for i in age:
            self.kwargs[self.n]=i
            self.n=self.n+1
    def algo1(self):
        """argumentlarni o'rta arfmetigini qaytaradi 1-formula"""
        sumt=0
        ast=0
        for i in self.kwargs.values():
            sumt=sumt+i
        ast=sumt/(self.n+1)
        return ast

    def algo2(self):
        """Delta Ardgumentni qaytaradi 2-formula"""
        arr=list()
        d=self.algo1()
        for i in self.kwargs.values():
            arr.append(d-i)
        return arr        #list qiymat qaytariyabdi

    def kvad_algao3(self):
        kvat=list()
        for i in self.algo2():
            kvat.append(math.pow(i,2))
        return kvat

    def algo3(self):
        """3-formula argument qiyamtlarining kvadratlari yig'indisi"""
        sumE=0
        for i in self.algo2():
            sumE=sumE+i*i
        return sumE       # sonli qiymat qaytaradi

    def algo4(self):
        """4-formula bo'yincha son qaytaradi"""
        sigma=math.sqrt(self.algo3()/self.n)
        return sigma

    def algo5(self):
        """5-formula son qaytaradi"""
        sigmaN=self.algo4()/math.sqrt(self.n+1)
        return sigmaN

    def algo6(self):
        """6-formula asosida x1 va x2 larni topib olib uzatish"""
        # x=list()
        # # x=self.algo2().copy()
        # for u in self.algo2():
        #     x.append(u)
        x1=list()
        x2=list()
        for i in range(20):
            if i <= 9:
                x1.append(self.algo2()[i]-2.1*self.algo5())
            else:
                x2.append(self.algo2()[i] + 2.1 * self.algo5())
        for i in x2:
            x1.append(i)
        return x1

    def algo7(self):
        """7-formulaga asosan ro'yxat qaytaradi"""
        y=list()
        for a in self.algo2():
            y.append(  (1/(self.algo4()*math.sqrt(2*math.pi)))*math.exp(-(math.pow(a,2)/(2*math.pow(self.algo4(),2)))))
        return y
    def wow(self):
        gotto={}
        ali1 = int(self.algo1() * 100) / 100
        ali3 = int(self.algo3() * 100) / 100
        ali4 = int(self.algo4() * 100) / 100
        ali5 = int(self.algo5() * 100) / 100
        for i in range(20):
            ali2=int(self.algo2()[i]*100)/100
            kvat_nat=int(self.kvad_algao3()[i]*100)/100
            ali6=int(self.algo6()[i]*100)/100
            ali7=int(self.algo7()[i]*100)/100
            gotto[i]=f" {ali1}     {ali2}      {kvat_nat}        {ali3}        {ali4}        {ali5}      {ali6}     {ali7}".format(ali1,ali2,kvat_nat,ali3,ali4,ali5,ali6,ali7)
        return gotto

# s=Hisoblash
# for i in range(20):
#     s=i
#
# s=Hisoblash(1,2,3,3,3,4,3,2,4,3,2,4,3,2,4,3,8,7,9,3)
# # #s=1,2,3,3,3,4,3,2,4,3,2,4,3,2,4,3,8,7,9,3
# # # g,u=s.algo6()
# # print(s.algo1())  #int 1
# # print(type(s.algo2())) #list 1
# # print(type(s.algo3())) #int 1
# # print(type(s.algo4())) #int 1
# # print(s.algo6()) #int 1
# # # print(type(g)) #tuple 2
# # print(type(s.algo7())) #list 1
# print(s.wow())
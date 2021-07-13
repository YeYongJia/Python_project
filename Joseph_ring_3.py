import csv
import xlrd     
import pandas as pd
from zipfile import ZipFile

class Person:
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id
    def print_all(self):
        print('Name:',self.name,'Age:',self.age,'Id:',self.id)
    def print_id(self):
        print(self.id)

class QueueRule():
    def __init__(self,name_list,age_list,id_list,num = 0):
        minList = min(len(name_list),len(age_list),len(id_list))
        people_list = []
        if (num == 0) |(num > minList):
            num = minList
        
        for i in range(num):
            people_list.append(Person(name_list[i],age_list[i],id_list[i]))
                   
        self.list = people_list[0:num]
        self.len = num
    
    def joseph_ring(self,step = 2,start_pos = 0):
        assert (start_pos < self.len) & (start_pos >=0) ,'开始id不符合规定'
        assert step > 1, '输入的step不符合标准'

        copy_list = self.list[:]
        self.outputList = []
        relative_position = 0
        id = start_pos

        while len(copy_list) > 1:
            if id>len(copy_list)-1:
                id = 0
            if relative_position == step-1:
                self.outputList.append(copy_list[id])
                del copy_list[id]
                relative_position = -1            
                id -= 1
            id +=1
            relative_position +=1
        self.outputList.append(copy_list[0])

        return self.outputList
class Reader():
    def __init__(self,filePath):
        self.file = filePath
class Excel_reader(Reader):
    def readExcel(self):
        excelFile = pd.read_excel(self.file)
        name_list = list(excelFile['name'])
        age_list = list(excelFile['age'])
        id_list = list(excelFile['id'])
    

        self.list = QueueRule(name_list,age_list,id_list)
        return self.list
class Csv_reader(Reader):
    def readCsv(self):
        csvFile = pd.read_csv(self.file)
        name_list = list(csvFile['name'])
        age_list = list(csvFile['age'])
        id_list = list(csvFile['id'])

        self.list = QueueRule(name_list,age_list,id_list)
        return self.list      
class Zip_reader(Reader):
    def readZip(self):

        zipFile = ZipFile(self.file,'r')
        f = zipFile.open(zipFile.namelist()[0])
        excelFile = pd.read_excel(f)

        name_list = list(excelFile['name'])
        age_list = list(excelFile['age'])
        id_list = list(excelFile['id'])

        self.list = QueueRule(name_list,age_list,id_list)
        return self.list        
if __name__ == "__main__":

#    name_list = ['Aiwell','Bob','Coco','Durant','Eimmy','Frech','Gill','Haword','Iinsa','Jasd','Kxcd','Lasd','Mc','Nac','Nsdd']# 一共15个
#    age_list = [23,24,23,24,26,27,28,59,23,12,34,13,45,23,24]
#    id_list = list(range(15))

#    num,step,start_pos = eval(input('请输入人数n,计数单位step,开始计数的位置：'))# eval ：将 str 型转化为 int 型
#    df = pd.read_excel(r'people_information.xlsx')
#    print(df)
#    name = list(df['name'])
    filePath1 = 'people_information1.xlsx'
    filePath2 = 'people_information2.csv'
    filePath3 = 'people_information3.zip'

    excelFile = Excel_reader(filePath1)
    csvFile = Csv_reader(filePath2)
    zipFile = Zip_reader(filePath3)

    
    excelToList = excelFile.readExcel()
    csvToList = csvFile.readCsv()
    zipTolist = zipFile.readZip()

#    print(name[1])
#    a = QueueRule(name_list,age_list,id_list,num)
    
    for i in  excelToList.joseph_ring(2,3):
        i.print_all()
    for i in  csvToList.joseph_ring(2,3):
        i.print_all()
    for i in  zipTolist.joseph_ring(2,3):
        i.print_all()
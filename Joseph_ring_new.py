class Person:
    def __init__(self,name,age,id,flag =1):
        self.name = name
        self.age = age
        self.id = id
    def print_all(self):
        print('Name:',self.name,'Age:',self.age,'Id:',self.id)
    def print_id(self):
        print(self.id)
    def print_suv(self):
        print('id:',self.id,'is survive.','Name:',self.name,'Age:',self.age)

def joseph_ring(people_list,num,step=2,start_pos = 0):
    assert num < len(people_list),'输入人数num大于列表中的总人数'
    assert (start_pos < num) & (start_pos >=0) ,'开始id不符合规定'
    assert step > 1, '输入的step不符合标准'
    p_list = people_list[0:num]
    output_list = []
    relative_position = 0
    id = start_pos
    while len(p_list) > 1:
        if id>len(p_list)-1:
            id = 0
        if relative_position == step-1:
            output_list.append(p_list[id])
            del p_list[id]
            relative_position = -1            
            id -= 1
        id +=1
        relative_position +=1
    output_list.append(p_list[0])
    return output_list



if __name__ == "__main__":

    name_list = ['Aiwell','Bob','Coco','Durant','Eimmy','Frech','Gill','Haword','Iinsa','Jasd','Kxcd','Lasd','Mc','Nac','Nsdd']# 一共15个
    age_list = [23,24,23,24,26,27,28,59,23,12,34,13,45,23,24]
    id_list = list(range(15))

#生成一个list，每个元素是一个Person实例
    people_list = []
    for i in range(15):
        people_list.append(Person(name_list[i],age_list[i],id_list[i]))

    num,step,start_pos = eval(input('请输入人数n,计数单位step,开始计数的位置：'))# eval ：将 str 型转化为 int 型
    pop_list = joseph_ring(people_list,num,step,start_pos)
    for i in pop_list:
        i.print_all()

from Acmer import Acmer

date=input("输入起始时间 For example:2016-11-01 将爬2016-11-01之后AC的所有题目:\n")

acmers=[]#保存所有集训队员的dict
acmersfile=open("acmers.txt","r")#读取本地保存集训队员的文件
acmerinfo=acmersfile.readline()#队员信息 格式 name OJname OJID OJname OJID ......

while acmerinfo!='':
    acmerinfo=acmerinfo.split()#以空格为分界 分隔这一行为一个List
    name=acmerinfo[0]
    acmers.append(Acmer(name))
    curAcmer=acmers[-1]#当前处理的ACMer
    #读取所有Ta所在的所有OJ和对应的ID
    for i in range(1,len(acmerinfo),2):
        OJ=acmerinfo[i]
        ID=acmerinfo[i+1]
        curAcmer.addID(OJ,ID)
    acmerinfo=acmersfile.readline()

for person in acmers:
    person.updateAcProblems(date)
    person.updateScore()

acmers.sort(key=lambda x:x.score,reverse=True)

rank=1
for person in acmers:
    print('Rank',rank,person,end=' ')
    print()
    rank+=1

while True:
    isSave = input("Save as txt? (Y/n)\n")
    if isSave.upper() == 'Y':
        path = 'outPutFile/'+date + '.txt'
        print("save as:"+path)
        file = open(path, 'w')
        rank = 1
        for person in acmers:
            file.write('rank:'+str(rank)+' '+str(person)+'\n')
            rank+=1
        file.close()
        break
    elif isSave.upper() == 'N':
        break
    else:
        pass

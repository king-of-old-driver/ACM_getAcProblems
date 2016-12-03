from HDU import HDU
from POJ import POJ
from NYOJ import NYOJ
class Acmer:
    def __init__(self,name):
        self.name=name
        self.score=0
        self.ID={}
        self.AcProblems={}
    def addID(self,OJ,ID):
        self.ID[OJ]=ID
    def updateScore(self):
        self.score=0
        for i in self.AcProblems.keys():
            self.score+=self.AcProblems[i]
        return self.score
    def updateAcProblems(self,date='1970-01-01'):
        for OJ in self.ID.keys():
            command=OJ+'(self.ID[OJ],date).getAcProblems(self.AcProblems)'
            eval(command)

    def __repr__(self):
        ans=self.name+' 题数: '+str(len(self.AcProblems))+' 积分:'+str(round(self.score, 2))
        for prob in self.AcProblems.keys():
            ans+='\n'+'\t'+prob+':'+str(round(self.AcProblems[prob], 2))
        return ans
from GetWeb import GetWeb
class OJ:
    def __init__(self,ID,date='1970-01-01'):
        self.ID=str(ID)
        self.date=date

    def getAcProblems(self,problemsDict):
        getWeber = GetWeb(self.acProblemsFirstPageUrl())
        while self.dataFiltering(self.date, getWeber.getData(), problemsDict):  # 过滤html源码
            tmpurl = self.getNextPageUrl(getWeber.getData()).decode('utf-8')
            getWeber = GetWeb(tmpurl)

    def getNumblersAfterStr(self,data, p,start=0):  # 获得data与模式串p相同的子串后的数字
        psize = len(p)
        for i in range(start, len(data)):
            if data[i:i + psize] == p:
                ans = 0
                j = i + psize
                tmp = data[j:j + 1].decode('utf-8')  # 编码成str型
                while str.isdigit(tmp):
                    ans = ans * 10 + int(tmp)
                    j += 1
                    tmp = data[j:j + 1].decode('utf-8')
                return ans

    def getLevel(self,problemID):
        pass

    def getNextPageUrl(self,nowPageData):
        pass

    def dataFiltering(self,date,data,dict):#处理date之后的题目 data为html源码 dict为acmer的ac题目字典
        pass

    def acProblemsFirstPageUrl(self):
        pass
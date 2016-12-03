from OJ import OJ
from GetWeb import GetWeb

class NYOJ(OJ):
    def getAcProblems(self,problemsDict):
        url= self.acProblemsFirstPageUrl()
        #print(url)
        getWeber = GetWeb(url)
        while self.dataFiltering(self.date, getWeber.getData(), problemsDict):  # 过滤html源码
            url = self.getNextPageUrl(url)
            getWeber = GetWeb(url)

    def getNextPageUrl(self,url):
        #http://acm.nyist.net/JudgeOnline/status.php?do=search&result=Accepted&userid=13450765437&page=1
        start=len(url)
        while str.isdigit(url[start-1:start]):
            start-=1
        pageNum=int(url[start:])
        pageNum+=1
        newUrl=url[:start+1]+str(pageNum)
        return newUrl

    def getLevel(self,problemID):  # level=提交人数 / ac人数
        #http://acm.nyist.net/JudgeOnline/problem.php?pid=118
        url = 'http://acm.nyist.net/JudgeOnline/problem.php?pid='
        url = url + problemID
        getWeber = GetWeb(url)
        data = getWeber.getData()

        # <td><b>Total Submissions:</b> 17095</td>
        # <td><b>Accepted:</b> 4905</td></tr>

        headOfLevel=b'<span class="editable highlight">'

        return self.getNumblersAfterStr(data, headOfLevel)

    def __getAcDate(self,data,start):
        #http://acm.nyist.net/JudgeOnline/code.php?runid=1760610
        head=b'http://acm.nyist.net/JudgeOnline/'
        end=start
        while data[end:end+1]!=b'"':
            end+=1
        url = head + data[start:end]
        url=url.decode('utf-8')
        runTimeData = GetWeb(url).getData()
        headOfDate = b'<span class="editable highlight" id="problem[time_limit]">'
        dateExample=b'2016-10-26'
        for i in range(len(runTimeData)):
            if runTimeData[i:i+len(headOfDate)]==headOfDate:
                i=i+len(headOfDate)
                return runTimeData[i:i+len(dateExample)]

    def dataFiltering(self,date, data, dict):
        maxItemNumber = 15
        encodeDate = date.encode('utf-8')
        headOfProbID = b'problem.php?pid='
        headOfDate = b'method="post" action="'
        countItem = 0
        for i in range(len(data)):
            if data[i:i+len(headOfDate)]==headOfDate:
                i = i + len(headOfDate)
                acDate = self.__getAcDate(data,i)#get acDate
                if acDate<encodeDate:
                    return False
                j=i
                countItem += 1
                while headOfProbID != data[j:j + len(headOfProbID)]:
                    j+=1
                problemID = str(self.getNumblersAfterStr(data, headOfProbID,j))#get problem ID
                i = j + len(headOfProbID)

                probIDStr = 'NYOJ' + problemID
                if probIDStr not in dict.keys():
                     dict[probIDStr] = self.getLevel(problemID)  # 计算难度
            if countItem == maxItemNumber:
                return True
        return False

    def acProblemsFirstPageUrl(self):
        #http://acm.nyist.net/JudgeOnline/status.php?do=search&result=Accepted&userid=13450765437&page=1
        return 'http://acm.nyist.net/JudgeOnline/status.php?do=search&result=Accepted&userid=' + self.ID + '&page=1'
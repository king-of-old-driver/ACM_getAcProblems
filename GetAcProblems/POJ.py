from OJ import OJ
from GetWeb import GetWeb

class POJ(OJ):
    def getNextPageUrl(self,nowPageData):
        # [<a href=status?user_id=13450765437&result=0&top=15713805><font color=blue>Next Page
        pEnd = b'>Next Page</font>'
        pStart=b'<a href='
        head = b'http://poj.org/'  # 注意 POJ的模式p后不带'/' 此处补上

        for i in range(0, len(nowPageData)):
            if pEnd == nowPageData[i:i + len(pEnd)]:
                j=i
                while nowPageData[j:j+2]!=b'><':
                    j-=1
                nextPageUrlEndIndex=j
                while nowPageData[j:j+len(pStart)]!=pStart:
                    j-=1
                nextPageUrlStartIndex = j + len(pStart)
                return head + nowPageData[nextPageUrlStartIndex:nextPageUrlEndIndex]

    def getLevel(self,problemID):  # level=ac人数*10 / 提交人数 取整
        url = 'http://poj.org/problem?id='
        url = url + problemID
        getWeber = GetWeb(url)
        data = getWeber.getData()

        # <td><b>Total Submissions:</b> 17095</td>
        # <td><b>Accepted:</b> 4905</td></tr>

        submitP = b'<td><b>Total Submissions:</b> '
        acSubmitP = b'<td><b>Accepted:</b> '

        return self.getNumblersAfterStr(data, submitP) / self.getNumblersAfterStr(data, acSubmitP)

    def dataFiltering(self,date, data, dict):
        # <a href=problem?id=3164
        """
        <tr align=center><td>16260353</td><td><a href=userstatus?user_id=13450765437>13450765437</a></td><td><a href=problem?id=3164>3164</a></td><td><font color=blue>Accepted</font></td><td>804K</td><td>94MS</td><td>G++</td><td>3063B</td><td>2016-11-03 22:47:42</td></tr>
        """
        maxItemNumber = 20
        dateExample = b'2016-09-22'  # 日期样例
        encodeDate = date.encode('utf-8')
        headOfProbID = b'<a href=problem?id='
        countItem = 0
        for i in range(len(data)):
            if headOfProbID == data[i:i + len(headOfProbID)]:
                countItem += 1
                problemID = data[i + len(headOfProbID):i + len(headOfProbID) + 4].decode('utf-8')
                j = i
                while not (data[j + 4] == data[j + 4 + 3] and b'-' == data[j + 4:j + 5]):
                    j += 1
                acDate = data[j:j + len(dateExample)]

                if acDate >= encodeDate:
                    probIDStr = 'POJ' + problemID
                    if probIDStr not in dict.keys():
                        dict[probIDStr] = self.getLevel(problemID)  # 计算难度
                else:
                    return False
            if countItem == maxItemNumber:
                return True

    def acProblemsFirstPageUrl(self):
        return 'http://poj.org/status?result=0&user_id=' + self.ID
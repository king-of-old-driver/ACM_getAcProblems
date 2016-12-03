from OJ import OJ
from GetWeb import GetWeb
class HDU(OJ):
    def dataFiltering(self,date, data, dict):
        # <td>2016-11-05 16:29:18</td><td><font color=red>Accepted</font></td><td><a href="/showproblem.php?pid=2874">2874</a></td><td>2012MS</td><td>25492K</td><td>2859B</td><td>G++</td><td class=fixedsize><a href="/userstatus.php?user=13450765437">GDPU_lrc</a></td></tr><tr bgcolor=#D7EBFF align=center ><td height=22px>18837376</td>
        dateExample = b'2016-09-22'
        maxItemNumber = 15
        encodeDate = date.encode('utf-8')
        #p = b"<td>" + encodeDate[0:4]  # ac时间的模式识别 such as: <td>2016
        p=b'</td><td>'
        pSize = len(p)

        countItem = 0
        for i in range(0, len(data)):
            if data[i:i + pSize] == p:  # 被模式识别成功 p开头
                j=i+pSize
                if data[j+4:j+5]==data[j+7:j+8] and data[j+4:j+5]==b'-':
                    countItem += 1
                    acDate = data[j:j+len(dateExample)]  # 获取ac时间
                    if acDate >= encodeDate:  # 在给定时间之后AC的 添加进dict
                        probIDp=b'pid='
                        while data[j:j+len(probIDp)]!=probIDp:
                            j+=1
                        j+=len(probIDp)
                        k=j
                        while data[k:k+1]>=b'0' and data[k:k+1]<=b'9':
                            k+=1
                        problemID = data[j:k].decode('utf-8')
                        probIDStr = 'HDU' + problemID
                        if probIDStr not in dict:
                            dict[probIDStr] = self.getLevel(problemID)  # 计算难度
                    else:
                        return False
            if countItem == maxItemNumber:
                return True

    def getLevel(self,problemID):  # level=ac人数*10 / 提交人数 取整
        url = 'http://acm.hdu.edu.cn/showproblem.php?pid='
        url = url + problemID
        getWeber = GetWeb(url)
        data = getWeber.getData()

        # submitExample='Total Submission(s): 7691&nbsp'
        # acSubmitExample='Accepted Submission(s): 5293<br>'

        submitP = 'Total Submission(s): '.encode('utf-8')
        acSubmitP = 'Accepted Submission(s): '.encode('utf-8')

        return self.getNumblersAfterStr(data, submitP) / self.getNumblersAfterStr(data, acSubmitP)

    def getNextPageUrl(self,nowPageData):
        # <a style="margin-right:20px" href="/status.php?first=18426130&user=13450765437&pid=&lang=&status=5#status">Next Page
        p = b'">Next Page'
        head = b'http://acm.hdu.edu.cn'
        # http://acm.hdu.edu.cn/status.php?last=17850310&user=gdpuDong&pid=&lang=&status=5#status
        for i in range(0, len(nowPageData)):
            if p == nowPageData[i:i + len(p)]:
                j = i
                while nowPageData[j:j + 1] != b'"':
                    j -= 1
                nextPageUrlEndIndex = j
                j -= 1
                while nowPageData[j:j + 1] != b'"':
                    j -= 1
                nextPageUrlStartIndex = j + 1
                return head + nowPageData[nextPageUrlStartIndex:nextPageUrlEndIndex]

    def acProblemsFirstPageUrl(self):
        return 'http://acm.hdu.edu.cn/status.php?user=' + self.ID + '&status=5'
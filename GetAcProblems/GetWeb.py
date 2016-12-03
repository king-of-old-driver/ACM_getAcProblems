#encoding:UTF-8
import urllib.request
import socket
import sys
import http

class GetWeb:
    TIME_OUT_LIMIT=2#设置连接超时为1s
    TRYTIMES=100#重试次数
    def __init__(self,url,decode=False,decodeTo='utf-8'):
        self.url = url

        for i in range(self.TRYTIMES):
            try:
                self.data = urllib.request.urlopen(url,timeout=self.TIME_OUT_LIMIT).read()
                break
            except ConnectionResetError:
                print('Connection reset by peer[连接被重置]...正在重试.....')
            except socket.timeout:
                print('socket.timeout: timed out[连接超时]...正在重试.....')
            except http.client.IncompleteRead:
                #print('http.client.IncompleteRead: IncompleteRead...正在重试')
                pass
        else:
            print("无法连接到目标url!")
            sys.exit(0)

        if decode:
            try:
                if decode:
                    self.data = self.data.decode(decodeTo)
            except UnicodeDecodeError:
                pass

    def save(self,path,style="wb"):
        file=open(path,style)
        file.write(self.data)

    def getData(self):
        return self.data
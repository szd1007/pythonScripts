#-*- encoding: gb2312 -*-
import HTMLParser

class MyParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
    def read_content(self,path):
        f = open(path)
        lines = f.readlines()
        content = ""
        for line in lines:
            content += line
        return content
    
        
    def handle_starttag(self, tag, attrs):
        # �������¶����˴���ʼ��ǩ�ĺ���
        if tag == 'a':
            # �жϱ�ǩ<a>������
            for name,value in attrs:
                if name == 'href':
                    if "http://d" in value:
                        if "pin=&" in value:
                            print value
                        else:
                            s = value.index("pin=")
                            e = value.index("&",s)
                            pin =value[s:e]
                            pinReplace = "pin=1321085436-727786"
                            url = value.replace(pin,pinReplace)
                            
                            print url+"#"+pinReplace
        

if __name__ == '__main__':
    a = '<html><head><title>test</title><body><a href="http://www.163.com">���ӵ�163</a></body></html>'
    
    my = MyParser()
    # ����Ҫ���������ݣ���html�ġ�
    content = my.read_content("mixerUrl.txt")
    my.feed(content)
    

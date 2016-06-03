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
        # 这里重新定义了处理开始标签的函数
        if tag == 'a':
            # 判断标签<a>的属性
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
    a = '<html><head><title>test</title><body><a href="http://www.163.com">链接到163</a></body></html>'
    
    my = MyParser()
    # 传入要分析的数据，是html的。
    content = my.read_content("mixerUrl.txt")
    my.feed(content)
    

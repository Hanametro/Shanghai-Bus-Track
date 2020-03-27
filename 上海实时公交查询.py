# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import requests

def MD5(x):
    import hashlib
    
    m = hashlib.md5()
    b = x.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()
    return str_md5
try:
    bnumber=input("请输入公交线路（例：71路，北安线）：")
    dire=input("请输入上下行(0或1)：")
    stopid=input("请输入车站序号：")
    bn=MD5(bnumber)
            
    postdata={'stoptype':dire,'stopid':stopid,'sid':bn }
    r=requests.post('https://shanghaicity.openservice.kankanews.com/public/bus/Getstop',data=postdata)
    result=r.text
    print(bnumber,"实时公交信息\n")
    if result=='{"error":"-2"}':
        print("暂未发车\n")
    else:
        rs=result.strip('[\'{').strip(']}\'').split(",")
        busnumber=((rs[1].strip('\'').strip('\"').split(":"))[1].strip('\"')).encode('utf-8').decode("unicode-escape")
        stopdis=((rs[2].strip('\'').strip('\"').split(":"))[1].strip('\"'))
        distance=((rs[3].strip('\'').strip('\"').split(":"))[1].strip('\"'))
        time=((rs[4].strip('\'').strip('\"').split(":"))[1].strip('\"'))
                
        print(busnumber,"\n","距离本站：",stopdis,"站，",distance,"m\n","预计",time,"s后到达本站\n")
        
except:
    exit()
# -*- coding: utf-8 -*-
import requests
import csv
def MD5(x):
    import hashlib
    
    m = hashlib.md5()
    b = x.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()
    return str_md5
with open('busdata.csv',encoding='utf-8')as t:
        t_csv = csv.reader(t)
        for row in t_csv:
            bnumber=row[0]
            dire=row[1]
            stopid=row[2]
            stopname=row[3]
            dest=row[4]
            bn=MD5(bnumber)
            
            postdata={'stoptype':dire,'stopid':stopid,'sid':bn }
            r=requests.post('https://shanghaicity.openservice.kankanews.com/public/bus/Getstop',data=postdata)
            result=r.text
            print(bnumber," ",stopname," 车站(",dest,"方向)")
            if result=='{"error":"-2"}':
                print("暂未发车\n")
            else:
                rs=result.strip('[\'{').strip(']}\'').split(",")
                busnumber=((rs[1].strip('\'').strip('\"').split(":"))[1].strip('\"')).encode('utf-8').decode("unicode-escape")
                stopdis=((rs[2].strip('\'').strip('\"').split(":"))[1].strip('\"'))
                distance=((rs[3].strip('\'').strip('\"').split(":"))[1].strip('\"'))
                time=((rs[4].strip('\'').strip('\"').split(":"))[1].strip('\"'))
                
                print(busnumber,"\n","距离本站：",stopdis,"站，",distance,"m\n","预计",time,"s后到达本站\n")
            print("--------------------------------")
a=input(" ")
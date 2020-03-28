# -*- coding: utf-8 -*-
import requests
import urllib
from bs4 import BeautifulSoup
def MD5(x):
    import hashlib
    
    m = hashlib.md5()
    b = x.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()
    return str_md5
try:
    bnumber=input("请输入公交线路（例：71路，北安线）：")
    bn=MD5(bnumber)
    stoplist=[]        
    
    url1="https://shanghaicity.openservice.kankanews.com/public/bus/mes/sid/"+bn
    r1 = requests.get(url1)
    soup = BeautifulSoup(r1.text, 'html.parser')
    stop_list = soup.find_all('span', class_='name')
    for item in stop_list:       
        a=item.text
        stoplist.append(a)
   
    dire=input("请输入上下行(0："+stoplist[-1]+" 方向； 1:"+stoplist[0]+" 方向)：")
    if dire=="1":
        stoplist=[]
        url2="https://shanghaicity.openservice.kankanews.com/public/bus/mes/sid/"+bn+"?stoptype=1"
        r1 = requests.get(url2)
        soup = BeautifulSoup(r1.text, 'html.parser')
        stop_list = soup.find_all('span', class_='name')
        for item in stop_list:       
            a=item.text
            stoplist.append(a)
 
    j=1
    present=[]
    detail={}
    for i in stoplist:          
        stopid=str(j)
        postdata={'stoptype':dire,'stopid':stopid,'sid':bn }
        r=requests.post('https://shanghaicity.openservice.kankanews.com/public/bus/Getstop',data=postdata)
        result=r.text
        id=int(stopid)-1
       # print("\n",bnumber," ",stoplist[id]," 车站 实时公交信息\n")
        
        if result=='{"error":"-2"}':
            #print("暂未发车\n")
            pass
        else:
            rs=result.strip('[\'{').strip(']}\'').split(",")
            busnumber=((rs[1].strip('\'').strip('\"').split(":"))[1].strip('\"')).encode('utf-8').decode("unicode-escape")
            stopdis=((rs[2].strip('\'').strip('\"').split(":"))[1].strip('\"'))
            distance=((rs[3].strip('\'').strip('\"').split(":"))[1].strip('\"'))
            time=((rs[4].strip('\'').strip('\"').split(":"))[1].strip('\"'))                    
            #print(busnumber,"\n","距离本站：",stopdis,"站，",distance,"m\n","预计",time,"s后到达本站\n")
            if int(stopdis)==1:
                present.append(id)
                detail[id]=[busnumber,distance]
        j=j+1
        
    try:
        print("\n",bnumber," 开往：",stoplist[-1],"方向  \n 沿途站点：\n")
        i=1
        for it in stoplist:
            if i in present:
                number=detail[i][0]
                distance=detail[i][1]
                print(str(i),".",stoplist[i-1],"  🚌↓  " ,number ,"距离下站：",distance,"m")
            else:
                print(str(i),".",stoplist[i-1])
            i=i+1
    except:
        pass
except:
    exit()
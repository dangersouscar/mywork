#线机票价格查询
import requests
import datetime
import pandas as pd
import numpy as np
import matplotlib

getallcityandairports='https://b2c.csair.com/ita/intl/app'
headers ={
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding":"gzip,deflate,br",
"Accept-Language":"zh-CN,zh;q=0.9",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Content-Length":"139",
"Content-Type":"application/x-www-form-urlencoded",
"Cookie":"likev_user_id=4a2e5ec6-4aa0-4f14-e653-553349027e43;sid=52130c9a3fe14654b18547aeb4b11bb3;globalroute=cn_CN_cn;_gscu_422057653=04594197w9j5y214;_gcl_au=1.1.828354503.1604594433;ticketBoolingSearch=%7B%22segType%22%3A%22S%22%2C%22adultNum%22%3A%221%22%2C%22childNum%22%3A%220%22%2C%22infantNum%22%3A%220%22%2C%22citys%22%3A%5B%7B%22id%22%3A%22single-formCity%22%2C%22value%22%3A%22%E8%BE%BE%E5%8D%A1%22%7D%2C%7B%22id%22%3A%22single-formCityCode%22%2C%22value%22%3A%22DAC%22%7D%2C%7B%22id%22%3A%22isdepair%22%2C%22value%22%3Afalse%7D%2C%7B%22id%22%3A%22single-toCity%22%2C%22value%22%3A%22%E5%B9%BF%E5%B7%9E%22%7D%2C%7B%22id%22%3A%22single-toCityCode%22%2C%22value%22%3A%22CAN%22%7D%2C%7B%22id%22%3A%22isarrair%22%2C%22value%22%3Afalse%7D%5D%2C%22dates%22%3A%5B%7B%22id%22%3A%22single-formCalender%22%2C%22value%22%3A%222020-11-07%22%2C%22minDate%22%3A%22%2B0d%22%7D%5D%7D;last_session_stm_8mrmut7r76ntg21b=1604848618832;likev_session_id_8mrmut7r76ntg21b=f7b42271-82d3-461d-ae11-4b3b34175203;last_session_id_8mrmut7r76ntg21b=f7b42271-82d3-461d-ae11-4b3b34175203;temp_zh=cou%3D0%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2020-11-07%3B%E8%BE%BE%E5%8D%A1-%E5%B9%BF%E5%B7%9E%3B1%2C0%2C0%3B00%3B%26cou%3D1%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2020-11-08%3B%E8%BE%BE%E5%8D%A1-%E5%B9%BF%E5%B7%9E%3B1%2C0%2C0%3B00%3B%26cou%3D2%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2020-11-09%3B%E8%A5%BF%E5%AE%89-%E5%B9%BF%E5%B7%9E%3B1%2C0%2C0%3B00%3B%26cou%3D3%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2020-11-09%3B%E8%BE%BE%E5%8D%A1-%E5%B9%BF%E5%B7%9E%3B1%2C0%2C0%3B00%3B%26;ycyintang.session.id=1a3e5eb6-de48-4fc0-b5e1-829b532bca2a;WT.al_flight=WT.al_hctype%28S%29%3AWT.al_orgcity1%28DAC%29%3AWT.al_dstcity1%28CAN%29%3AWT.al_orgdate1%282020-11-09%29%3AWT.al_adultnum%281%29%3AWT.al_childnum%280%29%3AWT.al_infantnum%280%29;JSESSIONID=E8E8CEB237EDA5B595E7208998D2C0F9;language=zh_CN;_gscbrs_422057653=1;zsluserCookie=true;_gscs_422057653=04848622x6p9f011|pv:36;WT-FPC=id=37.111.193.200-3408441856.30847889:lv=1604854176837:ss=1604848533221:fs=1604594183249:pn=36:vn=6;likev_session_etm_8mrmut7r76ntg21b=1604854183731",
"Host":"b2c.csair.com",
"Origin":"https://b2c.csair.com",
"Referer":"https://b2c.csair.com/ita/intl/zh/flights?flex=1&m=0&p=100&t=DAC-CAN-20201109&egs=ITA,ITA&open=1&flex=1&nb=1",
"Sec-Fetch-Dest":"document",
"Sec-Fetch-Mode":"navigate",
"Sec-Fetch-Site":"same-origin",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/86.0.4240.183Safari/537.36",
}
data = {
"language":"zh",
"country":"cn",
"m":"0",
"adt":"1",
"cnn":"0",
"inf":"0",
"dep":"DAC",
"depName":"DAC",
"arr":"CAN",
"arrName":"CAN",
"date":"20210231",
"flexible":"1",
"nearAirlineRecommend":"1",
"open":"1",
}
res=requests.post(getallcityandairports,data=data,headers=headers)
print(res.text)
print(res.text.find('execution'))
x=int(res.text.find('execution'))+10
id=res.text[x:x+32]
print(res.text[x:x+32])











filepath2=r"https://b2c.csair.com/ita/rest/intl/minprice/calendar?execution="+id+"&country=cn&_=1604577692146"
print(filepath2)
def get_data(filepath2):
    url = filepath2
    time1 = str(datetime.datetime.now())[0:10].replace("-","")
    res1=str(requests.get(url).text)
    print(res1)
    df = pd.read_csv(url,encoding='gb18030')
    return res1
df = get_data(filepath2)
x=eval(df)["ita"]["day"]
data=pd.DataFrame(x)
data=data[(data.price>0)]
print(data)

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
 
my_sender='862947189@qq.com'    # 发件人邮箱账号
my_pass = 'wjxmbudnzpjpbahf'              # 发件人邮箱密码
my_user=["caidenghong008@gmail.com"]    # 收件人邮箱账号，我这边发送给自己
def mail():
    ret=True
    try:
        msg=MIMEText(data.to_html(escape=False),'html','utf-8')
        
        msg['From']=formataddr(["南方航空机票查询早报",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=','.join(my_user)              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="南方航空机票查询早报"                # 邮件的主题，也可以说是标题
        print(msg['To'])
 
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,msg['To'].split(','),msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret
 
ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")



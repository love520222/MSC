#箐优网APP签到脚本


import requests
import json

#sever酱SCkey
SCkey = '***********'

Cookie = '*************************'



##################################################以下内容请勿修改###############################################
def start():
    headers={
    'version': '139',
    'authorization': 'Token 9F5BBF8F752F060B00D38F7C81686852695A463CD5661FE0848CBEADB3ACFD5E25FB42EF1D4D08242D7CBEFE5DE9358F8FF34CE90E2404ED1810F66F464007F19BF66EDD2BB06B3A7651C2D453332F0C2EE87E2810C5850A71E6CA0758650940332187A92844AFB9AE1528B9986BAA02F2DC61A3F0878B9CECD2FFB4599B19EE41E8572D6FB5569B8D535EA8F8B2D3BB5C67941B071C72BF703EA8BBF56AF087',
   'deviceid': '99001301564902',
   'package': 'jyeoo.app.ystudy',
   'imei': '99001301564902',
   'platformname': 'AndroidPhone',
   'versionname': 'ystudy3.7.9',
   'mac': '02:00:00:00:00:00',
   'platform': '2',
   'fingerprint': 'Xiaomi/raphael/raphael:9/PKQ1.181121.001/V10.3.7.0.PFKCNXM:user/release-keys',
   'content-length': '0',
    'user-agent': 'Apache-HttpClient/UNAVAILABLE (java 1.4)',
    'mato-app-id': 'jyeoo.app.ystudy',
    'x-maa-pic-param': '01246400',
    'x-maa-auth': '783958689_1577699365_9a313da9f7ef0873c3fca50bb9aee03d',
    'x-remove-iphost': '0',
    'x-maa-alias': '.wifi.maa.f924b2d.maasdk.com',
    'mato-net': 'CM,WIFI',
    'mato-version': '7.8.0.12.0,2',
    'x-maa-display-id': '3939303031333031353634393032',
    'accept-encoding': 'gzip, deflate,wzip',
    'x-maa-mark': '6c47e4cd98359d2bd88a43280c1d2f7b',
    'cookie': 'jyean=tlnG9NAWoPhxyuoE72RMusIJbvmmqzri_GbBvxk9ETbClGscbBtN4CmTvKOaiyqIwmQKzn-e76QltM6cWikH6cywYPZmxVkDyg5_-RYvkUlQ0qvHwlJ_IxE0oG-MVAcd0',
    'Cookie': Cookie ,

    }
    url="http://api.jyeoo.com/AppTag/UserSign"
    # session = requests.Session()
    # session.trust_env = False  # No proxy settings from the OS
    # r = session.post(url=url,headers=headers, verify=True)
    c=requests.post(url=url,headers=headers)
    d=json.loads(c.text)
    e = d['Msg']
    def pdj():
        if e == '' :
            return '签到成功'
        else:
            return e
    f = str(pdj())
    requests.get('https://sc.ftqq.com/'+ SCkey +'.send?text=' + '箐优自动签到：' + f + '&desp=' + '箐优网APP自动签到已执行')
    print('箐优网APP签到已完成',f)
def main_handler(event, context):
    return start()


if __name__ == '__main__':
    start()

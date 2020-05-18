import requests,re

class QQVideo(object):

    def __init__(self):
        self.sign1 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_system&cmd=2'   #电脑
        self.sign2 = 'https://v.qq.com/x/bu/mobile_checkin' #手机
        # 获取cookie接口
        self.auth_refresh = 'https://access.video.qq.com/user/auth_refresh?*****************************************************'
        # 通知密钥
        self.SCkey = '******************************************'
        # 登录headers
        self.login_headers = {
            'Referer': 'https://v.qq.com',
            'Cookie': '**************************************************'
        }
        # 签到headers
    def Login_sign(self):
        try:
            login = requests.get(self.auth_refresh,headers= self.login_headers)
            cookie = requests.utils.dict_from_cookiejar(login.cookies)
            # print(cookie)
            sign_headers = {
                'Referer': 'https://m.v.qq.com',
                'Cookie': '***********************; vqq_vusession='+ cookie['vqq_vusession']+';'
            }

            sign1 = requests.get(self.sign1,headers= sign_headers).text
            count1 = re.findall('ccalendar-cell.*?checked.*?cell-day">\\s+(\\d+).*?text2">\\s+(已签到)', sign1)
            msg1 = '电脑累签到' + str(len(count1)) + '天,本次获得V值：' + sign1[42:-14]
            # print(msg1)

            sign2 = requests.get(self.sign2,headers= sign_headers)
            sign2s = sign2.text.encode(sign2.encoding).decode(sign2.apparent_encoding)
            sign2ss = re.findall('''<div key="\d" class="ccalendar-cell sp checked today "><div class="ccalendar-cell-text1">
        今日
      </div> <div class="ccalendar-cell-day">
        3
      </div> <div class="ccalendar-cell-text2">([\s\S]*?)</div></div>''',sign2s)

            # sign2.encode='ISO-8859-1'
            sign2_content = '手机签到成功' if '已签到' in str(sign2ss) else '手机签到失败'
            # print(sign2.apparent_encoding)
            print (sign2_content)

            #print(sgin2)

            return msg1,sign2_content
        except Exception as e:
            return '本次签到失败，请检查Cookie或其它',str(e)

    def mssage(self,msg,msg1):
        # send = requests.post('https://sc.ftqq.com/' + self.SCkey + '.send?text=' + msg+ '&desp=' + msg1).text
        # print(send)
        return

def main_handler():
    sign = QQVideo().Login_sign()
    content = ', '.join(sign)
    content1 = sign[1]
    QQVideo().mssage(content,content1)
    return

main_handler()




#执行失败


import requests,re

class QQVideo(object):

    def __init__(self):
        self.sign1 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_system&cmd=2'   #电脑
        self.sign2 = 'https://v.qq.com/x/bu/mobile_checkin' #手机
        # 获取cookie接口
        self.auth_refresh = 'https://access.video.qq.com/user/auth_refresh?vappid=11059694&vsecret=fdf61a6be0aad57132bc5cdf78ac30145b6cd2c1470b0cfe&type=qq&g_tk=&g_vstk=1902091394&g_actk=1766092375&callback=jQuery19104864986985868831_1575435945374&_=1575435945375'
        # 通知密钥
        self.SCkey = 'SCU92528T39cb446ef8bbbe4cddede43fba309e545e8853a90b6de'
        # 登录headers
        self.login_headers = {
            'Referer': 'https://v.qq.com',
            'Cookie': 'video_guid=f8fd5cfcbc43c9b9; video_platform=2; pgv_pvi=9681966080; RK=GZJFNICdOv; ptcz=7a3bee237d87fc853b81f6d13249459cfad37950ac64e370e46d492ecc045d80; pgv_pvid=6460783459; eas_sid=i105O7V4s7y4m5C740n2b0a2E8; tvfe_boss_uuid=70fd826c217464a7; uin_cookie=o2670874998; ied_qq=o2670874998; o_cookie=2670874998; pac_uid=1_2670874998; _video_qq_login_time_init=1584096503; LW_sid=U1U5g8h4o2L5t8H320S0F7A5J5; LW_uid=t1l548M49285G8o3j0e0h7F5q6; main_login=qq; vqq_access_token=D196420F6EA7D354BF083C591C66F597; vqq_appid=101483052; vqq_openid=374954F29E5134E39942EA1F34E99E1C; vqq_vuserid=182670357; vqq_refresh_token=B0505B78CF41661DC219354A26F7AE26; uid=263354044; pgv_info=ssid=s307562740; vqq_vusession=h8QletqHqUaEZKk9rxnztw..; vqq_next_refresh_time=6600; vqq_login_time_init=1584509312; login_time_last=2020-3-18 13:28:34; pgv_si=s9853820928; _qpsvr_localtk=0.08989873614605148'
        }
        # 签到headers
    def Login_sign(self):
        try:
            login = requests.get(self.auth_refresh,headers= self.login_headers)
            cookie = requests.utils.dict_from_cookiejar(login.cookies)
            # print(cookie)
            sign_headers = {
                'Referer': 'https://m.v.qq.com',
                'Cookie': 'video_guid=f8fd5cfcbc43c9b9; video_platform=2; pgv_pvi=9681966080; RK=GZJFNICdOv; ptcz=7a3bee237d87fc853b81f6d13249459cfad37950ac64e370e46d492ecc045d80; pgv_pvid=6460783459; eas_sid=i105O7V4s7y4m5C740n2b0a2E8; tvfe_boss_uuid=70fd826c217464a7; uin_cookie=o2670874998; ied_qq=o2670874998; o_cookie=2670874998; pac_uid=1_2670874998; _video_qq_login_time_init=1584096503; LW_sid=U1U5g8h4o2L5t8H320S0F7A5J5; LW_uid=t1l548M49285G8o3j0e0h7F5q6; main_login=qq; vqq_access_token=D196420F6EA7D354BF083C591C66F597; vqq_appid=101483052; vqq_openid=374954F29E5134E39942EA1F34E99E1C; vqq_vuserid=182670357; vqq_refresh_token=B0505B78CF41661DC219354A26F7AE26; uid=263354044; pgv_info=ssid=s307562740; vqq_vusession='+ cookie['vqq_vusession']+';'
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


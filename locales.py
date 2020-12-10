import requests
with open('token', 'r') as file:
    token = file.read()
auth    = {'Authorization': token}
res     = requests.get('https://discordapp.com/api/v6/users/@me', headers=auth)
localeo = res.json().get('locale')
if localeo == 'da':
    localey = 'Dansk'
elif localeo == 'de':
    localey = 'Deutsch'
elif localeo == 'en-GB':
    localey = 'UK'
elif localeo == 'en-US':
    localey = 'US'
elif localeo == 'es-ES':
    localey = 'Spanish'
elif localeo == 'fr':
    localey = 'French'
elif localeo == 'hr':
    localey = 'Croatian'
elif localeo == 'it':
    localey = 'Italian'
elif localeo == 'lt':
    localey = 'Lithuanian'
elif localeo == 'hu':
    localey = 'Hungarian'
elif localeo == 'nl':
    localey = 'Dutch'
elif localeo == 'no':
    localey = 'Norwegian'
elif localeo == 'pl':
    localey = 'Polish'
elif localeo == 'pt-BR':
    localey = 'Portuguese'
elif localeo == 'ro':
    localey = 'Romanian'
elif localeo == 'fi':
    localey = 'Finnish'
elif localeo == 'sv-SE':
    localey = 'Swedish'
elif localeo == 'vi':
    localey = 'Vietnamese'
elif localeo == 'tr':
    localey = 'Turkish'
elif localeo == 'cs':
    localey = 'Czech'
elif localeo == 'el':
    localey = 'Greek'
elif localeo == 'bg':
    localey = 'Bulgarian'
elif localeo == 'ru':
    localey = 'Russian'
elif localeo == 'uk':
    localey = 'Ukrainian'
elif localeo == 'th':
    localey = 'Thai'
elif localeo == 'zh-CN':
    localey = 'Chinese'
elif localeo == 'ja':
    localey = 'Japanese'
elif localeo == 'zh-TW':
    localey = 'Chinese'
elif localeo == 'ko':
    localey = 'Korean'
else:
	localey = 'N/A'
with open('templocale', 'w') as file:
    file.write(localey)
    file.close
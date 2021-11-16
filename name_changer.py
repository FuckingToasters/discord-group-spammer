import requests,threading,random,json

config = json.load(open('config.json'))
token = config.get('token')
def r():
    while True:
        channelid = random.choice(open('group_id.txt').readlines()).strip('\n')
        names = ['github.com/fuckinmoney'] # ADD MORE IF NEEDED
        response = requests.patch(f'https://discord.com/api/v9/channels/{channelid}',  headers={'Authorization': token}, json = {'name': random.choice(names)})
        print(response.content)
        print(response)

th = 10
for i in range(th):
    t = threading.Thread(target=r)
    t.start()

import requests , threading, random, json
open('log.txt', 'w').close()
user_id = input('Enter User ID:')
config = json.load(open('config.json'))
token = config.get('token')

def sendreq():
    shit = open('group_id.txt')
    for line in shit:
        l2 = random.choice(open('group_id.txt').readlines())
        already_checked = open('log.txt', mode='r')
        all_of_it = already_checked.read()
        check = all_of_it.find(l2)
        if check != -1:
            pass
        else:
            f = open('log.txt', 'a')
            f.write(l2)
            f.close()
            channelid = l2.strip('\n')
            response = requests.put(f'https://discord.com/api/v9/channels/{channelid}/recipients/{user_id}',headers={'Authorization': token})

th = 10
for i in range(th):
    t = threading.Thread(target=sendreq)
    t.start()


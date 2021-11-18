# make sure to look at the other files and sometimes you se something around "with open("...txt") as file:" 
# this is defently better then just open(...) as it manage the files automatically and you will not need to close the files manually etc.
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

# changing the value of the variable "th" might cause connection issues and the whole code will run wayyy slower even if you put a higher number.
# this number do NOT mean the total requests. the number of connections at the same time is meant. the total connections are defined in for line in shit
# so the total number of connections equals to the lines of the group_id.txt file.
th = 10
for i in range(th):
    t = threading.Thread(target=sendreq)
    t.start()


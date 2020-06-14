from io import BytesIO
from PIL import Image
import requests
import time
import sys
import os

#################################################
#             Variables declaration             #
#################################################

version = "0.1"
CHROME_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
FIREFOX_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
IE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'

#################################################
#                     Color                     #
#################################################

class colors:
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

#################################################
#            Declaration of function            #
#################################################

def exitApps():
    sys.exit(f"{colors.fg.lightblue}Exiting...")

def showHelp():
    print("")
    print(f"{colors.bg.lightgrey}{colors.fg.black}exit{colors.reset}{colors.disable} -> {colors.reset}Exit the application.")
    print(f"{colors.bg.lightgrey}{colors.fg.black}help{colors.reset}{colors.disable} -> {colors.reset}Displays the help utility.")
    print(f"{colors.bg.lightgrey}{colors.fg.black}icon{colors.reset}{colors.disable} -> {colors.reset}Allows to retrieve a user's icons")
    print(f"{colors.bg.lightgrey}{colors.fg.black}orgs{colors.reset}{colors.disable} -> {colors.reset}Retrieves information about an organization")
    print(f"{colors.bg.lightgrey}{colors.fg.black}user{colors.reset}{colors.disable} -> {colors.reset}Retrieves information about a user")
    print("")

def getIcons():
    userOrgs = input(f"{colors.fg.cyan}Do you want to retrieve the icon of a user or an organization? (U/O):{colors.reset} ")
    if(userOrgs.lower() == "u" or userOrgs.lower() == "user" or userOrgs.lower() == "users"):
        getIconsUsername()
        return
    if(userOrgs.lower() == "o" or userOrgs.lower() == "org" or userOrgs.lower() == "orgs"):
        getIconsOrgs()
        return
    print(f"{colors.fg.yellow}You canceled the operation!{colors.reset}")

def getIconsUsername():
    print()
    username = input(f"{colors.fg.cyan}Enter username: {colors.reset}")
    iconRQ = requests.get("https://api.github.com/users/" + username, headers={'User-Agent': CHROME_USER_AGENT})
    iconJSON = iconRQ.json()
    if not "message" in iconJSON:
        question = input(f"{colors.fg.cyan}Do you want to display the image? (Y/N): {colors.reset}")
        if(question.lower() == "y" or question.lower() == "yes"):
            imgURL = requests.get(iconJSON['avatar_url'])
            if(imgURL.status_code != 200):
                print(f"{colors.fg.red}ERROR: An error has occurred.{colors.reset}")
            else:
                img = Image.open(BytesIO(imgURL.content))
                img.show()
        print(colors.fg.pink + iconJSON['avatar_url'] + colors.reset)
    else:
        print(f"{colors.fg.red}ERROR: The username entered is invalid!{colors.reset}")

def getIconsOrgs():
    print()
    orgs = input(f"{colors.fg.cyan}Enter the name of the organization: {colors.reset}")
    orgsICON = requests.get("https://api.github.com/orgs/" + orgs, headers={'User-Agent': CHROME_USER_AGENT})
    orgsIconJSON = orgsICON.json()
    if not "message" in orgsIconJSON:
        question = input(f"{colors.fg.cyan}Do you want to display the image? (Y/N): {colors.reset}")
        if(question.lower() == "y" or question.lower() == "yes"):
            imgURL = requests.get(orgsIconJSON['avatar_url'])
            if(imgURL.status_code != 200):
                print(f"{colors.fg.red}ERROR: An error has occurred.{colors.reset}")
            else:
                img = Image.open(BytesIO(imgURL.content))
                img.show()
        print(colors.fg.pink + orgsIconJSON['avatar_url'] + colors.reset)
    else:
        print(f"{colors.fg.red}ERROR: The name of the organization is invalid!{colors.reset}")

def getUsers():
    username = input(f"{colors.fg.cyan}Enter username: {colors.reset}")
    usernameRequest = requests.get("https://api.github.com/users/" + username, headers={'User-Agent': CHROME_USER_AGENT})
    userJSON = usernameRequest.json()
    if not "message" in userJSON:
        print("")
        print("Username: " + userJSON['login'])
        if(userJSON['bio'] != ""):
            print("Description: " + str(userJSON['bio']))
        else:
            print("Description: None")
        print("ID: " + str(userJSON['id']))
        print("Node ID: " + userJSON['node_id'])
        if(userJSON['site_admin'] == True):
            print("Site Admin: True")
        else:
            print("Site Admin: False")
        if(userJSON['name'] != ""):
            print("Name: " + str(userJSON['name']))
        else:
            print("Name: None")
        if(userJSON['company'] != ""):
            print("Company: " + str(userJSON['company']))
        else:
            print("Company: None")
        if(userJSON['blog'] != ""):
            print("Website: " + str(userJSON['blog']))
        else:
            print("Website: None")
        if(userJSON['twitter_username'] != None):
            print("Twitter Username: @" + str(userJSON['twitter_username']))
            print("Twitter Username: https://twitter.com/" + str(userJSON['twitter_username']))
        else:
            print("Twitter Username: None")
        if(userJSON['location'] != ""):
            print("Location: " + str(userJSON['location']))
        else:
            print("Location: None")
        print("Repositories: " + str(userJSON['public_repos']))
        print("Gists: " + str(userJSON['public_gists']))
        print("Followers: " + str(userJSON['followers']))
        print("Following: " + str(userJSON['following']))
        print("Created At: " + str(userJSON['created_at']))
        print("Updated At: " + str(userJSON['updated_at']))
    else:
        print(f"{colors.fg.red}ERROR: The username entered is invalid!{colors.reset}")

def getOrgs():
    organization = input(f"{colors.fg.cyan}Enter the name of the organization: {colors.reset}")
    req = requests.get("https://api.github.com/orgs/" + organization, headers={'User-Agent': CHROME_USER_AGENT})
    json = req.json()
    if not "message" in json:
        print("")
        print("Login: " + json["login"])
        print("ID: " + str(json["id"]))
        print("Node ID: " + json["node_id"])
        print("URL: https://github.com/" + str(json['login']))
        if(json['name'] != ""):
            print("Name: " + str(json['name']))
        else:
            print("Name: None")
        if(json['description'] != ""):
            print("Description: " + str(json['description']))
        else:
            print("Description: None")
        if(json['blog'] != None):
            print("Website: " + str(json['blog']))
        else:
            print("Website: None")
        if(json['email'] != None):
            print("Email: " + str(json['email']))
        else:
            print("Email: None")
        if(json['twitter_username'] != None):
            print("Twitter Username: @" + str(json['twitter_username']))
            print("Twitterl URL: https://twitter.com/" + str(json['twitter_username']))
        else:
            print("Twitter Username: None")
        print("Verified: " + str(json['is_verified']))
        print("Repositories: " + str(json['public_repos']))
        print("Gists: " + str(json['public_gists']))
        print("Created At: " + str(json['created_at']))
        print("Updated At: " + str(json['updated_at']))
    else:
        print(f"{colors.fg.red}ERROR: The name of the organization is invalid!{colors.reset}")

#################################################
#           Launching the application           #
#################################################

print("####################################################")
print("#          Github Statistics - By VCoding          #")
print("#                   Version: " + version + "                   #")
print("####################################################")
print("\n\nWelcome to the Github Statistics project.")
print("Write to help to see the list of available commands.")

while(True):
    x = input(f"{colors.fg.purple}>> {colors.reset}")
    if(x.lower() == "exit"):
        exitApps()
    if(x.lower() == "help"):
        showHelp()
    if(x.lower() == "icon" or x.lower() == "icons"):
        getIcons()
    if(x.lower() == "user" or x.lower() == "users"):
        getUsers()
    if(x.lower() == "org" or x.lower() == "orgs"):
        getOrgs()

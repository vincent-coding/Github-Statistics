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
#            Declaration of function            #
#################################################

def showHelp():
    print("")
    print("exit -> Exit the application.")
    print("help -> Displays the help utility.")
    print("icon -> Allows to retrieve a user's icons")
    print("orgs -> Retrieves information about an organization")
    print("user -> Retrieves information about a user")
    print("")

def getIcons():
    userOrgs = input("Do you want to retrieve the icon of a user or an organization? (U/O): ")
    if(userOrgs.lower() == "u" or userOrgs.lower() == "user" or userOrgs.lower() == "users"):
        getIconsUsername()
        return
    if(userOrgs.lower() == "o" or userOrgs.lower() == "org" or userOrgs.lower() == "orgs"):
        getIconsOrgs()
        return
    print("You canceled the operation!")

def getIconsUsername():
    print()
    username = input("Enter username: ")
    iconRQ = requests.get("https://api.github.com/users/" + username, headers={'User-Agent': CHROME_USER_AGENT})
    iconJSON = iconRQ.json()
    if not "message" in iconJSON:
        question = input("Do you want to display the image? (Y/N): ")
        if(question.lower() == "y" or question.lower() == "yes"):
            imgURL = requests.get(iconJSON['avatar_url'])
            if(imgURL.status_code != 200):
                print("ERROR: An error has occurred.")
            else:
                img = Image.open(BytesIO(imgURL.content))
                img.show()
        print(iconJSON['avatar_url'])
    else:
        print("ERROR: The username entered is invalid!")

def getIconsOrgs():
    print()
    orgs = input("Enter the name of the organization: ")
    orgsICON = requests.get("https://api.github.com/orgs/" + orgs, headers={'User-Agent': CHROME_USER_AGENT})
    orgsIconJSON = orgsICON.json()
    if not "message" in orgsIconJSON:
        question = input("Do you want to display the image? (Y/N): ")
        if(question.lower() == "y" or question.lower() == "yes"):
            imgURL = requests.get(orgsIconJSON['avatar_url'])
            if(imgURL.status_code != 200):
                print("ERROR: An error has occurred.")
            else:
                img = Image.open(BytesIO(imgURL.content))
                img.show()
        print(orgsIconJSON['avatar_url'])
    else:
        print("ERROR: The name of the organization is invalid!")

def getUsers():
    username = input("Enter username: ")
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
    else:
        print("ERROR: The username entered is invalid!")

def getOrgs():
    print("getOrgs")

#################################################
#           Launching the application           #
#################################################

print("####################################################")
time.sleep(0.2)
print("#          Github Statistics - By VCoding          #")
time.sleep(0.2)
print("#                   Version: " + version + "                   #")
time.sleep(0.2)
print("####################################################")
print("\n\nWelcome to the Github Statistics project.")
print("Write to help to see the list of available commands.")

while(True):
    x = input(">> ")
    if(x.lower() == "exit"):
        sys.exit()
    if(x.lower() == "help"):
        showHelp()
    if(x.lower() == "icon" or x.lower() == "icons"):
        getIcons()
    if(x.lower() == "user" or x.lower() == "users"):
        getUsers()
    if(x.lower() == "org" or x.lower() == "orgs"):
        getOrgs()

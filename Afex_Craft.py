
import os
import requests
import random


ver = "0.1"
# Payloads Start
 
def pc_info_paylaod():
  discord_url = input("Enter Discord Webhook URL: ")
  q_discord_url = input("Do you want to verify webhook  URL? (y / n) > ")

  if q_discord_url == "y":
    code = random.randint(1111, 9999)
    
    Message = {
    "content": "Your Code is: " + str(code)
    }    

    print("Sending Code .... ")

    requests.post(discord_url, data=Message)
    print()
    print()
    print()
    conf_code = input("Please enter code you get: ")
    
    if conf_code == code:
      print("Yes!, This webhook work! ")
    else:
      print("Opps! Invalid code!")
      exit()

  
# Payloads End




# Start
print("Welcome to Afex!")
updates_q = input("Do you want to check for updates? (y/n): ")

if updates_q == "y":
  last_ver = requests.get("https://raw.githubusercontent.com/S1AL53R/afex/main/VERSION")
  print()
  print("Your version is: " + ver)
  print("Last version is: " + str(last_ver.text))

  if ver == last_ver.text:
    print("No new updates!")
    last_ver_save = True

  else:
    print("Check GitHub Repo for last version.")
  last_ver_save = True

if updates_q == "n":
  update_skip = True
  last_ver_save = None

else:
  print("ERROR: PLEASE UPDATE !!!")
  exit()

os.system("clear")

print("Welcome to Afex!")

if last_ver_save == True:
  print("(Last) Version is " + ver)

if update_skip == True:
  print("Version is: " + ver)

print()
print("Please Select Payload...")
print("[1] Give Me Basic PC Info")

select_payload = input("Please Select | > ")

if select_payload == "1":
  pc_info_paylaod()

else:
  print("ERROR: INVALID OPTION TRY AGAIN !!!")
  exit()

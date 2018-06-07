from telethon import TelegramClient
import time
import random
# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
result = {}
path="settings"
with open(path, 'r', encoding='utf-8') as file:
    for line in file:
        value_pair = line.split('=')
        left = value_pair[0].strip()
        right = value_pair[1].strip()
        if right.isnumeric():
            result[left] = int(right)
        else:
            result[left] = right
print(result)

api_id = result['api_id'] 
api_hash = result['api_hash'] 

client = TelegramClient('session_name', api_id, api_hash)
client.start()
print("Connected to client.")
# Client message initialized
message = result['message']

with open("contacts.csv") as fileobject:
    for line in fileobject:
        print('Sending message to '+line)
        time.sleep(random.randint(5,10))
        client.send_message(line, message)
print("All the messages have been sent sucessfully.")
#print(client.get_me().stringify())

# client.send_file('username', '/home/myself/Pictures/holidays.jpg')

# client.download_profile_photo('me')
# messages = client.get_messages('+917000000000')
# client.download_media(messages[0])

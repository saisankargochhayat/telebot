# telebot


Steps to setup the project- 
Go to project directory - 

```pip3 install telethon```

(make sure you have python3 and pip3 installed.)

Now that you have telethon installed on your debian system-
 1. Go to this link - https://my.telegram.org/apps and make a client. For this step you need a working phone number and a telegram application. The app title and shortname can be anything of your choice. 
 2. Once you are done with this step copy the api_id and api_hash value. 
 3. Make a copy of 'settings.example' and rename it to 'settings'. With the message parameter containing the message you want to send to your clients. 
 4. Make a copy of 'contacts.csv.example' and rename it to 'contacts.csv' and add the numbers of clients whom you want to send message in telegram in interational format. (example in contacts.csv.example).
 5. Now run ```python3 telebot.py```. Complete the otp verification and the message sending will begin. 

Voilla you have sucessfully sent all your clients the specific message. 

from telethon.sync import TelegramClient

from telethon.sessions import StringSession

print ("")

print ("")

print("""processing.......""")

API_KEY = '2014211'

API_HASH = "fda65aa2e04bd13aa20f3c0594497b0b"

while True:

  try:

   with TelegramClient(StringSession(), API_KEY, API_HASH) as client:

      print("")

      session = client.session.save()

      client.send_message("me", f"Here is your TELEGRAM STRING SESSION\n(tap to copy)👇 \n\n `{session}`")

      print("You telegramString session successfully stored in your telegram, please check your Telegram Saved Messages ")

      print("Store it safe !!")

  except:

   print ("")

   print ("Wrong phone number \n make sure its with correct  country code")

   print ("")

   continue

  break


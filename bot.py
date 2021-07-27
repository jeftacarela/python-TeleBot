import os
import telebot
import zomatopy

# config={
#   "user_key":"ZOMATO_API_KEY"
# }
    
# zomato = zomatopy.initialize_app(config)

baseurl='https://developers.zomato.com/api/v2.1/geocode?lat=%f&lon=%f' %(lat,lon)
header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": "--------------ZOMATO KEY----------------------"}
    
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'ok, start')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,'what?')

def city_name(message):
    city_ID = zomato.get_city_ID(message)
    collections_dictionary = zomato.get_collections(city_ID, limit=10)
    bot.reply_to(message,collections_dictionary)
    return

def restautant(message):
    try:
        city_ID = zomato.get_city_ID(message)
        restaurant_dictionary = zomato.get_nearby_restaurant(city_ID, limit=10)
        bot.reply_to(message,collections_dictionary)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def nearby_restaurant_menu(message):
    username=message['from']['first_name']
    chat_id=message['from']['id']
    command=message['text']
    print(str(latitude))
    command=command.split(' ',1)[1]
    print(command)
    command=command.title()
    response= requests.get(baseurl,headers=header)
    ans = response.json()
    bot.reply_to(chat_id,"This is the link of the menu: ")
    for x in range(len(ans['nearby_restaurants'])):
        print(ans['nearby_restaurants'][x]['restaurant']['menu_url'])
        if ans['nearby_restaurants'][x]['restaurant']['name'] == command:
            print(ans['nearby_restaurants'][x]['restaurant']['menu_url'])
            bot.reply_to(chat_id,p['nearby_restaurants'][x]['restaurant']['menu_url'])
    # print(baseurl)
    return


def nearby_restaurant(message):
    username=message['from']['first_name']
    chat_id=message['from']['id']
    lat=message['location']['latitude']
    lon=message['location']['longitude']
    global latitude
    latitude=lat
    global longitude
    longitude=lon
    response = requests.get(baseurl, headers=header)
    # print(baseurl)
    print(str(lat))
    ans = response.json()
    bot.reply_to(chat_id,'These are the list :\n')
    for x in range(len(g['nearby_restaurants'])):
        print(ans['nearby_restaurants'][x]['restaurant']['name'])
        bot.reply_to(chat_id,g['nearby_restaurants'][x]['restaurant']['name'])        
    print(ans['nearby_restaurants'][0]['restaurant']['name'])
    return

print('bot running')
bot.polling()
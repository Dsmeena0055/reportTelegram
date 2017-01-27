import telebot
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_token = config['Telegram']['token']
bot = telebot.TeleBot(api_token)

link = config['Telegram']['link']
group_id = int(config['Telegram']['group_id'])
admin_id = int(config['Telegram']['admin_id'])

DB_HOST = config['Database']['DB_HOST']
DB_USER = config['Database']['DB_USER']
DB_PASS = config['Database']['DB_PASS']
DB_NAME = config['Database']['DB_NAME']

berserker = False
num_reports = 5
ban_time = 300

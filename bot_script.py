import os
import requests
import schedule
import time
from datetime import datetime
import pytz
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables from the .env file
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
API_URL = os.getenv('API_URL')

# Define the timezone (e.g., Asia/Tehran)
timezone = pytz.timezone('Asia/Tehran')

# Function to send a message to Telegram
def send_message(message):
    url = f'{API_URL}{BOT_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=data)

# Custom function to check if the current time matches the scheduled time
def is_time_correct(schedule_time):
    now = datetime.now(timezone)
    return now.strftime('%H:%M') == schedule_time

# Meal reminder functions
def remind_meal_1():
    if is_time_correct("12:00"):
        send_message("🍽 یک ساعت تا اولین وعده غذایی شما باقی مانده است. آماده شوید! (تخم مرغ نیمرو و بیکن)")

def meal_1_time():
    if is_time_correct("13:00"):
        send_message("🍽 زمان اولین وعده غذایی! (تخم مرغ نیمرو و بیکن)")

def remind_meal_2():
    if is_time_correct("16:00"):
        send_message("🍽 یک ساعت تا دومین وعده غذایی شما باقی مانده است. آماده شوید! (مرغ گریل شده و سبزیجات)")

def meal_2_time():
    if is_time_correct("17:00"):
        send_message("🍽 زمان دومین وعده غذایی! (مرغ گریل شده و سبزیجات)")

def remind_meal_3():
    if is_time_correct("20:00"):
        send_message("🍽 یک ساعت تا سومین وعده غذایی شما باقی مانده است. آماده شوید! (ماهی سالمون و آووکادو)")

def meal_3_time():
    if is_time_correct("21:00"):
        send_message("🍽 زمان سومین وعده غذایی! (ماهی سالمون و آووکادو)")

# Water and coffee reminder functions
def remind_water():
    send_message("💧 لطفاً آب بنوشید و بدن خود را هیدراته نگه دارید.")

def remind_coffee():
    if is_time_correct("10:00"):
        send_message("☕️ وقت نوشیدن قهوه است!")

# Supplement reminder functions
def remind_vitamin_c():
    if is_time_correct("09:30"):
        send_message("💊 لطفاً قرص جوشان ویتامین C خود را مصرف کنید.")

def remind_magnesium():
    if is_time_correct("14:00"):
        send_message("💊 لطفاً قرص جوشان منیزیم خود را مصرف کنید.")

def remind_vitamin_d():
    if is_time_correct("19:00"):
        send_message("💊 لطفاً قرص ویتامین D خود را مصرف کنید.")

# Sleep and wake-up reminder functions
def remind_sleep():
    if is_time_correct("00:00"):
        send_message("🛌 وقت خواب است. لطفاً ساعت 12 شب بخوابید.")

def remind_wake_up():
    if is_time_correct("07:00"):
        send_message("⏰ وقت بیدار شدن است! لطفاً ساعت 7 صبح بیدار شوید.")

# Schedule reminders
schedule.every().day.at("12:00").do(remind_meal_1)
schedule.every().day.at("13:00").do(meal_1_time)
schedule.every().day.at("16:00").do(remind_meal_2)
schedule.every().day.at("17:00").do(meal_2_time)
schedule.every().day.at("20:00").do(remind_meal_3)
schedule.every().day.at("21:00").do(meal_3_time)

# Water reminders every hour
schedule.every().hour.at(":30").do(remind_water)

# Coffee and supplements reminders
schedule.every().day.at("09:30").do(remind_vitamin_c)
schedule.every().day.at("10:00").do(remind_coffee)
schedule.every().day.at("14:00").do(remind_magnesium)
schedule.every().day.at("19:00").do(remind_vitamin_d)

# Sleep and wake-up reminders
schedule.every().day.at("00:00").do(remind_sleep)
schedule.every().day.at("07:00").do(remind_wake_up)

# Main loop to run the schedule
while True:
    schedule.run_pending()
    time.sleep(1)
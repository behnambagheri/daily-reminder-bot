import os
import requests
import schedule
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables from the .env file
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
API_URL = os.getenv('API_URL')

# Function to send a message to Telegram
def send_message(message):
    url = f'{API_URL}{BOT_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=data)

# Meal reminder functions
def remind_meal_1():
    # Remind one hour before the first meal
    send_message("🍽 یک ساعت تا اولین وعده غذایی شما باقی مانده است. آماده شوید! (تخم مرغ نیمرو و بیکن)")

def meal_1_time():
    # Notify when it's time for the first meal
    send_message("🍽 زمان اولین وعده غذایی! (تخم مرغ نیمرو و بیکن)")

def remind_meal_2():
    # Remind one hour before the second meal
    send_message("🍽 یک ساعت تا دومین وعده غذایی شما باقی مانده است. آماده شوید! (مرغ گریل شده و سبزیجات)")

def meal_2_time():
    # Notify when it's time for the second meal
    send_message("🍽 زمان دومین وعده غذایی! (مرغ گریل شده و سبزیجات)")

def remind_meal_3():
    # Remind one hour before the third meal
    send_message("🍽 یک ساعت تا سومین وعده غذایی شما باقی مانده است. آماده شوید! (ماهی سالمون و آووکادو)")

def meal_3_time():
    # Notify when it's time for the third meal
    send_message("🍽 زمان سومین وعده غذایی! (ماهی سالمون و آووکادو)")

# Water and coffee reminder functions
def remind_water():
    # Remind to drink water
    send_message("💧 لطفاً آب بنوشید و بدن خود را هیدراته نگه دارید.")

def remind_coffee():
    # Remind to have coffee
    send_message("☕️ وقت نوشیدن قهوه است!")

# Supplement reminder functions
def remind_vitamin_c():
    # Remind to take Vitamin C
    send_message("💊 لطفاً قرص جوشان ویتامین C خود را مصرف کنید.")

def remind_magnesium():
    # Remind to take Magnesium
    send_message("💊 لطفاً قرص جوشان منیزیم خود را مصرف کنید.")

def remind_vitamin_d():
    # Remind to take Vitamin D
    send_message("💊 لطفاً قرص ویتامین D خود را مصرف کنید.")

# Sleep and wake-up reminder functions
def remind_sleep():
    # Remind to sleep at 12 AM
    send_message("🛌 وقت خواب است. لطفاً ساعت 12 شب بخوابید.")

def remind_wake_up():
    # Remind to wake up at 7 AM
    send_message("⏰ وقت بیدار شدن است! لطفاً ساعت 7 صبح بیدار شوید.")

# Schedule meal reminders
schedule.every().day.at("12:00").do(remind_meal_1)  # One hour before first meal
schedule.every().day.at("13:00").do(meal_1_time)    # Time for first meal
schedule.every().day.at("16:00").do(remind_meal_2)  # One hour before second meal
schedule.every().day.at("17:00").do(meal_2_time)    # Time for second meal
schedule.every().day.at("20:00").do(remind_meal_3)  # One hour before third meal
schedule.every().day.at("21:00").do(meal_3_time)    # Time for third meal

# Schedule water and coffee reminders
schedule.every().hour.at(":30").do(remind_water)    # Remind to drink water every hour
schedule.every().day.at("10:00").do(remind_coffee)  # Remind for coffee at 10 AM

# Schedule supplement reminders
schedule.every().day.at("09:30").do(remind_vitamin_c)  # Vitamin C reminder
schedule.every().day.at("14:00").do(remind_magnesium)  # Magnesium reminder
schedule.every().day.at("19:00").do(remind_vitamin_d)  # Vitamin D reminder

# Schedule sleep and wake-up reminders
schedule.every().day.at("00:00").do(remind_sleep)  # Sleep reminder at 12 AM
schedule.every().day.at("07:00").do(remind_wake_up)  # Wake-up reminder at 7 AM

# Main loop to run the schedule
while True:
    schedule.run_pending()
    time.sleep(1)
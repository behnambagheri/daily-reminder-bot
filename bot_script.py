import os
import requests
import schedule
import time
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables from the .env file
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
API_URL = os.getenv('API_URL')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to send a message to Telegram
def send_message(message):
    try:
        url = f'{API_URL}{BOT_TOKEN}/sendMessage'
        data = {'chat_id': CHAT_ID, 'text': message}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            logging.info(f"Message sent: {message}")
        else:
            logging.error(f"Failed to send message: {message}. Status code: {response.status_code}")
    except Exception as e:
        logging.error(f"Error sending message: {e}")

# Meal reminder functions
def remind_meal_1():
    logging.info("Reminding for first meal (1 hour before).")
    send_message("🍽 یک ساعت تا اولین وعده غذایی شما باقی مانده است. آماده شوید! (گوشت گاو گریل شده و سالاد اسفناج)")

def meal_1_time():
    logging.info("It's time for the first meal.")
    send_message("🍽 زمان اولین وعده غذایی! (گوشت گاو گریل شده و سالاد اسفناج)")

def remind_meal_2():
    logging.info("Reminding for second meal (1 hour before).")
    send_message("🍽 یک ساعت تا دومین وعده غذایی شما باقی مانده است. آماده شوید! (ماهی تن و سالاد کلم پیچ)")

def meal_2_time():
    logging.info("It's time for the second meal.")
    send_message("🍽 زمان دومین وعده غذایی! (ماهی تن و سالاد کلم پیچ)")

def remind_meal_3():
    logging.info("Reminding for third meal (1 hour before).")
    send_message("🍽 یک ساعت تا سومین وعده غذایی شما باقی مانده است. آماده شوید! (گوشت قرمز و کلم بروکلی بخارپز)")

def meal_3_time():
    logging.info("It's time for the third meal.")
    send_message("🍽 زمان سومین وعده غذایی! (گوشت قرمز و کلم بروکلی بخارپز)")

# Snack reminder functions
def remind_snack_1():
    logging.info("Reminding for the first snack.")
    send_message("🍴 میان‌وعده: فندق و بادام (یک مشت کوچک)")

def remind_snack_2():
    logging.info("Reminding for the second snack.")
    send_message("🍴 میان‌وعده: پنیر چدار و چند تکه تربچه")

# Water and coffee reminder functions
def remind_water():
    logging.info("Reminding to drink water.")
    send_message("💧 لطفاً آب بنوشید و بدن خود را هیدراته نگه دارید.")

def remind_coffee():
    logging.info("Reminding to have coffee.")
    send_message("☕️ وقت نوشیدن قهوه است!")

# Supplement reminder functions
def remind_vitamin_c():
    logging.info("Reminding to take Vitamin C.")
    send_message("💊 لطفاً قرص جوشان ویتامین C خود را مصرف کنید.")

def remind_magnesium():
    logging.info("Reminding to take Magnesium.")
    send_message("💊 لطفاً قرص جوشان منیزیم خود را مصرف کنید.")

def remind_vitamin_d():
    logging.info("Reminding to take Vitamin D.")
    send_message("💊 لطفاً قرص ویتامین D خود را مصرف کنید.")

# Sleep and wake-up reminder functions
def remind_sleep():
    logging.info("Reminding to go to sleep.")
    send_message("🛌 وقت خواب است. لطفاً ساعت 12 شب بخوابید.")

def remind_wake_up():
    logging.info("Reminding to wake up.")
    send_message("⏰ وقت بیدار شدن است! لطفاً ساعت 7 صبح بیدار شوید.")

# Schedule reminders for meals
schedule.every().day.at("12:00").do(remind_meal_1)
schedule.every().day.at("13:00").do(meal_1_time)
schedule.every().day.at("16:00").do(remind_meal_2)
schedule.every().day.at("17:00").do(meal_2_time)
schedule.every().day.at("20:00").do(remind_meal_3)
schedule.every().day.at("21:00").do(meal_3_time)

# Schedule reminders for snacks
schedule.every().day.at("15:30").do(remind_snack_1)
schedule.every().day.at("19:00").do(remind_snack_2)

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
logging.info("DailyReminderBot started successfully.")
while True:
    schedule.run_pending()
    time.sleep(1)
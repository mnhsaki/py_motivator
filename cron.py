from apscheduler.schedulers.background import BackgroundScheduler
from main import send_whatsapp_text,client,quote
import time
BackgroundScheduler(timezone="Asia/Dhaka")
BackgroundScheduler.start()

job = BackgroundScheduler.add_job(send_whatsapp_text,'cron',[client,quote],hour="13",minute="52")
print(job)

while True:
    time.sleep(1)                                  
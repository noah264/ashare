from flask_apscheduler import APScheduler
import time

def task1(x):
    print(f'task 1 executed --------: {x}', time.time())


def task2(x):
    print(f'task 2 executed --------: {x}', time.time())


def init_scheduler(app):
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.add_job(func=task1, args=('循环',), trigger='interval', seconds=5, id='interval_task')
    scheduler.add_job(func=task2, args=('定时任务',), trigger='cron', second='*/10', id='cron_task')
    scheduler.start()
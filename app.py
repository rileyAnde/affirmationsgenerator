from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import random

app = Flask(__name__)

def update_website():
    with open("affirmations.txt", "r") as affs:
        alist = []
        for aff in affs:
            alist.append(aff)
    taffs= random.sample(alist, 10)
    todays = open("t_affs.txt", "w")
    for i in taffs:
        todays.write(i)
    todays.close()

# create a scheduler instance
scheduler = BackgroundScheduler()
# schedule the task to run daily at 12:00 AM)
scheduler.add_job(update_website, 'cron', hour=0, minute=0)
# start the scheduler
scheduler.start()

@app.route('/')
def index():
    with open("t_affs.txt", "r") as file:
        alist = []
        for i in file:
            alist.append(i.strip())
            print(len(alist))
    return render_template("index.html", text1=alist[0], text2=alist[1], text3=alist[2], text4=alist[3], text5=alist[4], text6=alist[5], text7=alist[6], text8=alist[7], text9=alist[8], text10=alist[9])

if __name__ == '__main__':
    update_website()
    app.run(debug=True)

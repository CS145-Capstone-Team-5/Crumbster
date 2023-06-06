from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import random
from notifs import dailyNotif, overNotif, maxNotif, putNotif
from factsNtips import facts, tips
from flask_cors import CORS, cross_origin
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

app = Flask("__name__")
api = Api(app)

# Ensures that the mobile app can retrieve data from the server
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Storing the logs from Arduino
wasteLvls = {
    'curLvl': {'dataLog': "0"}
}

# Retrieval of random fun fact or tip 
class Info(Resource):
    def get(self):
        factMsg = random.choice(list(facts.values()))
        tipMsg = random.choice(list(tips.values()))
        latestLog = Log()
        return jsonify(factMsg | tipMsg | latestLog.get())
    
# Simulation of Load Sensor data retrieval
class Log(Resource):
    def get(self):
        return wasteLvls['curLvl']
    
    def put(self):
        newLog = int(request.form['dataLog'])
        oldLog = int(wasteLvls['curLvl']['dataLog'])

        if (newLog-oldLog) >= 100:
            overNotif(str(newLog-oldLog))
        elif (newLog-oldLog) > 0:
            putNotif(str(newLog-oldLog))
        if newLog >= 3000:
            maxNotif()
        
        wasteLvls['curLvl'] = {'dataLog': str(newLog)}
        return wasteLvls, 201
    
api.add_resource(Info, '/')
api.add_resource(Log, '/log')

# Sending a notification every specified interval/at a specific time daily
scheduler = BackgroundScheduler()

#trigger = CronTrigger(year="*", month="*", day="*", hour="18", minute="0", second="0")
scheduler.add_job(dailyNotif, 'interval', minutes=5)
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True)


## COMMAND TO RUN (on Windows Terminal):
#   >> python -m flask --app CrumbsterAPI run --host=192.168.68.107
#   note: replace 192.168.68.107 with IPv4 address of network from device's POV

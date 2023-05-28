from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import random
from firebase_admin import messaging 
from notifs import message
from flask_cors import CORS, cross_origin
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

app = Flask("__name__")
api = Api(app)

# Ensures that the mobile app can retrieve data from the server
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Sample Dictionary storing the fun facts and tips to be displayed
facts_tips = {
    'info1': {'fact': "The scale of the current global hunger and malnutrition crisis is enormous, with more than 345 million people facing high levels of food insecurity in 2023 - more than double the number in 2020. - WFP"},
    'info2': {'fact': "More than 900,000 people worldwide are fighting to survive in catastrophic hunger/one step away from famine. This is ten times more than five years ago, an alarmingly rapid increase. - WFP"},
    'info3': {'fact': "The climate crisis is one of the leading causes of the steep rise in global hunger. Climate shocks destroy lives, crops and livelihoods, and undermine people's ability to feed themselves. - WFP"},
    'info4': {'tip': "Preplan and write your shopping list before going to the grocery store. As you write your list, think about what meals you will be preparing the following week, and check your fridge to see what items you already have. - FDA"},
    'info5': {'tip': "When at the store, buy only what you need and stick to your shopping list. Be careful when buying in bulk, especially with items that have a limited shelf life. - FDA"},
    'info6': {'tip': "Prepared too much food for a party at your home? Pack extras in containers for guests to take home or take some over to a neighbor as a nice gesture. - FDA"}
}

# Storing the logs from Arduino
wasteLvls = {
    'curLvl': {'dataLog': "0"}
}

# Retrieval of random fun fact or tip 
class Info(Resource):
    def get(self):
        Msg = random.choice(list(facts_tips.values()))
        latestLog = Log()
        return jsonify(Msg | latestLog.get())
    
# Simulation of Load Sensor data retrieval
class Log(Resource):
    def get(self):
        return wasteLvls['curLvl']
    
    def put(self):
        request_data = request.form['dataLog']
        wasteLvls['curLvl'] = {'dataLog': request_data}
        return wasteLvls, 201
    
api.add_resource(Info, '/')
api.add_resource(Log, '/log')

def sendNotif():
    response = messaging.send(message)
    print('Successfully sent message:', response)

# Sending a notification every specified interval/at a specific time daily
scheduler = BackgroundScheduler()

trigger = CronTrigger(year="*", month="*", day="*", hour="18", minute="0", second="0")
scheduler.add_job(sendNotif, 'interval', minutes=1)
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True)


## COMMAND TO RUN (on Windows Terminal):
#   >> python -m flask --app CrumbsterAPI run --host=192.168.68.107
#   note: replace 192.168.68.107 with IPv4 address of network from device's POV

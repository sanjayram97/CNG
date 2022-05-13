from flask import Flask, render_template, request, session, redirect, url_for
import time
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', daily_petrol_consumption = '',
                                         daily_petrol_expense = '',
                                         daily_vehicle_running = '',
                                         mileage = '',
                                         petrol_cost_pl = '',
                                         cng_cost_pl = '',
                                         cng_mileage = '',
                                         daily_cng_consumption = '',
                                         cng_expense = '',
                                         daily_fuel_saving = '')
    daily_vehicle_running = request.form.get('daily_vehicle_running')
    mileage = request.form.get('mileage')

    print('-----')
    print(daily_vehicle_running, mileage)
    print('-----')

    daily_petrol_consumption = float(daily_vehicle_running) / float(mileage)

    petrol_cost_pl = request.form.get('petrol_cost_pl')

    daily_petrol_expense = float(daily_petrol_consumption) * float(petrol_cost_pl)
    cng_cost_pl = request.form.get('cng_cost_pl')

    cng_mileage = 0.0600000000000005 + (1.632 * float(mileage))
    daily_cng_consumption = float(daily_vehicle_running) / float(cng_mileage)
    cng_expense = daily_cng_consumption * float(cng_cost_pl)

    daily_fuel_saving = daily_petrol_expense - cng_expense
    
    return render_template('index.html', daily_petrol_consumption = round(float(daily_petrol_consumption),2),
                                         daily_petrol_expense = round(float(daily_petrol_expense),2),
                                         daily_vehicle_running = round(float(daily_vehicle_running),2),
                                         mileage = round(float(mileage),2),
                                         petrol_cost_pl = round(float(petrol_cost_pl),2),
                                         cng_cost_pl = round(float(cng_cost_pl),2),
                                         cng_mileage = round(float(cng_mileage),2),
                                         daily_cng_consumption = round(float(daily_cng_consumption),2),
                                         cng_expense = round(float(cng_expense),2),
                                         daily_fuel_saving = round(float(daily_fuel_saving),2))



if __name__ == "__main__":
    app.run(debug=True, port=5001)
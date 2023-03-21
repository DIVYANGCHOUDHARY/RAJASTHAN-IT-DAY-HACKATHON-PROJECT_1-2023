from flask import Flask, render_template
import os
from flask import Flask, jsonify
import subprocess
import hack
import win32com.client

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/specs')
def specs():
   return render_template("specs.html")

# @app.route('/drivers')
# def drivers():
#     drivers = os.listdir('/lib/modules')
#     return jsonify(drivers)

# @app.route('/data')
# def data():
#   exec(hack)
  
#   with open('data.txt', 'r') as f:
#     content = f.read()
#     return render_template('specs.html', content=content)

@app.route('/system_drivers')
def system_drivers():
    wmi = win32com.client.GetObject('winmgmts:')
    drivers = wmi.ExecQuery('SELECT * FROM Win32_SystemDriver')

    driver_list = []
    for driver in drivers:
        driver_dict = {}
        driver_dict['Name'] = driver.Name
        driver_dict['Description'] = driver.Description
        driver_dict['PathName'] = driver.PathName
        driver_dict['State'] = driver.State
        driver_dict['Status'] = driver.Status
        driver_list.append(driver_dict)

    return render_template('specs.html', drivers=driver_list)

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
  app.run(debug=True)
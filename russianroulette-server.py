import json
import random

# import flask web microframework
from flask import Flask
from flask import request
from flask import abort

# import from the 21 Developer Library
from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)



def cat(filepath):
    with open(filepath, 'r') as file:
        return file.readline()


def spin_the_cylinder():
    revolver = [
        "/etc/wpa_supplicant/wpa_supplicant.conf",
        "/etc/wpa_supplicant/ifupdown.sh",
        "/etc/wpa_supplicant/functions.sh",
        "/etc/wpa_supplicant/action_wpa.sh",
        "/etc/wpa_supplicant/ifupdown.sh",
        "/etc/gai.conf",
        ".russianroulette-server.py",
        ".russianroulette-server.py",
        ".russianroulette-server.py",
        ".russianroulette-server.py"
    ]

    bullet = random.randint(0,len(revolver))
    muzzle = cat(revolver[bullet])
    return muzzle


# endpoint to get a value from the server
@app.route('/pull_the_trigger')
@payment.required(1313)
def pull_the_trigger():

    pull_the_trigger = spin_the_cylinder()

    if pull_the_trigger is None:
        abort(500)

    return pull_the_trigger


@app.route('/')
def get_info():
    info_obj = {
	"name": "russian roulette",
    "description":"I can lose my wifi ssid and password",
	"version": 100,
        "pricing": {
            "/" : {
                "minimum" : 1313
            },
        }

    }
    return json.dumps(info_obj)

if __name__ == '__main__':
    print ("pick up the gun... ")
    app.run(host='0.0.0.0', port=13013, debug=True)


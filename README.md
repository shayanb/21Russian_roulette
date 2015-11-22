
[Russian Roulette](https://en.wikipedia.org/wiki/Russian_roulette)
============================

Summary:  Randomly sends a file from the server file system, one of which is wifi config file (/etc/wpa_supplicant/wpa_supplicant.conf) which contains SSID and the PASSWORD


Running the server
------------------

	$ python3 russianroulette-server.py



API;

1. Get info
--------------

HTTP URI: /

Params: None

Result:

	{
	    "description": "I can lose my wifi ssid and password",
	    "name": "Russian Roulette",
	    "pricing": {
	        "/shoot": {
	            "minimum": 1313
	        }
	    },
	    "version": 101
	}

Pricing:

	Free


2. Pull the Trigger
--------------

HTTP URI: /shoot

Params: None

Result:

	Content of the chosen file

Pricing:

	1313


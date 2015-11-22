
[Russian Roulette](https://en.wikipedia.org/wiki/Russian_roulette)
============================

Summary:  Randomly sends a file from the server file system, one of which is wifi config file (/etc/wpa_supplicant/wpa_supplicant.conf) which contains SSID and the PASSWORD


Running the server
------------------

	$ python3 russianroulette-server.py


Running the clinet (Joining the party)
-------------------

	wget https://goo.gl/2cEQ1e -O russianroulette-client.py ; python3 russianroulette-client.py shoot


API;

1. Get info
--------------

HTTP URI: /

Params: None

Result:

	  |^\                      _________________/\_
	 |~~~|--------------~~~~~~~~~~~~~~~~,xx.~~~~~~~~\
	|___|-------++++==|___|~~~~~|_____(x@x),;'//  ||
	                  |~~~||    |~~~~~~~~~~~ //   ||
	                   ~\(_(=)~~ ,-~-\       \  __/
	                      ~~~~~\[  \ ]\       \/
	                            `:  |'()       \
	                              ~~~~\ \       \
	                                   \ \       \
	                                    \ \       \
	                                     \ \       \
	                                      \ \       ||
	                                       | \       ||
	                                       |  \_  ___||
	                                       \____( )-=~
																				 
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

	[Content of the chosen file]

Pricing:

	1313


TODO:
-----
* add more random stuff
* reboot the machine if shot?
* reboot the client if shot?

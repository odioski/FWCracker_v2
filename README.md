# FWCracker

This script will attempt to guess at your password using most laymens favorited of password paradigms, ie., abc123. It's handy if you often use such passwords 
with firmware locks on your devices.

*There are three things you'll need other than what you probably already have those being a Python interpreter and an IDE:*

	1. A HID recognizable Keyboard/emulator, preferably one which can send and recieve RS-232. These can be found easily online, but so far I've only found retailers overseas.
	2. A USB to TTL cable to connect to the emulator. These are more easily found here.
 	3. A module called PySerial which can be had from PyPi.org via pip.
	
*You can visit the following link to see what the hid/emulator looks like:* https://tinyurl.com/5xe4n4mn

I've considered expanding it to include user input (hints) and possibly some randomization with the hopes of making it faster.
That's why it's there on Github.
 
I'm sure you realize that most modern hardware has some kind of lockout enabled after mutltiple failed attempts. For some instances this will still work fine,
mostly for older hardware and of course some of the relics are more than accessible. If the password is simple and if it is indeed a 
firmware lock you're trying to bypass or a boot-up lock. Against an OS, I imagine you'll only have success with the most ancient of systems.

And, if you haven't realized, hints or some idea of what the password is, is actually neccessary for this to work. This is why future versions will
query for hints, in order to help the app guess the right combination. Therefore, this application wouldn't be of much use to the Black Hat market, but owners 
of the gear, and some repair personnel could gain some use from it. Some Black Hat's could possibly use this, but those are the truly embedded (practiced) ones.

Lastly, Brute-force makes an attempt for every possible combination of characters used in the suspected password. It takes more or less the same amount of code to write such, 
however more complex, but due to the speed of CMOS or BIOS in general, it would take infinitly longer to complete. For the most part they're fire and forget 
but they're also *notoriously slow*. This approach requires a little detective work before deploying, so, with a lttle info and a ton of luck results can 
possibly be gained faster. 

I think you can see the idea clearly and what my hopes are for this app. I'll continue to develop it, and branch off to create something more user friendly. 
I haven't gotten into GUI development yet but if I find a good source on the subject I'll gladly add that in.

# INSTALLATION
	
Clone from Github using git: 
	
	git clone https://github.com/odioski/FWCracker_v2.git
	
Navigate to the /src folder and use pip to get PySerial: 
	
	pip install pyserial

Launch FWCracker:
	
	python FWCracker.py

Another option, is to use the PyInstaller created executable.

Navigate to /dist folder. Inside is FWCracker.exe


# SUPPORT

If FWCracker can't find *pyserial-ports* you'll have to add it to your *PATH*.

You should launch FWCracker from the safety of your venv. You should also install pyserial from the root of your venv. 
If FWCracker still can't find pyserial-ports then you'll most likely need to add it to your *PATH*.

You can find it on linux as su:

	find / -name pyserial-ports

This will add whatever *find* returns to your *PATH*: 

	find / -name pyserial-ports -exec echo -e ":{}\n" >> $PATH \;
 
That's the fastest way. You can also just fix your venv.

	python -m venv path/to/your/venv

cd to your venv, and run all commands from there. Or use the provided python and pip in your bin in the venv.

Something like:

	venv/bin/pip install pyserial

 or 
 
	bin/python ../FWCracker.py

 

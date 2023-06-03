####################################################################################################################################################################
##
##  MARCH 2023
##
##  This is version 2 of FWCracker, with one major update. Instead of using constants (the word patterns) we'll ask the user for input.
##  I imagine this will amount to the same amount of code but at least the end-user won't have to know python or any coding to use it. For more info about
##  FWCracker in general view the README.
##
##  The original code for FWCracker is below this code in a block comment. Select it all, copy and paste to a new *.py file and uncomment and it should work.
##  As I mentioned in the code and elsewhere I believe there is some timing issue with macs's or they don't recognize the emulator's I use. So, that's all for that.
##  
##  If you need something to bypass a Window's Machine or PC, this will work for you just fine, for now. I'll be updating continuously although sporadically and not
##  very often. Just tidying up the user interface and making things a bit more friendly. The essential logic of the code and operatability is pretty much done. After I
##  read up on how to package this properly for any user, that will probably be all for this. 
##
##  So, enjoy.
##
##
##  UPDATE 5/2/23
##
##  After furhter investigation I learned that the mac I was using for testing was compromised. Thus the perceived timing or keyboard communication issue. I began to suspect
##  that having two keyboards plugged in (one of them being the emulator) was the issue, but after some thought I realized no keyboard is actually needed in the 
##  first stage of a boot lock, since the point is to keep one from accessing any of the system until the password is given. So, either my firmware was corrupted or 
##  the POST is built wrong. There should be no way to enter Cmd-Option-R to access either the firmware or the recovery system without first passing the check, 
##  from the firmware/boot lock. 
##
##  Because that's what a firmware/boot lock is supposed to do. That's the layer of protection it provides given it's operating normally.
##
##  Therefore, there is no issue with the macs, and you can use this app equally on both PC and Apple end-user workstation platforms.
####################################################################################################################################################################


import time

import serial

import subprocess


code = "pyserial-ports -v"
#   Just in case someone needs it...


def welcome_user():
    print("\n\nWelcome to FWCracker 2 \n")
    time.sleep(2)
    input("The following questions will clue me in to what your password could possibly be. This app can only help you if you give me a hint. \n"
            "The passwords we can crack are simple passwords. In other words, abc123. Anything more complex and there isn't much we can do that won't take a lifetime to process. \n"
            "Of course if you're feeling adventurous, a raw brute-force mode is currently being formulated.\n\n"
            "Press 'Enter' to continue...")
    find_port()    
    get_hints()



def find_port():
    print("\nThis is probably the stickiest question so I'll start here. Which port is you emulator connected to?\n"
            "\nHere's what I found \n")
    time.sleep(2)
    subprocess.run(code)
    time.sleep(1)
    hid_port = input("\nType the name of the port your device is using. Should be something like /dev/tty/USB# or COM#... ")
    print("\nYou're device is set: " + hid_port + "\n")
    return hid_port




def get_hints():
    print("While answering these questions, try to keep the numbers and words seperate...")
    some_word = input("\nType in the word or phrase you think is part of the password, then press enter: ")
    number_pattern = input("\nType in the part of the password which you believe is a number. Your best guess really is suitable: ")
    z = -1
    while z <= 0:
        check = number_pattern
        global_number_pattern = number_pattern
        while check.isdecimal() == False:
            number_pattern = input("\nThis app will only attempt at simple passwords, ie., abc123 "
            "if there is no number as part of the sequence, this won't help \n"
            "Please enter a number here or Q to exit: ")
            check = number_pattern
        if check.isdecimal():
            control =input("\nDoes your BIOS require re-confirmation on failed attempts? Y or N:")
            print("\nGot it...\n")
            time.sleep(4)
            print("We'll begin in just a few seconds. Make sure you keep the power on or you'll have to start over... \n")
            time.sleep(5)
            print("Here we go...\n")
            time.sleep(3)
            z = 1
            build_range(global_number_pattern, some_word, control)
        elif number_pattern == 'Q':
            print("Goodbye...")
            exit()
        elif number_pattern == 'q':
            print("Goodbye...")
            exit()        
        

def build_range(global_number_pattern, some_word, control):
    known_factor = int(global_number_pattern) / 10
    keep = ""
    if known_factor <= 1:
        o_range = 10
        print("10 different possibilities based on this info...\n")
        keep = 'Y'
    else:
        if known_factor <= 10:
            o_range = 100
            print("100 different possiblities based on this info...\n")
            keep = 'Y'
        else:
            if known_factor <= 100:
                o_range = 1000
                print("1,000 different possiblities based on this info...\n")
                keep = 'Y'
            else:
                if known_factor <= 1000:
                    o_range = 10000
                    print("10,000 different possiblities based on this info...\n")
                    keep = 'Y'
    set_range = o_range
    starter(global_number_pattern, keep, some_word, control, set_range)
    while o_range >= 10001:
        o_range = 100000
        print("Based on the number you provided this will take a very long time.\n")
        keep = 'Y'
    set_range = o_range
    starter(global_number_pattern, keep, some_word, control, set_range)
    while o_range >= 100001:
        o_range = 1000000
        keep = input("Practically impossible, theoretically....Shall we continue? "
        "Y or N: ")
    set_range = o_range
    starter(global_number_pattern, keep, some_word, control, set_range)
    while o_range >= 1000001:
        o_range = 1000000
        keep = input("Last chance...\n"
        "Y or N: ")
    set_range = o_range
    time.sleep(3)
    starter(global_number_pattern, keep, some_word, control, set_range)



def starter(global_number_pattern, keep, some_word, control, set_range):
    if str(keep) == 'y':
        build_passcode(some_word, control,  set_range)
    elif str(keep) == 'Y':
        build_passcode(some_word, control, set_range)
    elif str(keep) == 'yes':
        build_passcode(some_word, control, set_range)
    elif str(keep) == 'YES':
        build_passcode(some_word, control, set_range)
    elif str(keep) == 'Yes':
        build_passcode(some_word, control, set_range)
    elif str(keep) == 'n':
        print("Goodbye...")
    elif str(keep) == 'N':
        print("Goodbye...")
    elif str(keep) == 'no':
        print("Goodbye...")
    elif str(keep) == 'No':
        print("Goodbye...")
    elif str(keep) == 'NO':
        print("Goodbye...")
    else:
        print("..::Music::..")
        exit()
    time.sleep(3)
        


def build_passcode(some_word, control, set_range):
    n = 1
    while n <= set_range:
        passcode = some_word + str(n)
        to_bytes = passcode.encode(encoding='ascii')
        do_writer_do(to_bytes, n, passcode, control, set_range)
        n += 1
    print("Later...")
    exit()


def do_writer_do(to_bytes, n, passcode, control, set_range):
    print("This is attempt #" + str(n) + " of " + str(set_range) + ", using this password: " + passcode)
    time.sleep(1)
#   The mac issue was resolved 5/2/23, I'll release my personal notes maybe if it proves profitable. 
#   Basically, a long delay is no longer necessary and the app works on PC's and Mac's equally.
#   Therefore, only a 2-3 second delay is ever needed. With new hardware, we may be able to 
#   eliminate it altogehter.
    ser = serial.Serial(hid_port)
    ser.baudrate = 9600
#   PySerial and part of the setup...
    ser.write(to_bytes)
    time.sleep(1)
    if str(control) == 'y':
        ser.write("\n")
    elif str(control) == 'Y':
        ser.write("\n")
    elif str(control) == 'yes':
        ser.write("\n")
    elif str(control) == 'Yes':
        ser.write("\n")
    elif str(control) == 'YES':
        ser.write("\n")
    int(n)
    int(set_range)
    time.sleep(2)


welcome_user()

##  And there you are...


###################################################################################################################################################################################
##
##  THE ORIGINAL FWCracker.............
##
###################################################################################################################################################################################
##   This script will attempt to guess at your password using most laymens favorited of password paradignms, ie., abc123. It's handy if you often use such passwords 
##   with firmware locks on your devices. Most have long since stoped using these particular patterns but if you change the constants to suite your needs, 
##   it should work just fine.
##
##   There are three things you'll need other than what you probably already have those being a Python interpreter and an IDE:
##
##   -- A HID recognizable Keyboard/emulator, preferably one which can send and recieve RS-232. These can be found easily online, but so far I've only found retailers overseas.
##   -- A USB to TTL cable to talk to the emulator. These are more easily found here.
##   -- A module called PySerial which can be had from PyPi.org via pip
##
##   I've considered expanding it to include user input (hints) and possibly some randomization with the hopes of making it faster.
##   That's why it's there on Github.
##  
##   I'm sure you realize that most modern hardware has some kind of lockout enabled after mutltiple failed attempts. For some instances this will still work fine,
##   mostly for older hardware and of course some of the relics are more than accessible. If the password is simple and if it is indeed a 
##   firmware lock you're trying to bypass or a boot-up lock. Against an OS, I imagine you'll only have success with the most ancient of systems.
##
##   And, if you haven't realized, hints or some idea of what the password is, is actually neccessary for this to work. This is why future versions will
##   queery for hints, in order to help the app guess the right combination. Therefore, this application wouldn't be of much use to the Black Hat market, but owners 
##   of the gear, and some repair personnel could gain some use from it. Some Black Hat's could possibly use this, but those are the truly embedded (practiced) ones.
##
##   Lastly, Brute-force makes an attempt for every possible combination of characters used in the suspected password. It takes more or less the same amount of code to write such, 
##   however more complex, but due to the speed of CMOS or BIOS in general, it would take infinitly longer to complete. For the most part they're fire and forget 
##   but they're also notoriously slow. This approach requires a little detective work before deploying, so, with a lttle info and a ton of luck results can 
##   possibly be gained faster. 
##
##   I think you can see the idea clearly now and what my hopes are for this app. I'll continue to develop it, and branch off to create something more user friendly. 
##   I haven't gotten into gui development yet but if I find a good source on the subject I'll gladly add that in.
##
#################################################################################################################################################################################
#


""" import time
#   although we really love Mac's they can be a little janky...need to slow down the transmissions to some degree.
import subprocess
#   this is to run a line of code which might aide the eu.
import serial
#   and this piece is the real magic behind the script.


Word1 = "Xbox"
Word2 = "xbox"
Word3 = "XBOX"
Word4 = "xBOX"
#
#   These were my favorite words for simple passwords like firmware passwords. As you can see, bruteforce is hard to do.
#   I don't use any of these with my devices anymore so don't feel suspect for reading this...
#   You can and should change the constants to your own word patterns or add more or less if needed.
#
Word5 = "App"
Word6 = "app"
Word7 = "APP"
Word8 = "aPP"
#
#
#


code = "pyserial-ports -v"
#   The little helper I mentioned earlier...

global counter
global attempts

counter = 0
attempts = 0

#   Counters,



def status(attempts):
    print("\n So far, you've made " + str(attempts) + " attempts to penetrate this machine...and counting.\n")
#   A bit of joke, since this will take a while, it's ok to get a little comfortable.


def pass_guesser(counter, attempts):
    #   The attempts.
    n = 0
    while n <= 9999:                         ##############################################################
        #   Trying for Xbox...                                                                          #            This loop can be and is iterated for each suspected
        counter += 1    #   Titan                                                                       #            word pattern. As far as the part of the combo which
        WordPattrn = Word1                                                                              #            includes numbers, use 'the imagined largest factor 
        passcode = WordPattrn + str(n) + "\r"                                                     ###############    of those combined digits real number'~Boris
        print("\n This is attempt # " + str(counter) + " in this sequence..." + str(passcode))      ###########      So if you suspect the number is 4195, maybe, then count 
        do_writer_do(passcode, ser, clear)                                                              #            to 5000. If you think it's 332 then count to 400 or
        n += 1                                                                                          #            maybe 350, etc... This is why adding some radomization 
        #                                                                                               #            could speed things up. Once user input is added, we can
    n = 1                                                  ###############################################           replace these loops for ones which are more tailored
    int(counter)                                                                                        #            and can then condense some things.
    int(attempts)
    #   Oddly enough, the variables need to be converted back to integers every iteration. 
    #   I may be missing something but I thought a variable's type was determined by it's usage or how it's referenced, here in python.
    attempts += counter
    #   You have to keep a record outside of the loop to count precisely. This precept escaped me for many years.
    #   If you think about it, you can't add or take from a loop, something that's already cycling without stopping the cycle or waiting for it to end, right?
    status(attempts)
    counter = 0
    while n <= 9999:
        #   Trying for xbox
        WordPattrn = Word2
        passcode = WordPattrn + str(n) + "\r"
        print("\n This is attempt # " + str(counter) + " in this sequence..." + str(passcode))
        do_writer_do(passcode, ser, clear)
        n += 1
        counter += 1
    n = 1
    int(counter)
    int(attempts)
    attempts += counter
    counter = 0
    status(attempts)
    while n <= 9999:
        #   Trying for XBOX...
        WordPattrn = Word3
        passcode = WordPattrn + str(n) + "\r"
        print("\n This is attempt # " + str(counter) + " in this sequence..." + str(passcode))
        do_writer_do(passcode, ser, clear)
        n += 1
        counter += 1
    n = 1
    int(counter)
    int(attempts)
    attempts += counter
    counter = 0
    status(attempts)
    while n <= 9999:
        # Trying for xBOX...
        WordPattrn = Word4
        passcode = WordPattrn + str(n) + "\r"
        print("\n This is attempt # " + str(counter) + " in this sequence..." + str(passcode))
        do_writer_do(passcode, ser, clear)
        n += 1
        counter += 1
    n = 1
    int(counter)
    int(attempts)
    attempts += counter
    counter = 0
    status(attempts)
    while n <= 9999:
        #   Trying for App...
        WordPattrn = Word5
        passcode = WordPattrn + str(n) + "\r"
        print("\n This is attempt # " + str(counter) + " in this sequence..." + str(passcode))
        do_writer_do(passcode, ser, clear)
        n += 1
        counter += 1
    n = 1
    int(counter)
    int(attempts)
    attempts += counter
    counter = 0
    status(attempts)
    while n <= 9999:
        #   Trying for app...
        WordPattrn = Word6
        passcode = WordPattrn + str(n) + "\r"
        print("\n This is attempt # " + str(counter) + " in this sequence..." + str(passcode))
        do_writer_do(passcode, ser, clear)
        n += 1
        counter += 1
    n = 1
    int(counter)
    int(attempts)
    attempts += counter
    counter = 0
    status(attempts)
    while n <= 9999:
        #   Trying for APP...
        WordPattrn = Word7
        passcode = WordPattrn + str(n) + "\r"
        print("\n This is attempt # " + str(counter) + " in this sequence..." + str(passcode))
        do_writer_do(passcode, ser, clear)
        n += 1
        counter += 1
    n = 1
    int(counter)
    int(attempts)
    attempts += counter
    counter = 0
    status(attempts)
    while n <= 9999:
        #   Trying for aPP...
        WordPattrn = Word8
        passcode = WordPattrn + str(n) + "\r"
        print("\n This is attempt # " + str(counter) + " in this sequence..." + str(passcode))
        do_writer_do(passcode, ser, clear)
        n += 1
        counter += 1
    n = 1
    int(counter)
    int(attempts)
    attempts += counter
    counter = 0
    status(attempts)



def do_writer_do(passcode, ser, clear):
    #   The writer...
    print(ser.name + " " + str(passcode) + " " + str(clear))
    to_bytes = passcode.encode(encoding='ascii')
    #   Your emulator will most likely convert 'ascii' to the corresponding keycodes.
    ser.write(to_bytes)
    print("\n")
    time.sleep(13)
#
#   This is PySerial from serial and is how this app sends/writes to the emulator. Visit this site to learn more: https://pyserial.readthedocs.io/en/latest/index.html
#   I haven't found out what's up with this yet. No where near that amount of time is needed on other systems. Just the mac.
#   Still searching for a concise source on the innerworkings of keyboards. I suspect there's a control byte sent or recieved which can help things along.
#   Until google finds it, this will suffice. 
#   
#   It's dangerous to try and read with this device since you could permanently lock the port if things don't sync correctly.
#   Thus damaging or destroying the device. So, some knowledge of keyboard communications is neccessary before moving forward.
#
#   I've only encountered this issue with the mac. Other systems respond normally and only a second or two is neccessary between transmissions.

subprocess.run(code)
#   This is as dangerous as it's known to be, however this tool is meant for offline use.
#   Plus, in this scenario there's no advanced system or OS present, only the BIOS and CMOS are encountered.
#   Not sure how one would exploit it from this vantage point, or why, or if one could possibly profit.


hid_port = input("Enter your emulator's serial port: ")
ser = serial.Serial(hid_port)
clear = ser.is_open
print("Your emulator's serial port is " + hid_port + " " + str(clear))
time.sleep(1)
#   User input, it's good when you can get it.

ser.baudrate = 9600
# PySerial as well, neccesary protocols for this app and your device.

pass_guesser(counter, attempts)
#   Anyway, here you go...










   




 """

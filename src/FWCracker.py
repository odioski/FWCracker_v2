import time
#   Needed for flow control

import serial
# Needed for PySerial

import subprocess
# Needed to run the helper code


code = "pyserial-ports -v"
#   Just in case someone needs it...


def FWCracker():
    def find_port():
        global ser 
        global hid_port
        print("\nThis is probably the stickiest question. Which port is you emulator connected to?\n"
                "\nHere's what I found \n")
        time.sleep(5)
        subprocess.run(code)
        time.sleep(5)
        hid_port = input("\nType the name of the port your device is using. Should be something like /dev/tty/USB# or COM#... ")
        print("\nYou're device is set: " + hid_port + "\n")
        ser = serial.Serial(hid_port)
        ser.baudrate = 9600
        #   PySerial and part of the setup...

        
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
                find_port()
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

    def welcome_user():
        print("\n\nWelcome to FWCracker 2 \n")
        time.sleep(2)
        input("The following questions will clue me in to what your password could possibly be. This app can only help you if you give me a hint. \n\n"
                "The passwords we can crack are simple passwords. In other words, abc123. Anything more complex and there isn't much we can do that won't take a lifetime to process. \n\n"
                "Of course if you're feeling adventurous, a raw brute-force mode is currently being formulated.\n\n"
                "Press 'Enter' to continue...")
        get_hints()
    
    
    welcome_user()


FWCracker()


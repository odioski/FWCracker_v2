MARCH 2023

This is version 2 of FWCracker, with one major update. Instead of using constants (the word patterns) we'll ask the user for input.
I imagine this will amount to the same amount of code but at least the end-user won't have to know python or any coding to use it. For more info about
FWCracker in general view the README.

The original code for FWCracker is below this code in a block comment. Select it all, copy and paste to a new *.py file and uncomment and it should work.
As I mentioned in the code and elsewhere I believe there is some timining issue with macs's or they don't recognize the emulator's I use. So, that's all for that.
  
If you need something to bypass a Window's Machine or PC, this will work for you just fine, for now. I'll be updating continuously although sporadically and not
very often. Just tidying up the user interface and making things a bit more friendly. The essential logic of the code and operatability is pretty much done. After I
read up on how to package this properly for any user, that will probably be all for this and python. Unfortunately the hater's are in a frenzy trying once again to
disavow all that I do. Such is normal operating procedure and not much of a surprise, although I do admit I was hoping for something a little more original.
Perhaps a 'thank-you' or an 'I appreciate it'. Simple courtesy, that's all.

So, enjoy.


UPDATE 5/2/23

After furhter investigation I learned that the mac I was using for testing was compromised. Thus the perceived timing or keyboard communication issue. I began to suspect
that having two keyboards plugged in (one of them being the emulator) was the issue, but after some thought I realized no keyboard is actually needed in the 
first stage of a boot lock, since the point is to keep one from accessing any of the system until the password is given. So, either my firmware was corrupted or Apple had their 
heads up their asses when they built the POST. There should be no way to enter Cmd-Option-R to access either the firmware or the recovery system without first passing the check,
from the firmware/boot lock. Because that's what a firmware/boot lock is supposed to do. That is the layer of protection it provides given it's operating normally.

Therefore, there is no issue with the macs, and you can use this app equally on both PC and Apple end-user workstation platforms.

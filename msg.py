#Import required modules
import colorama
#importuje time'a
import time
#biblioteki z coloramy
from colorama import Fore, Back, Style
#importuje os'a
import os

#importuje cos tam jeszcze
colorama.init(autoreset=True)

clear = lambda: os.system('cls')

clear()

print (Fore.GREEN + "Uruchamianie sekwencji mero.py")
time.sleep(3)

print (Fore.CYAN + "10%")
time.sleep(3)
print (Fore.CYAN + "24%")
time.sleep(4)
print (Fore.CYAN + "36%")
time.sleep(2)
print (Fore.CYAN + "52%")
time.sleep(10)
print (Fore.RED + "Error in line 0, can't define Colorama")
time.sleep(2)


print (Fore.RED + "Uruchamianie zakończone niepowodzeniem, odnawianie")

time.sleep(7)

clear()
print (Fore.RED + "Ponawianie.")


time.sleep(3)

clear()

print (Fore.RED + "Ponawianie..")

time.sleep(3)

clear()

print (Fore.RED + "Ponawianie...")

time.sleep(3)

clear()

time.sleep(1)

print (Fore.RED + "Błąd, mero nie ma funkcji określonej w linijce 4 podpisanej jako: mozg")

time.sleep(4)
#czysci konsole
clear()

quit(0)
blue="\033[0;34m"         # Blue
red="\033[0;31m"          # Red
white="\033[0;37m"        # White
yellow="\033[0;33m"       # Yellow
green="\033[0;32m"        # Green
cyan="\033[0;36m"         # Cyan
color_off="\033[0m"       # Text Reset
line=yellow+"========================================================================================================================\n\n\t\t"
logo=red+str(""" _____ ___  ___  __   __  ______  _____ ______  _____ 
|_   _||  \/  |  \ \ / /  |  ___||_   _|| ___ \|  ___|
  | |  | .  . |   \ V /   | |_     | |  | |_/ /| |__  
  | |  | |\/| |   /   \   |  _|    | |  |    / |  __| 
  | |  | |  | |  / /^\ \  | |     _| |_ | |\ \ | |___ 
  \_/  \_|  |_/  \/   \/  \_|     \___/ \_| \_|\____/ 
                                                      
                                                      
""")

header=logo+cyan+"\n\n\t\tDevloped By : TR TAHIDUL RAJ\n\n"

print(header+line)

year=int(input("ENTER THE YEAR:"))

if year%4==0:
	print("\n\n\t\tTHIS IS A LEAP YEAR\t\t")
else:
	print("\n\n\t\tTHIS IS NOT A LEAP YEAR\n\n\t\t")
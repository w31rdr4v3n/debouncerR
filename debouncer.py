import requests
from os.path import isfile
from sys import argv

####################### VARIABLE ##############################
API_KEY = 'PUT HERE API KEY'
red="\033[1;31m"
gris="\033[1;30m"
green="\033[1;32m"
magenta="\033[1;35m"
transparent="\033[0m"


####################### ARGS ###################################
try:
	FILE = argv[1]
except IndexError:
	print("Usage: python3 debouncer.py [path]")
	exit(0)

####################### DEBOUNCER ##############################

def getDebounce(pin):
	response = requests.get("https://api.debounce.io/v1/", params={'api':API_KEY, 'email':pin.strip()}, headers={"Accept": "application/json"})
	debounce = response.json()["debounce"]
	if debounce['reason'] == 'Deliverable':
		print(f"{green}[+]{transparent} Email: {gris}{debounce['email']}{transparent} | Result: {green}{debounce['result']} - {debounce['reason']}{transparent}")
	else:
		print(f"{red}[-]{transparent} Email: {magenta}{debounce['email']}{transparent} | Result: {red}{debounce['result']} - {debounce['reason']}{transparent}")

	

####################### SINGLE EMAIL ##########################

if not isfile(FILE):
	getDebounce(FILE)
	exit(0)


########################## EMAIL FROM FILE ####################
with open(FILE) as file:
	for pin in file:
		getDebounce(pin)
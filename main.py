import time
from subprocess import call

print(" ______ _______  _____   _        _____  ")
print("|  ___| | |_| | |  ___| | |      |  ___| ")
print("| |___  |  _  | | |     | |      | |___  ")
print("|  ___| | | | | | |     | |      |  ___| ")
print("| |___  | | | | | |__|| | |____  | |___  ")
print("|_____| |_| |_| |_____| |______| |_____| ")

print("\nLoading")
print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("...")
time.sleep(1)
print("....")
print(".....")
time.sleep(2)
print("System succesfully started.")

print("\nWelcome to Eagle OS 2.2!\n\n")

# Laat login systeem runnen
# -------------------------

def open_py_file():
    call(["python", "Database/login.py"])

open_py_file()

# -------------------------

print("\nTest\n")

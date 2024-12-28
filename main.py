import win32api
import os
import string
import argparse

modes = ["Express", "Presets", "Advanced", "Training Mode"]

def getDrive():
    available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    print(available_drives)
    selectedDrive = input("Select the drive you would like to install MKDD to (use a number):")
    selectedDriveInt = int(selectedDrive)

    print("You have selected drive " + str(selectedDriveInt) + ", the " + str(available_drives[selectedDriveInt - 1]) + " drive.")
def selectMode():
    userMode = input("Select mode:\n1. Express\n2. Presets\n3. Advanced\n4. Training Mode")
    print("You have selected")
def expressMain():
    # will copy default files to flashdrive, Formula4o4 preset
def presetsMain():
    # will display a list of presets the user can choose from for different established rulesets
def advancedMain():
    # will tell the user to open the instructions in the 'Advanced' folder and press continue, then continues the process
def trainingMode():
    # will install training mode configuration onto the drive

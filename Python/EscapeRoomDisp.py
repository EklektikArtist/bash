
#============================================
# author: Micah Richards
# date: 10/4/17
# class: Library Work
#
# purpose: Display victory message on proper USB insertion
# input:  - USB
#         - 
# output: - Victory Splash Screen
#	  - 
#
#============================================

# imports
import pyudev, time, os

# define global constants and Booleans
context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')
passfile = open('passwords.txt', 'r')
password = passfile.readline().strip()
print ('The password is: %s' % password)
cont = False

# define functions
def pollfordrive():
    for device in iter(monitor.poll, None):
        if device.action =='add':
#	    print('You have plugged a device into the computer')
#            print('{} connected'.format(device))
	    return 1
        if device.action =='remove':
#	    print('You have unplugged a device from the computer')
#            print('{} disconnected'.format(device))
	    return 0

def calctdiff(Stt, Fnt):
    return (Fnt-Stt)/60.0

def donoth():
    print ('')
# ===== Main Program =====
while(True):
    ignvar = os.system ('clear')
    raw_input('Press enter to continue...')
    startTime=time.time()
    while (cont == False):
        enteredpass = raw_input('Please enter the password: ')
	print ('You entered: %s' % enteredpass)
        if (enteredpass == password):
            print ('That is the correct password!')
            cont = True
        else:
            print ('That is not the correct password')

    print ('Please insert the flashdrive with the file')
    while (pollfordrive() != 1):
        donoth()
    print ('You did it!')
    print ('It took you %f minutes to complete this!' % calctdiff(startTime, time.time()))
    while (pollfordrive() != 0):
        donoth()
    print ('Resetting System...')
    time.sleep(1)

# End of Program
print ('\n-----End of Program-----\n')

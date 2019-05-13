#!/usr/bin/env python3
##Create a dictionary
switch = {'hostname' : 'sw1', 'ip' : '10.0.0.1', 'version' : '1.2', 'vendor' : 'cisco'}

##display parts of the dictionary
print( switch ['hostname'])
print ( switch['ip'])

##Requests a 'fake' key
#print( switch['lynx'])


##Requests a 'fake' key with .get() method
print ("First test - .get()")
print( switch.get('lynx'))


print ("Second test - .get()")
print( switch.get('lynx', "The Key is in another castle!"))

print ("Third test - .get()")
print( switch.get('version'))

print ("Fourth test - .keys()")
print( switch.keys())

print ("Fifth test - .values()")
print( switch.values())

print ("Sixth test - .pop()")
switch.pop('version') #removes this key (and value) pair
print( switch.keys()) # Notice the value of version is gone
print( switch.values()) # notice the value 1.2

print ("Seventh test - Add a new value")
switch['adminlogin'] = 'kar108'
print( switch.keys()) # Notice added a new dict_keys
print( switch.values()) # notice new value displayed for part adminlogin

print ("Eighth test - Add a new value")
switch['password'] = 'qwerty'
print( switch.keys()) # Notice added a new disct_keys,  'password'
print( switch.values()) # notice the value of password being displayed

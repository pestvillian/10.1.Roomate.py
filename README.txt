https://github.com/pestvillian/10.1.Roomate.py.git

The Roomate class is based off of my Dormmate Wan. Wan in general has only three states of being, he is either gaming in his corner, 
sleeping for 12 hours, or setting off the building's fire alarm by trying to cook raw turkey with an electric Tea Kettle. 
The __init__ function contains the ability to set your roomate's name with default parameters already set. To use the Class in your interpreter, first navigate to the directory in which you have it saved.
Then enter into the python3 shell by typing python3. Once there, type the following: from Roomate import Roomate, and the class should then be imported into your interpreter. 
Once the Class has been imported, set a variable to Roomate and enter in your roomates same such as the following: var.Roomate("name"). You will then be presented with a message that
contains your roomates name. Once that is done, you have access to the following methonds: var.set_default()/var.zone()/var.recharch()/var.fire()/var.get_roomate_status().
The set_default() method returns your roomate to the initial parameters that were originaly set regardless of the current ones that may have been changed by other methonds
the zone() method, from any position, puts gaming = True, Sleeping = False, and setting_off_the_fire_alarm = Flase
the recharch() method set sleeping = True, gaming = Flase, and setting_off_the_fire_alarm = Flase
the fire() method sets gaming = Flase, sleeping = True, and setting_off_the_fire_alarm = True
the get_roomate_status() method will return the current boolean values of each parameter at their current states.
To run the example code, navigate to the directory in your interpreter and type the following: python3 Roomate.py, and the example code will be printed out on the screen.

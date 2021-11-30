# 10.1 your own class
# For the classes written below, they will depict the atributes of a real world object
# the real world object in question will be my roomate

#Debug module
import pdb

# Defining the attributes of Wan
class Roomate:
    def __init__(self, name, gaming=True,sleep=False,setting_off_fire_alarm=False):
        #self.gaming = gaming #The natural state of Wan
        #self.sleep = sleep # The Temporary State of Wan
        #self.setting_off_fire_alarm = setting_off_fire_alarm # A side quest of theirs
        self.name = name # You need to call them something
        print(f"This is your roomate {self.name}.\nIt is possible that he is one with the universe.")
        return

    # The recharge roomate method 
    def recharge(self):
        self._time_gaming = 12 # time in hours
        self.sleep = True
        self.gaming = False
        print(f"Wan has surpassed his level for now. The time has passed 4 AM. {self.sleep}") 
        return

    # The enter the gaming zone method
    def zone(self):
        self.gaming = True
        self.sleep = False
        print(f"Your roomate {self.name}, is in his natural state, his mind has become one with another dimension.\nHe is currently unreachable.")
        return

    # The side quest to shut down the Porter building
    def fire(self):
        self.setting_off_fire_alarm = True # It was bound to happen
        self.gaming = False
        self.sleep = False
        print(f"Your roomate {self.name}, has decided that it is a good idea to try and cook\nRaw Turkey in an electric tea kettle.\nYour floor will now be fined.")
        return

    # Restore your roomate to factory default settings
    def set_default(self):
        self.gaming = True
        self.sleep = False
        print("Wan has been rest to facotry default settings")
        return

    # get the current status of your roomate
    def get_roomate_status(self):
        # determine roomate status
        print(f"Your roomate {self.name} is gaming {self.gaming}.")
        print(f"Your roomate {self.name} is sleeping {self.sleep}.")
        print(f"Your roomate {self.name} is setting off the fire alarm {self.setting_off_fire_alarm}.")

    

# The general cycle of my Roomate
def main():

    # Define your roomate
    Person = Roomate("Wan")
    # Set the default settings for your Roomate
    Person.set_default()
    # Put your roomate to sleep
    Person.recharge()
    # Check the status of your roomate
    Person.get_roomate_status()
    # Put your roomate in the zone
    Person.zone()
    # Check in on the roomate
    Person.get_roomate_status()
    # He looks tired, put him back to sleep
    Person.recharge()
    # check
    Person.get_roomate_status()
    # your roomate is ready to break every rule in the building
    Person.fire()
    # See what has changed for him
    Person.get_roomate_status()
    # Exit message
    print("DONE!")
    return

if __name__ == "__main__":
    main()
    
    

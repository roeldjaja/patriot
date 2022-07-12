import csv
import random
import time

class MissileLauncher:
    """
    Missile Launcher Class
    
    """
    def __init__(self):
        return 
    
    
    def launch_missile(self, enemy):
        
        # Launch if enemy detected
        if enemy == 1 :
            print('Missile launched')
            if 0.8 < random.random():
                print('Enemy not hit\n')
            else: 
                print('Enemy hit\n')
                
             
class IFF:
    """
    IFF (Identification Friend or Foe) Class
    
    """
    def __init__(self):
        return  
    
    
    def find_foe(self, radarlist):
        
        # convert binary to decimal
        radarlistdecimal = list(map(lambda n: int(str(n),2), radarlist))
        
        # Count even and odd numbers
        odd_count = len(list(filter(lambda x: (x%2 != 0) , radarlistdecimal)))
        even_count = len(list(filter(lambda x: (x%2 == 0) , radarlistdecimal)))
        
        # Compare even and odd counts
        if even_count < odd_count:
            Foe = 1 ; print("Enemy identified")
        else: Foe = 0 ; print("No Enemy identified\n")
        return Foe
    
    
class Radar:
    """
    Radar Class
    
    """
    def __init__(self, file='Radar-output.csv'):
        self.active = False
        self.index = 0
        
        # Generate list from csv
        self.targets = []
        with open(file) as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                self.targets.append(row)
        
    
    def activate(self):
        self.active = True
        
    def deactivate(self):
        self.active = False
    
    # Select first row from targets list
    def detect(self):
        time.sleep(1)
        try: 
            return self.targets.pop(0)
        except IndexError:
            self.deactivate()
            return None
        
"""
Patriot Code Assessment

@author: Roel Djajadiningrat
"""

from Patriot import MissileLauncher, IFF, Radar


def main():
    launcher = MissileLauncher()
    iff = IFF()
    radar = Radar('Radar-output.csv')
    
    radar.activate()

    while radar.active:
        
        # list from Radar
        signal = radar.detect()
        
        if signal == None:
            return
     
        # Find enemy
        enemy = iff.find_foe(signal)
        
        # Launch Missile
        launcher.launch_missile(enemy)

main()






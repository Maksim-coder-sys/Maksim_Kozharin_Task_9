import time
class TrafficLight:
    __color = 'red'
    def running(self):
        print(f'TrafficLight is {TrafficLight.__color} color ')
        time.sleep(7)
        TrafficLight.__color = 'yellow'
        print(f'TrafficLight is {TrafficLight.__color} color ')
        time.sleep(2)
        TrafficLight.__color = 'green'
        print(f'TrafficLight is {TrafficLight.__color} color ')
        time.sleep(15)
        TrafficLight.__color = 'red'
t = TrafficLight()
t.running()
tr = TrafficLight()
tr.running()
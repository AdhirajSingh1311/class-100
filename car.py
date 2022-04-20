class Car(object):
    def __init__(self,model,color,company,speedLimit) :
        self.color=color
        self.company=company
        self.model=model
        self.speedLimit=speedLimit
    def start (self):
        print('started')
    
    def stop (self):
        print ("stopped")
    def accilarate (self):
        print ('accilarating')
    def changeGear (self,gearType):
        print('gearChanged')
inova=Car('a6','grey','tyota','220')
print (inova.color)
print (inova.speedLimit)

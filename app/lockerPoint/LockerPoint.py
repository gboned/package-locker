from app.package.Package import Package
from app.locker.Locker import Locker
import time


class LockerPoint:

    def __init__(self, id, address, lockers):

        self.id = id
        self.address = address
        self.lockers = lockers


    @staticmethod
    def processPackage(lockerPoint, package):
        print('Processing package. . .')

        if Package.isValid(package.getId()): # Devuelve True o False
            if package.getStatus() == 'NOT REGISTERED':
                emptyLockers = LockerPoint.searchEmptyLockers(lockerPoint)
                # 4. Si existe alguna taquilla vacía, abrirla con setStatus('OPENED') 
                print('Searching available lockers...')
                if emptyLockers != None and len(emptyLockers) > 0:
                    emptyLockers[0].setStatus('OPENED')   
                    print('Please, leave the package and close the locker before leave.') 
                    # 6. Tras 20 segundos, cerrar la taquilla.
                    # y marcar el paquete como 'keeping'.
                    print('Closing the opened locker...')
                    time.sleep(5)
                    emptyLockers[0].setStatus('CLOSED')
                    package.setStatus('KEEPING')
                    print('Process terminated.')    
                # 5. En caso contrario, imprimir por pantalla
                else:
                    print('There aren\'t any free lockers available at the moment.')
        else:
            print('Invalid code')
            print('Process terminated')


    @staticmethod
    def searchEmptyLockers(lockerPoint):
        emptyLockers = []
        for locker in lockerPoint.getLockers().values():
            if not locker.isOccupied():
                emptyLockers.append(locker)
        return emptyLockers 


    def getId(self):
        return self.id

    
    def setId(self, newId):
        self.id = newId



    def getAddress(self):
        return self.address


    def setAddress(self, newAddress):
        self.address = newAddress

    

    def getLockers(self):
        return self.lockers


    def setLockers(self, newLockers):
        self.lockers = newLockers

from app.package.Package import Package



class LockerPoint:

    def __init__(self, id, address, lockersList):

        self.id = id
        self.address = address
        self.lockersList = lockersList


    @staticmethod
    def processPackage(lockerPoint, package):
        print('Processing package. . .')
        if Package.isValid(package.getId()): # Devuelve True o False
            return True
        else:
            print('Invalid code')
            print('Process terminated')


    def getId(self):
        return self.id

    
    def setId(self, newId):
        self.id = newId



    def getAddress(self):
        return self.address


    def setAddress(self, newAddress):
        self.address = newAddress

    

    def getLockersList(self):
        return self.lockersList


    def setLockersList(self, newLockersList):
        self.lockersList = newLockersList

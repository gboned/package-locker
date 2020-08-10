class LockerPoint:

    def __init__(self, id, address, lockersList):

        self.id = id
        self.address = address
        self.lockersList = lockersList



    def processPackage(self, lockerPoint, package):
        Package.isValid(package.getId())
        return True


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

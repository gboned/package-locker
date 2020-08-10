class Locker:

    def __init__(self, id, status, occupied, packageCode):

        self.id = id
        self.status = status
        self.occupied = occupied
        self.packageCode = packageCode



    def getId(self):
        return self.id


    def setId(self, newId):
        self.id = newId



    def getStatus(self):
        return self.status


    def setStatus(self, newStatus):
        self.status = newStatus



    def isOccupied(self):
        return self.occupied
    

    def setOccupied(self, newOccupied):
        self.occupied = newOccupied



    def getPackageCode(self):
        return self.packageCode
    

    def setPackageCode(self, newPackageCode):
        self.packageCode = newPackageCode
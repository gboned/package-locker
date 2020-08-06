class Locker:

    def __init__(self, id, status, isOccupied, packageCode):

        self.id = id
        self.status = status
        self.isOccupied = isOccupied
        self.packageCode = packageCode



    def getId(self):
        return self.id


    def setId(self, newId):
        self.id = newId



    def getStatus(self):
        return self.status


    def setStatus(self, newStatus):
        self.status = newStatus



    def getIsOccupied(self):
        return self.isOccupied
    

    def setIsOccupied(self, newIsOccupied):
        self.isOccupied = newIsOccupied



    def getPackageCode(self):
        return self.packageCode
    

    def setPackageCode(self, newPackageCode):
        self.packageCode = newPackageCode
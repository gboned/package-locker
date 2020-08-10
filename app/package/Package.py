class Package:

    def __init__(self, id, status):

        self.id = id
        self.status = status

    @staticmethod
    def isValid(packageCode):
        if (
            packageCode[:4] == 'PACK' and
            packageCode[4] == '-' and
            packageCode[5:8].isdigit() and
            packageCode[8] == '-' and
            packageCode[9:12].isdigit() and
            packageCode[12] == '-' and
            packageCode[13:16].isdigit()):

                return True
        else:
            return False
    

    def getId(self):
        return self.id


    def setId(self, newId):
        self.id = newId



    def getStatus(self):
        return self.status


    def setStatus(self, newStatus):
        self.status = newStatus

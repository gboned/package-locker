class Package:

    def __init__(self, code, status):

        self.code = code
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
    

    def getCode(self):
        return self.code


    def setCode(self, newCode):
        self.code = newCode



    def getStatus(self):
        return self.status


    def setStatus(self, newStatus):
        self.status = newStatus

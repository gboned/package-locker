from app.locker.Locker import Locker



def testLocker():

    lockerInstance = Locker(
        '1', # identificador
        'CLOSED', # si está abierta o cerrada 
        False, # si está ocupado
        '' # código del paquete que lo ocupa (no hay)
    )

    assert lockerInstance != None
    assert lockerInstance.getId() == '1'
    assert lockerInstance.getStatus() == 'CLOSED'
    assert not lockerInstance.isOccupied
    assert lockerInstance.getPackageCode() == ''


    lockerInstance.setStatus('OPENED')

    assert lockerInstance.getStatus() == 'OPENED'

    lockerInstance.setIsOccupied(True)

    assert lockerInstance.isOccupied

    lockerInstance.setPackageCode('PACK-165-997-232')

    assert lockerInstance.getPackageCode() == 'PACK-165-997-232'



if __name__ == '__main__':
    testLocker()
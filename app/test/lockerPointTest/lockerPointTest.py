from app.locker.Locker import Locker
from app.lockerPoint.LockerPoint import LockerPoint
from app.package.Package import Package
import time


def testLockerPoint():

    locker1 = Locker(
        '1', # identificador
        'CLOSED', # si está abierta o cerrada 
        False, # si está ocupado
        '' # código del paquete que lo ocupa (no hay)
    )

    locker2 = Locker(
        '2', # identificador
        'CLOSED', # si está abierta o cerrada
        False, # si está ocupado
        '' # código del paquete que lo ocupa (no hay)
    )


     # Creamos la instancia del punto de recogida
    lockerPointInstance = LockerPoint(
        'sr6cxt7v8fybw9n', # identificador
        'Calle de las Flores, 22', # dirección
        {   
            # lista de taquillas 
            locker1.getId(): locker1, # '1': locker1
            locker2.getId(): locker2  # '2': locker2
        }
    )


    assert lockerPointInstance != None
    assert lockerPointInstance.getId() == 'sr6cxt7v8fybw9n'
    assert lockerPointInstance.getAddress() == 'Calle de las Flores, 22'
    # Para comprobar que el id del primer locker de la lista de lockers del LockerPoint es 1
    assert lockerPointInstance.getLockers()['1'].getId() == '1'

    lockerPointInstance.getLockers()['1'].setStatus('OPENED')
    assert lockerPointInstance.getLockers()['1'].getStatus() == 'OPENED'
    
    newPackage = Package(
        'PACK-111-222-333', # código identificador
        'NOT REGISTERED', # estado
    )
    # Guardar paquete en una de las taquillas
    lockerPointInstance.getLockers()['1'].setPackageCode(newPackage.getCode())
    newPackage.setStatus('KEEPING')
    locker1.setOccupied(True)

    keeper = LockerPoint.searchPackage(lockerPointInstance, newPackage)
    assert keeper != None
    assert keeper.getId() == locker1.getId()

    locker2.setOccupied(False)
    emptyLockers = LockerPoint.searchEmptyLockers(lockerPointInstance)
    assert len(emptyLockers) == 1
    
    assert emptyLockers[0].getId() == '2'
    assert emptyLockers[0].isOccupied() == False

    emptyLockers[0].setStatus('OPENED')
    assert locker2.getStatus() == 'OPENED'

if __name__ == '__main__':
    testLockerPoint()
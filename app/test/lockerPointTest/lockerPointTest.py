from app.locker.Locker import Locker
from app.lockerPoint.LockerPoint import LockerPoint



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
    assert lockerPointInstance.getLockersList()['1'].getId() == '1'

    lockerPointInstance.getLockersList()['1'].setStatus('OPENED')
    assert lockerPointInstance.getLockersList()['1'].getStatus() == 'OPENED'



if __name__ == '__main__':
    testLockerPoint()
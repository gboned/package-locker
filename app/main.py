from app.locker.Locker import Locker
from app.lockerPoint.LockerPoint import LockerPoint
from app.package.Package import Package



def main():

    # Preparamos las taquillas
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
    lockerPoint = LockerPoint(
        'sr6cxt7v8fybw9n', # identificador
        'Calle de las Flores, 22', # dirección
        [locker1, locker2] # lista de taquillas 
    )

    # Creamos un paquete para dejar...
    package1 = Package(
        'PACK-111-222-333', # código identificador
        'NOT REGISTERED', # estado
    )
    # y otro para recoger
    package2 = Package(
        'PACK-165-997-232', # código identificador
        'KEEPING', # estado
    )



if __name__ == '__main__':
    main()
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
        {   # Diccionario de taquillas
            locker1.getId(): locker1,
            locker2.getId(): locker2       
        }
 
    )

    # Creamos un paquete con un código válido, ...
    package1 = Package(
        'PACK-111-222-333', # código identificador
        'NOT REGISTERED', # estado
    )
    # otro con un código no válido...
    package2 = Package(
        'Pckr-00000000000', # código identificador
        'KEEPING', # estado
    )
    # e intentamos recoger un packete que no se encuentra en el lockerPoint
    package3 = Package(
        'PACK-555-231-444', # código identificador
        'KEEPING', # estado
    )


    print('Welcome!')

    print('------------------------------------------------------------------')

    # dejamos package1
    LockerPoint.processPackage(lockerPoint, package1)

    print('------------------------------------------------------------------')
        
    # recogemos package1
    LockerPoint.processPackage(lockerPoint, package1)

    print('------------------------------------------------------------------')

    # probamos con un código no válido -con package2-
    LockerPoint.processPackage(lockerPoint, package2)

    print('------------------------------------------------------------------')
    
    # probamos con un paquete que no está en este lockerPoint 
    LockerPoint.processPackage(lockerPoint, package3)

    print('------------------------------------------------------------------')

    print ('Bye!')



if __name__ == '__main__':
    main()
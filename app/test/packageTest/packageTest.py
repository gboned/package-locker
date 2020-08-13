from app.package.Package import Package



def testPackage():

    packageInstance = Package(
        'PACK-111-222-333', # código identificador
        'NOT REGISTERED', # estado
    )

    assert packageInstance != None
    assert packageInstance.getCode() == 'PACK-111-222-333'
    assert packageInstance.getStatus() == 'NOT REGISTERED'


    packageInstance.setId('PACK-222-333-444')

    assert packageInstance.getCode() == 'PACK-222-333-444'


    packageInstance.setStatus('KEEPING')
    
    assert packageInstance.getStatus() == 'KEEPING'


def testIsValid():
    packageInstance1 = Package(
    'PACK-111-222-333', # código identificador
    'NOT REGISTERED', # estado
    )

    packageInstance2 = Package(
        'Pckr-00000000000', # código identificador
        'KEEPING', # estado
    )

    packageInstance3 = Package(
        'PACK-555-231-444', # código identificador
        'KEEPING', # estado
    )

    assert Package.isValid(packageInstance1.getCode()) == True

    assert Package.isValid(packageInstance2.getCode()) == False

    assert Package.isValid(packageInstance3.getCode()) == True



if __name__ == '__main__':
    testPackage()
    testIsValid()

from app.package.Package import Package



def testPackage():

    packageInstance = Package(
        'PACK-111-222-333', # código identificador
        'NOT REGISTERED', # estado
    )

    assert packageInstance != None
    assert packageInstance.getId() == 'PACK-111-222-333'
    assert packageInstance.getStatus() == 'NOT REGISTERED'


    packageInstance.setId('PACK-222-333-444')

    assert packageInstance.getId() == 'PACK-222-333-444'


    packageInstance.setStatus('KEEPING')
    
    assert packageInstance.getStatus() == 'KEEPING'



if __name__ == '__main__':
    testPackage()


from optimizar import optimizar

def test_add ():
    datos = optimizar([])
    datos.add(8)
    datos.add(12)
    datos.add(6)
    datos.add(3)

def test_media():
    datos = optimizar([8,12,6,3])
    assert datos.media()
    


       


 
    
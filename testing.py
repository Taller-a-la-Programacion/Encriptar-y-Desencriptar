import encriptar;
import desencriptar;
import pytest;

texto = "CASA"

def test_encriptar_1():
    assert encriptar.encriptar(texto) == "043041053041"
    
def test_desencriptar_1():
    assert desencriptar.desencriptar("043041053041") == texto                      

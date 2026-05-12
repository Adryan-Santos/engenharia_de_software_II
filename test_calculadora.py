import pytest
from calculadora import Calculadora

def test_soma():
    
    #Arrange
    calc = Calculadora()
    #Fim Arrange

    valor_positivo = calc.soma(2,3)
    assert valor_positivo == 5

    valor_negativo = calc.soma(-7,4)
    assert valor_negativo == -3

    soma_flutuante = calc.soma(0.1,0.2) 
    assert soma_flutuante == 0.30

def test_subtrai():

    #Arrange
    calc = Calculadora()
    #Fim Arrange

    valor_positivo = calc.subtrai(3,2)
    assert valor_positivo == 1

def test_multiplica():

    #Arrange
    calc = Calculadora()
    #Fim Arrange

    valor_positivo = calc.multiplica(3,2)
    assert valor_positivo == 6

    valor_negativo = calc.multiplica(3,-2)
    assert valor_negativo == -6

def test_divide():

    #Arrange
    calc = Calculadora() 
    #Fim Arrange


    valor_positivo = calc.divide(6, 2)
    assert valor_positivo == 3

def test_varias_operacoes():

    #Arrange
    calc = Calculadora()
    #Fim Arrange

    result_soma = calc.soma(10.5, 4.5) # 15.0
    result_sub = calc.subtrai(result_soma, 3) # 12.0
    result_soma2 = calc.soma(result_sub, -2) # 10.0
    result_final = calc.multiplica(result_soma2, 2) # 20.0

    assert result_final == 20

def test_divisao_por_zero():
    
    #Arrange
    calc = Calculadora()

    #Act
    #Chamada da função a ser testada
    #Fim_Act

    with pytest.raises(ValueError, match=r"Não é permitida divisão por zero"):
        calc.divide(2,0)



def test_potencia():

    # Arrange
    calc = Calculadora()
    # Fim Arrange

    valor_positivo = calc.potencia(2, 3)
    assert valor_positivo == 8

    valor_zero = calc.potencia(5, 0)
    assert valor_zero == 1
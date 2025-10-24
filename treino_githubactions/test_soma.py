import soma as som
import subtracao as sub

def test_soma():
    result = som.soma(2, 2)

    assert 4 == result

def test_subtracao():
    result = sub.subtracao(2, 2)

    assert 0 == result

def test_multiplicacao():
    result = sub.multiplicacao(2, 2)

    assert 4 == result

def test_divisao():
    result = sub.divisao(2, 2)

    assert 1 == result
import converter

def test_length():
    assert converter.meters_to_km(1000) == 1
    assert converter.km_to_meters(1) == 1000

def test_weight():
    assert round(converter.kg_to_lb(1), 2) == 2.20
    assert round(converter.lb_to_kg(2.20462), 2) == 1.00

def test_temp():
    assert converter.c_to_f(0) == 32
    assert round(converter.f_to_c(32), 2) == 0

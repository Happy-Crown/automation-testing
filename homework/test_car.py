import pytest
from base_programming import Car


@pytest.fixture
def car():
    return Car("Hunday", "Solaris", 2017, 1000)


def test_default_mileage(car):
    assert car.mileage == 1000

@pytest.mark.parametrize("distance, result", [
    (0, 1000),
    (1, 1001),
    (1000, 2000),
    (0.5, 1000.5)
])
def test_increse_mileage(car, distance, result):
    car.drive(distance)
    assert car.mileage == result

def test_decrese_mileage_not_supported(car):
    with pytest.raises(ValueError):
        car.drive(-50)

def test_str_method_check(car):
    expected = "'Solaris' by 'Hunday' with 1000km mileage"
    assert str(car) == expected
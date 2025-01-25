import pytest
from base_programming import Car


@pytest.fixture
def base_car():
    return Car(brand="Hunday", model="Solaris", year =2017)

@pytest.fixture
def premium_car():
    return Car(brand="Tesla", model="Model S", year=2023)


# Проверки метода drive класса Car
def test_default_mileage(base_car):
    assert base_car.mileage == 0

@pytest.mark.parametrize("distance, result", [
    (0, 0),
    (1000, 1000),
    (50.5, 50.5)
])
def test_increse_mileage(base_car, distance, result):
    base_car.drive(distance)
    assert base_car.mileage == result

def test_multiple_increse_mileage(base_car):
    base_car.drive(500)
    base_car.drive(1000)
    assert base_car.mileage == 1500

def test_decrese_mileage_not_supported(base_car):
    with pytest.raises(ValueError):
        base_car.drive(-50)

# Проверки метода __str__ класса Car
def test_str_method_check(base_car):
    expected = "'Solaris' by 'Hunday' with 0km mileage"
    assert str(base_car) == expected

def test_str_method_after_increse_mileage(premium_car):
    premium_car.drive(5000)
    expected = "'Model S' by 'Tesla' with 5000km mileage"
    assert str(premium_car) == expected
    
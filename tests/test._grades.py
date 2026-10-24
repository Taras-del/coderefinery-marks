import pytest
from grades import calculate_average, get_highest_grade, is_passing

@pytest.mark.parametrize("grades, expected", [
    ([100, 90, 80], 90.0),
    ([85, 90, 92], 89.0),
    ([12.5, 11.5, 10.0], 11.333333) 
])
def test_calculate_average(grades, expected):
    assert calculate_average(grades) == pytest.approx(expected, rel=1e-4)

def test_get_highest_grade():
    assert get_highest_grade([55, 95, 80]) == 95

def test_is_passing():
    assert is_passing(80.0, 60.0) is True
    assert is_passing(40.0, 60.0) is False

def test_empty_grades_raises_error():
    with pytest.raises(ValueError):
        calculate_average([])

import AP

import pytest

@pytest.mark.areasqarearectperirect
def test_Area_of_square():
    sides= 4
    result = AP.Area_of_square(sides)
    assert result == sides**2
@pytest.mark.areasqarearectperirect
def test_perimeter_of_rectangle():
    length = 10
    breadth = 2
    result = AP.perimeter_of_rectangle(length,breadth)
    assert result == 2*(length+breadth)
@pytest.mark.areasqarearectperirect
def test_Area_of_Rectangle():
    length = 10
    breadth = 2
    result = AP.Area_of_Rectangle(length,breadth)
    assert result == length*breadth
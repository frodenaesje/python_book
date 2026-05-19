# file: test_sc_09_02_area_circle.py

import pytest
from sc_09_02_area_circle import area_circle


def test_area_radius_1():
    # pytest.approx() is used for approximate decimal equality.
    assert area_circle(1) == pytest.approx(3.14159, abs=0.001)


def test_area_radius_2():
    assert area_circle(2) == pytest.approx(12.56636, abs=0.001)

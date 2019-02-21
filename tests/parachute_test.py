import pytest, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../parachuteCore')))
import parachute
from parachuteCore import menu, menulist


def test_launch():
    assert True

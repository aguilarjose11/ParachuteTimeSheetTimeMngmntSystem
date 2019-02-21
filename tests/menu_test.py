import pytest, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../parachuteCore')))
from parachuteCore import menu, menulist


def test_runmenu(capsys):
    testedMenu = menu.Menu()
    tested_input = [1, 2, "72"]

    def mock_input(promptMessage):
        return tested_input.pop(0)

    testedMenu.getchoice = mock_input
    testreturn = menu.runmenu(testedMenu)
    out, err = capsys.readouterr()
    assert testreturn == "72"

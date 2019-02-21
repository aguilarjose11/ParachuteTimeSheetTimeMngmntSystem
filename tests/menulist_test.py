import pytest, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../parachuteCore')))
from parachuteCore import menulist, menu


class Test_menulist():

    @pytest.mark.parametrize("keys, expected", [
        ([72, 72, 72, 72, 13], "0"),
        ([80, 80, 80, 72, 13], "1"),
        ([80, 80, 13], "2"),
        ([127, 13], "0"),
        (["sys.exit", 27], "-1")
    ])
    def test_mainMenu(self, keys, expected, capsys):
        user_keys = keys

        def mock_input(*args, **argv):
            return keys.pop(0)

        def mock_getch(*args, **argv):
            return "testing..."

        menulist.ord = mock_input
        menulist.getch = mock_getch
        testMenu = menulist.mainMenu()
        if user_keys[0] == "sys.exit":
            user_keys.pop(0)
            with pytest.raises(SystemExit) as testee_exit:
                menu.runmenu(testMenu)
            assert testee_exit.type == SystemExit
            assert testee_exit.value.code == 0
        else:
            returnVal = menu.runmenu(testMenu)
            assert returnVal == expected

    @pytest.mark.parametrize("keys, expected", [
        ([13], "0"),
        ([80, 13], "1"),
        ([80, 80, 13], "2"),
        ([80, 80, 80, 13], "3"),
        ([80, 80, 80, 80, 13], "4"),
        ([80, 80, 80, 80, 80, 13], "4"),
        ([80, 80, 80, 80, 80, 72, 13], "3"),
        ([80, 80, 80, 80, 80, 72, 72, 13], "2"),
        ([80, 80, 80, 80, 80, 72, 72, 72, 13], "1"),
        ([80, 80, 80, 80, 80, 72, 72, 72, 72, 13], "0"),
        ([80, 80, 80, 80, 80, 72, 72, 72, 72, 72, 13], "0"),
        ([127, 13], "0"),
        (["sys.exit", 27], "-1")
    ])
    def test_registerMenu(self, keys, expected, capsys):
        user_keys = keys

        def mock_ord(*argv, **args):
            return user_keys.pop(0)

        def mock_getch(*argv, **args):
            return "...testing."

        menulist.getch = mock_getch
        menulist.ord = mock_ord
        testMenu = menulist.registerMenu()
        if user_keys[0] == "sys.exit":
            user_keys.pop(0)
            with pytest.raises(SystemExit) as testee_exit:
                menu.runmenu(testMenu)
            assert testee_exit.type == SystemExit
            assert testee_exit.value.code == 0
        else:
            returnVal = menu.runmenu(testMenu)
            assert returnVal == expected

    @pytest.mark.parametrize("keys, expected", [
        ([13], "0"),
        ([80, 13], "1"),
        ([80, 80, 13], "2"),
        ([80, 80, 80, 13], "2"),
        ([80, 80, 80, 72, 13], "1"),
        ([80, 80, 80, 72, 72, 13], "0"),
        ([80, 80, 80, 72, 72, 72, 13], "0"),
        ([124, 13], "0"),
        (["sys.exit", 27], "-1")
    ])
    def test_loginMenu(self, keys, expected, capsys):
        user_keys = keys

        def mock_ord(*argv, **args):
            return user_keys.pop(0)

        def mock_getch(*argv, **args):
            return "...testing."

        menulist.getch = mock_getch
        menulist.ord = mock_ord
        testMenu = menulist.loginMenu()
        if user_keys[0] == "sys.exit":
            user_keys.pop(0)
            with pytest.raises(SystemExit) as testee_exit:
                menu.runmenu(testMenu)
            assert testee_exit.type == SystemExit
            assert testee_exit.value.code == 0
        else:
            returnVal = menu.runmenu(testMenu)
            assert returnVal == expected

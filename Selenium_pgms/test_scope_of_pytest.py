import pytest

class Test_scope_pytest():

    @pytest.fixture(scope='session') # you can also use scope as "module"
    def setting_up(self):
        print("These statements to set-up Initially")
        a=10
        yield
        print("These statements to tear-down session")

    def test_01(self,setting_up):
        print(a)
        print("This is from test 01")

    def test_02(self,setting_up):
        print("This is from test 02")

    def test_03(self,setting_up):
        print(a)
        print("This is from test 03")
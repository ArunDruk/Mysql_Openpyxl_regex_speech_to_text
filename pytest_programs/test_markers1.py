##############################################################################################################
## pytest -v -s test_markers1.py -m login

## we can categorize the test cases based on customized markers like smoke , sanity etc
# pytest -m smoke -v
#pytest -k smoke
##############################################################################################################

from pytest import mark

@mark.login
def test_mark1():
    assert True

@mark.smoke
def test_mark2():
    assert True


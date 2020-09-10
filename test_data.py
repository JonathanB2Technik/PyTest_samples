from data import StudentDB

import pytest

@pytest.fixture(scope='module')
def db():
    print('=====setup=====')
    db = StudentDB()
    db.connect('data.json')
    yield db
    print('=====teardown=====')
    db.close()


def test_jo_data(db):
    jo_data = db.get_data('Jo')
    assert jo_data['id'] == 1
    assert jo_data['name'] == 'Jo'
    assert jo_data['result'] == 'fail'


def test_divi_data(db):
    divi_data = db.get_data('Divi')
    assert divi_data['id'] == 2
    assert divi_data['name'] == 'Divi'
    assert divi_data['result'] == 'pass'


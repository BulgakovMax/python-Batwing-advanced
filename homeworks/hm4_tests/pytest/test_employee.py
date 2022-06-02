import pytest
from employee import Employee
from classes import  ClassForTest

data = Employee("nick", "clinton", 1000)

def test_email():
    assert data.email == 'nick.clinton@email.com'

def test_fullname():
    assert data.fullname == 'nick clinton'

def test_apply_raise():
    assert data.pay*data.raise_amt == 1050

def test_monthly_schedule(requests_mock):
    requests_mock.get(
        "https://test.com", text="data", status_code=200)
    classForTest = ClassForTest()
    assert classForTest.send_request().ok
    assert classForTest.send_request().status_code == 200

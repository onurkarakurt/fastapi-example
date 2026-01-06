import pytest
from app.calculations import add, subtract, multiply, divide, BankAccount

@pytest.fixture
def zero_bank_account():
    print("Creating empty bank account")
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300)
])
def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1, num2) == expected

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(7, 6) == 42

def test_divide():
    assert divide(20, 5) == 4

def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    print("Testing default amount")
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit(bank_account):
    bank_account.deposit(30)
    assert bank_account.balance == 80

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 2) == 55 

@pytest.mark.parametrize("deposits, withdrawals, expected", [
    (200, 100, 100),
    (50, 25, 25),
    (300, 150, 150)
])
def test_bank_transaction(zero_bank_account, deposits, withdrawals, expected):
    zero_bank_account.deposit(deposits)
    zero_bank_account.withdraw(withdrawals)
    assert zero_bank_account.balance == expected
from app import add,mul,sub,div
 
def test_add():
    assert add(2, 3) == 5
def test_mul():
    assert mul(2, 2) == 4
def test_sub():
    assert sub(2,2)==0
def test_div():
    assert div(2,2)==1

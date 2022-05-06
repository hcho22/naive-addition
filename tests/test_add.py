from src.add import add
import numpy as np

def test_add():
    assert add(1) == 101
    assert add(np.int_(1)) == 101
    assert add(np.int_(1), np.int_(100)) == 101
    assert add("fourth ", "brain") == "fourth brain"


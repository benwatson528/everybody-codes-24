import os
from pathlib import Path

from main.day01.potion_preparation import solve


def test_p1_simple():
    assert solve("ABBAC") == 5


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 1299


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read()

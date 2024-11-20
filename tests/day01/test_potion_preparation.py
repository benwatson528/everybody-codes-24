import os
from pathlib import Path

from main.day01.potion_preparation import solve


def test_p1_simple():
    assert solve("ABBAC") == 5


def test_p1_real():
    assert solve(read_input("data/p1_input.txt")) == 1299


def test_p2_simple():
    assert solve(pair("AxBCDDCAxD")) == 28


def test_p2_real():
    assert solve(pair(read_input("data/p2_input.txt"))) == 5529


def test_p3_simple():
    assert solve(triple("xBxAAABCDxCC")) == 30


def test_p3_real():
    assert solve(triple(read_input("data/p3_input.txt"))) == 27734


def pair(ls):
    return zip(ls[::2], ls[1::2])


def triple(ls):
    return zip(ls[::3], ls[1::3], ls[2::3])


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().strip()

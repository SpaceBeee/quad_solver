import main
import pytest


def test_real_roots():
    assert main.quad_solver(1.0, 5.0, 6.0) == [-2.0, -3.0]

# def test_fraction_roots():
#     assert main.quad_solver(6, 11, -35) ==


def test_no_roots():
    ...


def test_one_root():
    ...


def test_imaginary_roots():
    with pytest.raises(Exception):
        main.quad_solver(1.0, 4.0, 5.0)


# def test_imaginary_roots():
#     assert main.quad_solver(1, 4, 5) == [-2 + i, -2 - i]


def test_wrong_parameters():
    with pytest.raises(TypeError):
        main.quad_solver(1)


def test_wrong_type1():
    with pytest.raises(TypeError):
        main.quad_solver('a', 'a', 'a')


def test_wrong_type2():
    with pytest.raises(TypeError):
        main.quad_solver('a', 'a', 'a')


import main
import pytest

coefficients = [
    (1.0, 0.0, -9.0, [3.0, -3.0]),
    (1.0, -4.0, 3.0, [3.0, 1.0]),
    (1.0, -4.0, 4.0, [2.0])
]

@pytest.mark.parametrize("a, b, c, solution", coefficients)

def test_coefficents(a, b, c, solution):
    assert main.quad_solver(a, b, c) == solution


def test_real_roots():
    assert main.quad_solver(1.0, 5.0, 6.0) == [-2.0, -3.0]

# def test_fraction_roots():
#     assert main.quad_solver(6, 11, -35) ==


def test_no_coefficients():
    with pytest.raises(ValueError):
        main.quad_solver(0.0, 1.0, 2.0)


def test_one_root():
    ...


def test_imaginary_roots():
    with pytest.raises(ValueError):
        main.quad_solver(1.0, 4.0, 5.0)


def test_imaginary_roots():
    assert main.quad_solver(1.0, 4.0, 5.0) == [(-2+1j), (-2-1j)]

def test_wrong_parameters():
    with pytest.raises(TypeError):
        main.quad_solver(1)


def test_wrong_type1():
    with pytest.raises(TypeError):
        main.quad_solver('a', 'a', 'a')


def test_wrong_type2():
    with pytest.raises(TypeError):
        main.quad_solver('a', 'a', 'a')
from src.myfunc import square_integer

class TestSquareInteger:
    
    def test_square_integer_positive(self):
        assert square_integer(2) == 4
        assert square_integer(3) == 9
        assert square_integer(10) == 100

    def test_square_integer_negative(self):
        assert square_integer(-2) == 4
        assert square_integer(-3) == 9
        assert square_integer(-10) == 100

    def test_square_integer_zero(self):
        assert square_integer(0) == 0

    def test_square_integer_large(self):
        assert square_integer(1000) == 1000000
        assert square_integer(-1000) == 1000000

require 'test/unit'
require 'fizzbuzz'

class TesteFizzBuzz < Test::Unit::TestCase

    def test_entrada_1_retorna_1
        fizzbuzz = FizzBuzz.new(1)
        self.assert_equal(fizzbuzz.imprimir, '1')
    end

    def test_entrada_3_retorna_fizz
        fizzbuzz = FizzBuzz.new(3)
        self.assert_equal(fizzbuzz.imprimir, 'fizz')
    end

    def test_entrada_2_retorna_2
        fizzbuzz = FizzBuzz.new(2)
        self.assert_equal(fizzbuzz.imprimir,'2')
    end

    def test_entrada_5_retorna_buzz
        fizzbuzz = FizzBuzz.new(5)
        self.assert_equal(fizzbuzz.imprimir,'buzz')
    end

    def test_entrada_15_retorna_fizzbuzz
        fizzbuzz = FizzBuzz.new(15)
        self.assert_equal(fizzbuzz.imprimir,'fizzbuzz')
    end

    def test_entrada_6_retorna_fizz
        fizzbuzz = FizzBuzz.new(6)
        self.assert_equal(fizzbuzz.imprimir, 'fizz')
    end

    def test_entrada_135_retorna_fizzbuzz
        fizzbuzz = FizzBuzz.new(135)
        self.assert_equal(fizzbuzz.imprimir, 'fizzbuzz')
    end

end

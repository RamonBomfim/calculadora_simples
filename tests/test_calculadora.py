import unittest
from decimal import Decimal

from calculadora import Calculadora

class Testcalculadora(unittest.TestCase):
  def setUp(self):
    self.calc = Calculadora()

  def test_adicao(self):
      """
      Test the addition method of the calc object with various input values.
      """
      self.assertAlmostEqual(self.calc.adicao(2, 3), Decimal(5))
      self.assertAlmostEqual(self.calc.adicao(-2, 3), Decimal(1))
      self.assertAlmostEqual(self.calc.adicao(0, 0), Decimal(0))

  def test_subtracao(self):
      """
      Test the subtraction method of the calc object with various inputs.
      """
      self.assertAlmostEqual(self.calc.subtracao(5, 3), Decimal(2))
      self.assertAlmostEqual(self.calc.subtracao(-2, 3), Decimal(-5))
      self.assertAlmostEqual(self.calc.subtracao(0, 0), Decimal(0))

  def test_multiplicacao(self):
      """
      Test the multiplicacao method of the calc object with various inputs.
      """
      self.assertEqual(self.calc.multiplicacao(2, 3), Decimal(6))
      self.assertEqual(self.calc.multiplicacao(-2, 3), Decimal(-6))
      self.assertEqual(self.calc.multiplicacao(0, 5), Decimal(0))

  def test_divisao(self):
      """
      Test the division method of the Calculator class with various input values.
      """
      self.assertEqual(self.calc.divisao(6, 3), Decimal(2))
      self.assertEqual(self.calc.divisao(-6, 3), Decimal(-2))
      self.assertEqual(self.calc.divisao(0, 5), Decimal(0))
      self.assertEqual(self.calc.divisao(1, 0), "ERRO: Não é possível dividir por zero.")

  def test_calcular(self):
      """
      Test the calcular method with various input combinations and check the expected results.
      """
      self.assertEqual(self.calc.calcular("+", 2, 3), Decimal(5))
      self.assertEqual(self.calc.calcular("-", 5, 3), Decimal(2))
      self.assertEqual(self.calc.calcular("*", 2, 3), Decimal(6))
      self.assertEqual(self.calc.calcular("/", 6, 3), Decimal(2))
      self.assertEqual(self.calc.calcular("/", 1, 0), "ERRO: Não é possível dividir por zero.")
      self.assertEqual(self.calc.calcular("%", 2, 3), "ERRO: Operação inválida. Por favor, escolha +, -, * ou /.")
      self.assertEqual(self.calc.calcular("+", "a", 3), "ERRO: Entrada inválida. Certifique-se de digitar números válidos.")

if __name__ == '__main__':
    unittest.main()

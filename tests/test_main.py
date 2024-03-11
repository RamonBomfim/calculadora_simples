import unittest
from unittest.mock import patch
from io import StringIO
from main import main

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['+', '2', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_adicao(self, mock_stdout, mock_input):
        """
        Test the addition function by simulating user input and checking the output.
        """
        main()
        self.assertIn("O resultado da operação é: 5", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['-', '5', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_subtracao(self, mock_stdout, mock_input):
        """
        Test the subtraction function by mocking user input and checking the output.
        """
        main()
        self.assertIn("O resultado da operação é: 2", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['*', '2', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiplicacao(self, mock_stdout, mock_input):
        """
        Test for the main function with patched input and output streams.
        """
        main()
        self.assertIn("O resultado da operação é: 6", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['/', '6', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_divisao(self, mock_stdout, mock_input):
        """
        Test the main function with division operation and check if the correct result is printed to the standard output.
        """
        main()
        self.assertIn("O resultado da operação é: 2", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['/', '1', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_divisao_por_zero(self, mock_stdout, mock_input):
        """
        Test the behavior of the main function when dividing by zero.
        """
        main()
        self.assertIn("ERRO: Não é possível dividir por zero.", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
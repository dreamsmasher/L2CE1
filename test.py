from conversions import *
import unittest

class TestConversions(unittest.TestCase):
  def test_km_to_m(self):
    testInputs = [1, 3, 0, 9.5, 1.5]
    for x in testInputs:
      output = c.km_to_m(x)
      assert output == x * 1000, "{} kilometers to meters should be {}, got {} instead".format(x, x / 1000, output)
  
  def test_m_to_km(self):
    testInputs = [1000, 1500, 3000, 9999]
    for x in testInputs:
      output = c.m_to_km(x)
      assert output == x / 1000, "{} meters to kilometers should be {}, got {} instead".format(x, x / 1000, output)

  def test_mg_to_g(self):
    testInputs = [1000, 500, 10000, 400]
    for x in testInputs:
      output = c.mg_to_g(x)
      assert output == x / 1000, "{} milligrams to grams should be {}, got {} instead".format(x, x / 1000, output)

  def test_mg_to_kg(self):
    testInputs = [1_000_000, 1_500_000, 3_000_000, 4_500_000, 9_000_000]
    for x in testInputs:
      output = c.mg_to_kg(x)
      expected = x / 1_000_000
      assert output == expected, "{} milligrams to kilograms should be {}, got {} instead".format(x, expected, output)

  def test_mm_to_km(self):
    testInputs = [1_000_000, 3_000_000, 4_500_000, 9_000_000]
    for x in testInputs:
      output = c.mm_to_km(x)
      expected = x / 1_000_000
      assert output == expected, "{} millimeters to kilometers should be {}, got {} instead".format(x, expected, output)

if __name__ == '__main__':
  c = Conversions()
  unittest.main()
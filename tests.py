import unittest

class TestGameFunctions(unittest.TestCase):
  def test_foo(self):
    self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
  unittest.main()
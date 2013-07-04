import unittest

class ScalesTest(unittest.TestCase):

  def test_default_scale(self):
    scale = Scale()
    self.assertEqual(['C', 'D', 'E', 'F', 'G', 'A', 'B'], scale)
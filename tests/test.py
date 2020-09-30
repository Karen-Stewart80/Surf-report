import unittest
from classes import Surf

class TestSurfClass(unittest.TestCase):
    def test_surf(self):
        report=Surf.waves(self)
        self.assertIsNotNone(report)
print("work")
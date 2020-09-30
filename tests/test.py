import unittest
from classes import Surf

class TestSurfClass(unittest.TestCase):
    def test_surf(self):
        report=Surf.surf_report(self)
        self.assertEqual(type(report),str)
print("work")
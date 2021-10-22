#!/usr/bin/python3
"""Unittest project 0x09. Python - Almost a Circle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class test_Base(unittest.TestCase):
    '''Testing base model'''

    def test_0_BaseInit(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base(None).id, 3)

    def test_0_Base_non_int(self):
        self.assertEqual(Base('thing').id, 'thing')
        self.assertEqual(Base([0, 1, 2]).id, [0, 1, 2])


class test_Rect(unittest.TestCase):
    '''Testing Rectangles inherited from Model'''

    def test_1_RectInit(self):
        with self.assertRaises(TypeError):
            Rectangle()
            Rectangle(1)
            Rectangle(None, None)
            Rectangle((1, 2))
            Rectangle("2", "4")
            Rectangle([1, 2])
        rect = Rectangle(10, 2)
        self.assertEqual([rect.width, rect.height, rect.x, rect.y, rect.id],
                         [10, 2, 0, 0, 4])
        rect = Rectangle(2, 10, 3, 11, 33)
        self.assertEqual([rect.width, rect.height, rect.x, rect.y, rect.id],
                         [2, 10, 3, 11, 33])

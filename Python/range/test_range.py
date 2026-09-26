std_range = range

from .range_implementation import range
import unittest


class TestRange(unittest.TestCase):

    def test_positive_sequence(self):
        start = 0
        step = 1
        end = 5
        r = range(start, end, step)
        std_r = std_range(start, end, step)
        for i, num in enumerate(r):
            self.assertEqual(num, std_r[i])

    def test_negative_sequence(self):
        start = 5
        step = -1
        end = 0
        r = range(start, end, step)
        std_r = std_range(start, end, step)
        for i, num in enumerate(r):
            self.assertEqual(num, std_r[i])

    # def test_listify(self):
    #     self.assertEqual(list[range(3)], [0,1,2])

    def test_end_not_included(self):
        start = 0
        end = 5
        step = 1
        self.assertEqual([i for i in range(start, end, step)][-1], end-1)

    def test_index_access(self):
        start = 0
        end = 5
        r = range(start, end)
        self.assertEqual(r[0], 0)
        self.assertEqual(r[2], 2)

    def test_len(self):
        self.assertEqual(len(range(1)), 1)
        self.assertEqual(len(range(2)), 2)
        self.assertEqual(len(range(0, 10, 2)), 5)
        self.assertEqual(len(range(0, 9, 2)), 5)
        self.assertEqual(len(range(1,0,-1)), 1)
        self.assertEqual(len(range(10, 0, 1)), 0)
        self.assertEqual(len(range(0, 0, 1)), 0)

    def test_index_access_negative(self):
        start = 0
        end = 5
        r = range(start, end)
        self.assertEqual(r[-1], 4)

    def test_out_of_range(self):
        self.assertRaises(IndexError, range.__getitem__, range(10), 10)
        self.assertRaises(IndexError, range.__getitem__, range(10), -11)
        self.assertRaises(IndexError, range.__getitem__, range(10, 0, -1), 10)
        self.assertRaises(IndexError, range.__getitem__, range(10, 0, -1), -11)
        self.assertRaises(IndexError, range.__getitem__, range(10, 0), 0)

    def test_reloads_after_first_use(self):
        r = range(5)
        for i in r:
            pass
        self.assertEqual([i for i in r], [0,1,2,3,4])

    def test_raises_if_zero_args(self):
        self.assertRaises(TypeError, range)

    def test_raises_if_gt_3_args(self):
        self.assertRaises(TypeError, range, 0, 5, 3, 4)

    def test_raises_if_step_0(self):
        self.assertRaises(ValueError, range, 0, 5, 0)

    def test_args_integers_only(self):
        self.assertRaises(TypeError, range, 0.5, 2, 2)
        self.assertRaises(TypeError, range, 0, 0.7, 1)
        self.assertRaises(TypeError, range, 0, 9, 0.3)

    def test_repr_if_1_or_2_arg(self):
        r = range(5)
        self.assertEqual(str(r), 'range(0, 5)')
        r = range(0, 5)
        self.assertEqual(str(r), 'range(0, 5)')

    def test_repr_if_step(self):
        r = range(0, 5, 3)
        self.assertEqual(str(r), 'range(0, 5, 3)')

    def test_immutable(self):
        r = range(5)
        self.assertRaises(AttributeError, setattr, r, 'step', 3)
        self.assertRaises(AttributeError, setattr, r, 'start', 3)
        self.assertRaises(AttributeError, setattr, r, 'stop', 3)

    def test_index_returns_correct_if_in_range(self):
        r = range(2, 10, 2)
        self.assertEqual(r.index(6), 2)
        self.assertEqual(r.index(2), 0)
        self.assertEqual(r.index(8), 3)

    def test_index_raises_if_not_in_sequence(self):
        r = range(2, 10, 2)
        self.assertRaises(ValueError, r.index, 9.2)

    def test_index_raises_if_out_of_range(self):
        r = range(2, 10, 2)
        self.assertRaises(ValueError, r.index, 10)
        self.assertRaises(ValueError, r.index, 9)
        self.assertRaises(ValueError, r.index, 7)
        self.assertRaises(ValueError, r.index, 1)
        r = range(10, 2, -2)
        self.assertRaises(ValueError, r.index, 11)
        self.assertRaises(ValueError, r.index, 2)
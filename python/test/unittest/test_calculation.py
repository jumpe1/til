import unittest
import calculation

release_name = 'lesson'


class CalTest(unittest.TestCase):

    def setUp(self):
        """テスト前にしたい処理"""

        print('setup')
        self.cal = calculation.Cal()

    def tearDown(self):
        """テスト後にしたい処理"""

        print('clean up')
        del self.cal

    # テストをスキップしたいときはデコレータで指定
    # @unittest.skip('skip!')
    @unittest.skipIf(release_name == 'lesson', 'skip!')
    def test_add_num_and_double(self):
        self.assertEqual(self.cal.add_num_and_double(1, 1), 4)
        """
        assertNotEqual(a, b)    a != b
        assertTrue(x)    bool(x) is True 
        assertFalse(x)  bool(x) is False
        など
        """

    def test_add_num_and_double_raise(self):
        # 例外処理
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')


if __name__ == '__main__':
    unittest.main()

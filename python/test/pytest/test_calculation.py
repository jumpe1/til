import pytest
import calculation

is_release = True


# todo pytestディレクトリに__init__.pyがあるとエラーになった
# 参考 https://www.blog.umentu.work/cannot-pytest/

# unittestと違いpytestではunittest.TestCaseを継承する必要がない
def test_add_num_and_double():
    cal = calculation.Cal()

    assert cal.add_num_and_double(1, 1) == 4
    # ok

    # assert cal.add_num_and_double(1, 1) != 4
    # bad

class TestCal(object):

    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()

    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal

    def setup_method(self, method):
        """テスト前にしたい処理"""

        print('method={}'.format(method.__name__))
        # setup_classを作ればいらない
        # self.cal = calculation.Cal()

    def teardown_method(self, method):
        """テスト後にしたい処理"""

        print('method={}'.format(method.__name__))
        # teardown_classを作ればいらない
        # del self.cal

    def test_add_num_and_double2(self, request):

        assert self.cal.add_num_and_double(1, 1) == 4

        # pytest test_calculation.py --os-name=mac -s
        os_name = request.config.getoption('--os-name')
        print(os_name)
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')

    def test_add_num_and_double3(self, tmpdir):

        assert self.cal.add_num_and_double(1, 1) == 4

        # pytestのfixture
        print(tmpdir)

    # テストスキップ
    # @pytest.mark.skip(reason='skip!')
    # @pytest.mark.skip(is_release==True, reason='skip!')
    def test_add_num_and_double_raise(self):
        # 例外処理
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')
            # ok

            # self.cal.add_num_and_double(1, 1)
            # bad


#
#     # テストをスキップしたいときはデコレータで指定
#     # @unittest.skip('skip!')
#     @unittest.skipIf(release_name == 'lesson', 'skip!')
#     def test_add_num_and_double(self):
#         self.assertEqual(self.cal.add_num_and_double(1, 1), 4)
#         """
#         assertNotEqual(a, b)    a != b
#         assertTrue(x)    bool(x) is True
#         assertFalse(x)  bool(x) is False
#         など
#         """

if __name__ == '__main__':
    pytest.main()

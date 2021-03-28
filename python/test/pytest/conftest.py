# pytestではtestのあるディレクトリにconftest.pyがあれば最初に見る

def pytest_addoption(parser):
    parser.addoption('--os-name',  default='linux', help='os name')
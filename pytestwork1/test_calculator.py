import pytest
import yaml
import os, sys
path = sys.path[0]
for i in range(1): path = os.path.dirname(path)
sys.path.append(path)
from pythoncode.calculator import Calculator

def get_datas():
    with open('./data.yml') as f:
        datas = yaml.safe_load(f)
        add_datas = datas["datas"]
        add_ids = datas["ids"]
        return [add_datas,add_ids]

class TestCalc:
    def setup_class(self):
        #实例化类，生成类的对象
        self.calc = Calculator()

    def setup_method(self):
        print("开始计算")
    def teardown_method(self):
        print("\n计算结束")
    #使用参数化
    @pytest.mark.parametrize("a,b,expect",get_datas()[0][0],ids=get_datas()[1][0])
    #测试add函数
    def test_add(self,a,b,expect):
        result = self.calc.add(a,b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect",get_datas()[0][1],ids=get_datas()[1][1])
    # 测试sub函数
    def test_sub(self,a,b,expect):
        result =self.calc.sub(a,b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect",get_datas()[0][2],ids=get_datas()[1][2])
    # 测试mul函数
    def test_mul(self,a,b,expect):
        result = self.calc.mul(a,b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect",get_datas()[0][3],ids=get_datas()[1][3])
    #测试div函数
    def test_div(self,a,b,expect):
        result = self.calc.div(a,b)
        assert result == expect

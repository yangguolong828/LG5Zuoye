import sys
import pytest
import yaml
import os

path = sys.path[0]
for i in range(1): path = os.path.dirname(path)
sys.path.append(path)

from pythoncode.calculator import Calculator

#通过 os.path.dirname获取当前文件所在目录的路径
yaml_file_path = os.path.dirname(__file__) + "/datanew.yml"


with open(yaml_file_path) as f:
    datas = yaml.safe_load(f)
    #获取文件中key为add_datas的数据
    add_datas = datas["addition_datas"]
    # 获取文件中key为add_ids的数据
    add_ids = datas["addition_ids"]
    # 获取文件中key为sub_datas的数据
    sub_datas = datas["subtraction_datas"]
    # 获取文件中key为sub_ids的数据
    sub_ids = datas["subtraction_ids"]
    # 获取文件中key为mul_datas的数据
    mul_datas = datas["multiplication_datas"]
    # 获取文件中key为mul_ids的数据
    mul_ids = datas["multiplication_ids"]
    # 获取文件中key为div_datas的数据
    div_datas = datas["division_datas"]
    # 获取文件中key为div_ids的数据
    div_ids = datas["division_ids"]

@pytest.fixture(scope="module")
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc


@pytest.fixture(params=add_datas)
def get_add_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")

@pytest.fixture(params=sub_datas)
def get_sub_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")

@pytest.fixture(params=mul_datas, ids=mul_ids)
def get_mul_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")


@pytest.fixture(params=div_datas)
def get_div_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")

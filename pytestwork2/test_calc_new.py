import pytest


class TestCalc:


    @pytest.mark.flaky(reruns=1,reruns_delay=2)
    @pytest.mark.run(order=1)
    # 测试add函数
    def test_add(self,get_calc,get_add_datas):
        try:
            # 调用add函数，返回的结果保存在result里面
            result = get_calc.add(get_add_datas[0],get_add_datas[1])
            if isinstance(result, float):
                result = round(result,2)
        except Exception as e:
            print(e)
        #判断result结果是否等于期望的值
        assert result == get_add_datas[2]


    @pytest.mark.run(order=4)
    # 测试div函数
    def test_div(self, get_calc, get_div_datas):
        try:
            # 调用div函数，返回的结果保存在result里面
            result = get_calc.div(get_div_datas[0], get_div_datas[1])
            if isinstance(result, float):
                result = round(result,2)
        except Exception as e:
            print(e)
        #判断result结果是否等于期望的值
        assert result == get_div_datas[2]

    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    @pytest.mark.run(order=2)
    # 测试sub函数
    def test_sub(self, get_calc, get_sub_datas):
        try:
            # 调用sub函数，返回的结果保存在result里面
            result = get_calc.sub(get_sub_datas[0], get_sub_datas[1])
            if isinstance(result, float):
                result = round(result,2)
        except Exception as e:
            print(e)
        #判断result结果是否等于期望的值
        assert result == get_sub_datas[2]


    @pytest.mark.run(order=3)
    # 测试mul函数
    def test_mul(self,get_calc,get_mul_datas):
        try:
            # 调用mul函数，返回的结果保存在result里面
            result = get_calc.mul(get_mul_datas[0],get_mul_datas[1])
            if isinstance(result, float):
                result = round(result,2)
        except Exception as e:
            print(e)
        #判断result结果是否等于期望的值
        assert result == get_mul_datas[2]



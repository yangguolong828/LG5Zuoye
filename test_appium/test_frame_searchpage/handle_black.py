import yaml


def handle_black(fun):
    def run(*args, **kwargs):
        parameter = args[0]
        with open("../black_list.yaml", "r", encoding="utf-8") as f:
            black_lists = yaml.load(f, Loader=yaml.FullLoader)
        # 捕获异常（元素没有找到）
        try:
            # 如果找到元素，返回
            return fun(*args, **kwargs)
        except Exception as e:
            # 遍历黑名单
            for black in black_lists:
                # 如果发现黑名单元素存在，对元素进行处理
                eles = parameter.driver.find_elements(*black)
                if len(eles) > 0:
                    # 通过点击的方式关闭弹窗
                    eles[0].click()
                    # 再次查找
                    return fun(*args, **kwargs)
            raise e
    return run
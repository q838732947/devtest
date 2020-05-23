import json

from jsonpath import jsonpath


def test():
    with open("./test_jsonpath.json") as f:
        print()
        j = json.load(f)
        # # 所有书的title[]
        # print(jsonpath(j, '$.store.book[*].title'))
        # print(jsonpath(j, '$..title'))
        # # 最后一本书，索引从0开始
        # print(jsonpath(j, '$..book[(@.length-1)]'))
        # # 第一本书的title
        # print(jsonpath(j, '$.store.book[0].title'))
        # 价格小于10的所有书的作者，使用'@'符号表示当前的对象，?(<判断表达式>) 使用逻辑表达式来过滤。
        # print(jsonpath(j, '$.store.book[?(@.price < 10)].title'))
        # print(jsonpath(j, '$.store..price'))
        #
        # # jsonpath找到了返回元素，找不到返回False
        # print(json.dumps(j, indent=2))

        j = {'errcode': 0, 'errmsg': 'ok', 'tag_group': [
            {'group_id': 'et4m93DAAA0lXsZlWX6hjxuexI4fekuw', 'group_name': 'test', 'create_time': 1590247405, 'tag': [
                {'id': 'et4m93DAAAeuCX_sI8p7x3yGPb2KsSfA', 'name': 'zhangsan', 'create_time': 1590247405, 'order': 0}],
             'order': 0}]}
        print(json.dumps(j, indent=2))
        result = jsonpath(json.dumps(j), expr='$.errcode')
        print(result)


if __name__ == '__main__':
    test()

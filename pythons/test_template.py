import json
from string import Template

import yaml


def test():
    with open("./test_template.yaml")as f:
        s = yaml.load(f)
        print(s)
        s = json.dumps(s)
        author = "chenling"
        print(Template(s).substitute(author=author))


def test2():
    s1 = Template('$who likes $what ')
    print(s1.substitute(who='tim',what='hhhhh'))

def test3():
    d = dict(who='java')
    print(Template('$who need $100').safe_substitute(d))
    print(Template('$who need $100').substitute(d))

if __name__ == '__main__':
    test2()

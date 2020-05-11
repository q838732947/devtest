import yaml


def write():
    a = {'name': 'Silenthand Olleander',
         'race': 'Human',
         'traits': ['ONE_HAND', 'ONE_EYE']
         }
    with open("yaml.yaml", "w") as f:
        yaml.dump(a, f)
    print(yaml.load(open("yaml.yaml", "r")))


def read():
    with open("yaml.yaml", "r") as f:
        s = yaml.load(f)
        print(s)


read()

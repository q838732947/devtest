import os
import time

import yaml

SEP = "*" * 20


def cmds_steps():
    with open("step.yml") as f:
        steps = yaml.safe_load(f)
    print(steps)
    for step in steps:
        start_time = time.time()
        print(SEP, step["comment"], SEP)
        os.system(step["cmd"])
        print(step["comment"], f"exe time {time.time() - start_time}s")


if __name__ == '__main__':
    cmds_steps()

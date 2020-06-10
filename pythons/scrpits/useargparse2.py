import argparse

parser = argparse.ArgumentParser()
parser.add_argument('name')
parser.add_argument('-re', required=True)
parser.add_argument('--male', choices=['man', 'women'], dest='gender')
result = parser.parse_args()
print(result)

import json
import sys


values = sys.argv[1]
tests = sys.argv[2]
report = sys.argv[3]

with open(values, 'r') as file1:
    values_data = json.load(file1)

with open(tests, 'r') as file2:
    tests_data = json.load(file2)


values_dct = {}
for value in values_data['values']:
    values_dct[value['id']] = value['value']


def update_values(param):
    if param['id'] in values_dct:
        param['value'] = values_dct[param['id']]
    if 'values' in param:
        for result in param['values']:
            update_values(result)

for item in tests_data['tests']:
    update_values(item)

with open(report, 'w') as file3:
    json.dump(tests_data, file3, indent=1)

print("Готово")











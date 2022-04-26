import json
import os

ages_file = './ages.json'

if os.path.isfile(ages_file) and os.stat(ages_file).st_size > 0:
    old_file = open(ages_file, 'r+')
    data = json.loads(old_file.read())
    print("Age is", data["age"], "-- adding a year.")
    data["age"] += 1
    print("New age is", data["age"])
else:
    old_file = open(ages_file, 'w+')
    data = {"name": "Roger", "age": 45}
    print("No file found, setting default age to", data["age"])
    old_file.write(json.dumps(data))

old_file.seek(0)
old_file.write(json.dumps(data))
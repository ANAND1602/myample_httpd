#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import json

with open("/runner/project/output.json") as json_file:
    new_inventory = json.load(json_file)
    print(json.dumps(new_inventory))


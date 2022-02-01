#!/usr/bin/env python3

import os
import sys

base = sys.argv[1]

group = 0
for n in range(2500000):
	if n % 10000 == 0:
		group += 1
		print(f"group {group}")
		os.makedirs(base + "/" + str(group), exist_ok=True)
	with open(base + "/" + str(group) + "/" + str(n), "wb") as f:
		pass

#!/usr/bin/env python3

import os
import sys
import random

base = sys.argv[1]

ids = list(range(2500000))
random.shuffle(ids)
exists = set()
for count, n in enumerate(ids):
	if count % 10000 == 0:
		print(f"count {count}")

	group = n % 10000
	if group not in exists:
		os.makedirs(base + "/" + str(group), exist_ok=True)
		exists.add(group)
	with open(base + "/" + str(group) + "/" + str(n), "wb") as f:
		pass

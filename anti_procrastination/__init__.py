import os
from typing import List

sites_all: List[str] = []
dir = "anti_procrastination/lists"
for root, dirs, files in os.walk(dir):
    for file in files:
        with open(f"{dir}/{file}", "r") as f:
            sites_all += f.readlines()

sites_cleaned = [site.rstrip() for site in sites_all]
output = list(set(sites_cleaned))

output_file = "sites-all.txt"
f = open(output_file, "a+")
f.write("\n".join(output))
f.close()
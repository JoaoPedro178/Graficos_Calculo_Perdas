import os
import subprocess
import pandas as pd
import numpy as np

src = os.listdir('testando')

#for i in range(100):
#    subprocess.Popen(f"echo '{i}' > testando/arquivo{i}.txt", shell=True)

for file in src:
    subprocess.Popen(f"cat testando/{file}", shell=True)
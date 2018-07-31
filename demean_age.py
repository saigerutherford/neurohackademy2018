import sys
import numpy as np
import pandas as pd

df = pd.read_csv(sys.argv[1], sep='\t')

mean_age = df.age.mean()

assert mean_age < 100
assert mean_age > 10

np.savetxt("demeaned_" + sys.argv[1], df.age-mean_age)

print("done!")

import df_utils as df
import pandas as pd
import numpy as np

# created to run test on modules to ensure they function properly in my local
# environment.

test_df = pd.DataFrame(np.ones([10,10]))
train = df.tvt_split(test_df)
print(train)

import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/data.csv'

# Load dataset
dataframe = pd.read_csv(url)
dataframe.head(2)
#    integer             datetime  category
# 0        5  2015-01-01 00:00:00         0
# 1        5  2015-01-01 00:00:01         0
dataframe.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 100 entries, 0 to 99
# Data columns (total 3 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   integer   100 non-null    int64
#  1   datetime  100 non-null    object
#  2   category  100 non-null    int64
# dtypes: int64(2), object(1)
# memory usage: 2.5+ KB

dataframe = pd.read_csv(url, parse_dates=["datetime"])
#    integer            datetime  category
# 0        5 2015-01-01 00:00:00         0
# 1        5 2015-01-01 00:00:01         0
dataframe.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 100 entries, 0 to 99
# Data columns (total 3 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   integer   100 non-null    int64
#  1   datetime  100 non-null    datetime64[ns]
#  2   category  100 non-null    int64
# dtypes: datetime64[ns](1), int64(2)
# memory usage: 2.5 KB

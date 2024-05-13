import pandas as pd

df = pd.DataFrame(
    data={
        "date": pd.date_range('1/1/2001', periods=100000, freq='h'),
    }
)
#                      date
# 0     2001-01-01 00:00:00
# 1     2001-01-01 01:00:00
# 2     2001-01-01 02:00:00
# 3     2001-01-01 03:00:00
# 4     2001-01-01 04:00:00
#                    ...
# 99995 2012-05-29 11:00:00
# 99996 2012-05-29 12:00:00
# 99997 2012-05-29 13:00:00
# 99998 2012-05-29 14:00:00
# 99999 2012-05-29 15:00:00
# [100000 rows x 1 columns]

# Select observations between two datetimes
df[(df['date'] > '2002-1-1 01:00:00') & (df['date'] <= '2002-1-1 04:00:00')]
#                     date
# 8762 2002-01-01 02:00:00
# 8763 2002-01-01 03:00:00
# 8764 2002-01-01 04:00:00

# Alternatively, set the date column as the DataFrame’s index and then slice using loc:
df = df.set_index(df['date'])
#                                    date
# date
# 2001-01-01 00:00:00 2001-01-01 00:00:00
# 2001-01-01 01:00:00 2001-01-01 01:00:00
# 2001-01-01 02:00:00 2001-01-01 02:00:00
# 2001-01-01 03:00:00 2001-01-01 03:00:00
# 2001-01-01 04:00:00 2001-01-01 04:00:00
#                                  ...
# 2012-05-29 11:00:00 2012-05-29 11:00:00
# 2012-05-29 12:00:00 2012-05-29 12:00:00
# 2012-05-29 13:00:00 2012-05-29 13:00:00
# 2012-05-29 14:00:00 2012-05-29 14:00:00
# 2012-05-29 15:00:00 2012-05-29 15:00:00
# [100000 rows x 1 columns]

df.loc['2002-1-1 02:00:00':'2002-1-1 04:00:00']  # The start and end indices are included
#                                    date
# date
# 2002-01-01 02:00:00 2002-01-01 02:00:00
# 2002-01-01 03:00:00 2002-01-01 03:00:00
# 2002-01-01 04:00:00 2002-01-01 04:00:00

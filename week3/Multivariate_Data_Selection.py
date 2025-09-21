import numpy as np
import pandas as pd

df = pd.read_csv("../nhanes_2015_2016.csv")

# df.head()
# print(df.head())

# SEQN	ALQ101	ALQ110	ALQ130	SMQ020	RIAGENDR	RIDAGEYR	RIDRETH1	DMDCITZN	DMDEDUC2	...	BPXSY2	BPXDI2	BMXWT	BMXHT	BMXBMI	BMXLEG	BMXARML	BMXARMC	BMXWAIST	HIQ210
# 0	83732	1.0	NaN	1.0	1	1	62	3	1.0	5.0	...	124.0	64.0	94.8	184.5	27.8	43.3	43.6	35.9	101.1	2.0
# 1	83733	1.0	NaN	6.0	1	1	53	3	2.0	3.0	...	140.0	88.0	90.4	171.4	30.8	38.0	40.0	33.2	107.9	NaN
# 2	83734	1.0	NaN	NaN	1	1	78	3	1.0	3.0	...	132.0	44.0	83.4	170.1	28.8	35.6	37.0	31.0	116.5	2.0
# 3	83735	2.0	1.0	1.0	2	2	56	3	1.0	5.0	...	134.0	68.0	109.8	160.9	42.4	38.5	37.7	38.3	110.1	2.0
# 4	83736	2.0	1.0	1.0	2	2	42	4	1.0	4.0	...	114.0	54.0	55.2	164.9	20.3	37.4	36.0	27.2	80.4	2.0
# [5 rows x 28 columns]

# df.dtypes
# print(df.dtypes)
# SEQN          int64
# ALQ101      float64
# ALQ110      float64
# ALQ130      float64
# SMQ020        int64
# RIAGENDR      int64
# RIDAGEYR      int64

keep = ['BMXWT', 'BMXHT', 'BMXBMI', 'BMXLEG', 'BMXARML', 'BMXARMC', 'BMXWAIST']
# keep2 = [column for column in df.columns if column.startswith('BMX')]
# keep3 = [column for column in df.columns if 'BMX' in column]

df_BMX = df[keep]
# df_BMX2 = df.loc[:,keep]

# pd.testing.assert_frame_equal(df_BMX, df_BMX2)

# print(df_BMX.head())
#    BMXWT  BMXHT  BMXBMI  BMXLEG  BMXARML  BMXARMC  BMXWAIST
# 0   94.8  184.5    27.8    43.3     43.6     35.9     101.1
# 1   90.4  171.4    30.8    38.0     40.0     33.2     107.9
# 2   83.4  170.1    28.8    35.6     37.0     31.0     116.5
# 3  109.8  160.9    42.4    38.5     37.7     38.3     110.1
# 4   55.2  164.9    20.3    37.4     36.0     27.2      80.4



# Selecting rows
waist_median = pd.Series.median(df_BMX['BMXWAIST'])

df_BMX_waist = df_BMX[df_BMX['BMXWAIST'] > waist_median]

# 두개의 조건을 동시에 만족하는 행 열

condition1 = df_BMX['BMXWAIST'] > waist_median
condition2 = df_BMX['BMXLEG'] < 32
df_BMX_condition1N2 = df_BMX[condition1 & condition2]

df_BMX3 = df_BMX.query('BMXWAIST > @waist_median & BMXLEG < 32')
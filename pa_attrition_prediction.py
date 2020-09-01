#기본 라이브러리 호출
import pandas as pd
import pandas_profiling
import numpy as np
import re
from matplotlib import pyplot as plt

#데이터 로드
df = pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv")
df.head()

#EDA
pandas_profiling.ProfileReport(df=df,minimal=True)

#EDA Result 
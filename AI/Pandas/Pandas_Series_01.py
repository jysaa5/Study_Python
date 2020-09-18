import pandas as pd

# Series
sr = pd.Series([17000, 18000, 1000, 5000],
               index=["피자", "치킨", "콜라", "맥주"])

print(sr)

print(sr.values)

print(sr.index)


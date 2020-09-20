import pandas as pd
import pandas_profiling

data = pd.read_csv(r'D:\workspace_Study\AI_Study\NLP_20200812\spam.csv', encoding='latin1')
print(data[:5])

# 프로파일링 결과 리포트를 pr에 저장
pr = data.profile_report()
# 바로 결과 보기
# data.profile_report()

pr.to_file('./pr_report.html')


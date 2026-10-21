from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parent
SRC=ROOT.parent
OUT=ROOT/'data'
OUT.mkdir(exist_ok=True)
files={
'priority':'09_Dashboard_Aggregates_2026-10-21-1917.csv',
'engagement':'05_Step.csv',
'plans':'06_Step.csv',
'adoption':'04_Step.csv',
'expiry':'07_Step.csv',
'kpis':'05.2_Step.csv',
'score_distribution':'08.1_Customer_Scoring_2026-10-21-1908.csv'
}
for k,f in files.items():
 d=pd.read_csv(SRC/f)
 if k=='adoption': d=d[(d.REGISTRATION_YEAR>=2017)&(d.TOTAL_GCPS>=20)].copy()
 if k=='expiry': d=d[d.EXPIRED_GCPS>=10].drop(columns=['MAX_DAYS_AFTER_EXPIRY']).copy()
 d.to_csv(OUT/f'{k}.csv',index=False)
print('Built aggregate-only CSVs:',', '.join(files))

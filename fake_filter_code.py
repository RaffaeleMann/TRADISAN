import pandas as pd

df = pd.read_csv('/home/luca/Scrivania/TRADISAN - FASE 1/fake.csv')

df_new = df[df['text'].str.contains('covid|coronavirus|vaccin.|cancro|tumore|dittatura sanitaria|autismo|salute|medicina|pandemia|lockdown|green pass|sarscov|sars-cov|pfizer|moderna|virus|alzheimer|farmaco|cura|aborto', case=False, na=False)]

df_new.to_csv('/home/luca/Scrivania/df_new.csv', index=False)

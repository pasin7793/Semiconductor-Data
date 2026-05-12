import pandas as pd
import numpy as np

# 데이터 불러오기
secom = pd.read_csv("secom.csv", sep=r"\s+", header=None)   # 공정 데이터
secom_labels = pd.read_csv("secom_labels.csv", sep=r"\s+", header=None) # 공정 데이터 라벨

secom.columns = [f"feature+{i}" for i in range(secom.shape[1])] # 공정 데이터 컬럼명 지정. shape[1] == 열의 갯수 # 0행 1열
secom_labels.columns = ["label", "datetime"]    # 공정 데이터 라벨 컬럼명 지정

df = pd.concat([secom, secom_labels], axis=1)   # 데이터를 '열'방향으로 이어 붙힘 

# print(df["label"].value_counts()) # "label" 데이터 값에 대한 갯수 -1 pass, 1 fail
# print(df[df["label"] == 1]) # 불량인 데이터 출력
# print(df["label"].value_counts(normalize=True) * 100) # 데이터 합격 / 불량 비율

# 결측치 확인
feature_cols = [col for col in df.columns if str(col).startswith("feature+")] # 'feature+' 로 시작하는 컬럼 묶음

# isnull() -> null이면 1, 데이터가 있으면 0
# sum() -> 합계 
# 둘이 합치면 마치 count()처럼 작동.

total_missing_data = df[feature_cols].isnull().sum().sum()
print("결측치 개수 : ",total_missing_data)

missing_feature_count = (df[feature_cols].isnull().sum() > 0).sum()
print("결측치가 있는 feature 개수:", missing_feature_count)

top20_missing_feature = df[feature_cols].isnull().sum().sort_values(ascending=False).head(20) # .sort_values(ascending=False) 내림차순
print("결측치가 많은 feature : ", top20_missing_feature)
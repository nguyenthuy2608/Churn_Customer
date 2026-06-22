import pandas as pd
import numpy as np
import joblib  # Thư viện dùng để load file .pkl
from sklearn.preprocessing import StandardScaler
# hàm để load dữ liệu cho EDA
def load_eda_data(file_path = "data_raw.csv", sep = ";"):
    df = pd.read_csv(file_path, sep=sep)
    return df
# hàm để load dữ liệu cho training
def load_training_data (file_path = "data_raw.csv", sep = ";"):
    df = load_eda_data(file_path, sep=sep)
    # 1. ONE-HOT ENCODING: 'Marital_Status' và 'Education_Level'
    df = pd.get_dummies(df, columns=["Marital_Status", "Education_Level"], dtype=int, drop_first=True)

    # 2. LABEL ENCODING: Churn (Existing = 0, Attrited = 1)
    df["Churn"] = df["Status"].map({
        "Existing Customer": 0,
        "Attrited Customer": 1
    })
    df.drop(columns=["Status"], inplace=True)

    # 3. LABEL ENCODING: Gender (Male = 0, Female = 1)
    df["Gender"] = df["Gender"].map({
        "M": 0, 
        "F": 1
    })

    # 4. XỬ LÝ & ENCODING: Income_Category
    # Thay thế Unknown bằng None
    df["Income_Category"] = df["Income_Category"].replace("Unknown", None) 
    
    # Tạo biến giả đánh dấu thu nhập không xác định (is_income_unknown)
    loc = df.columns.get_loc("Income_Category") + 1
    df.insert(loc, "is_income_unknown", df["Income_Category"].isna().astype(int))
    
    # Mã hóa các mức thu nhập thành số nguyên
    df["Income_Category"] = df["Income_Category"].map({
        "Less than $40K": 0,
        "$40K - $60K": 1,
        "$60K - $80K": 2,
        "$80K - $120K": 3,
        "$120K +": 4
    })
    
    # Điền các giá trị None còn lại bằng Mode (Giá trị phổ biến nhất)
    df["Income_Category"] = df["Income_Category"].fillna(df["Income_Category"].mode()[0])

    # 5. LABEL ENCODING: User_Level
    df["User_Level"] = df["User_Level"].map({
        "Blue": 0,
        "Silver": 1,
        "Gold": 2,  
        "Platinum": 3
    })
    return df
# hàm để load dữ liệu cho clustering
def load_clustering_data (file_path = "data_raw.csv"):
# 1. Tận dụng lại hàm load_training_data
    df = load_training_data(file_path).copy()
# 2. Khởi tạo và chuẩn hóa các biến số liên tục 
    scaler = StandardScaler()
    scale_features = ['Usage_Duration', 'Services_Used', 'Months_Inactive', 'Total_Spending', 'Total_Transaction']
    df[scale_features] = scaler.fit_transform(df[scale_features])
    return df 
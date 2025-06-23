import streamlit as st

def stdev(data): #標準偏差
    values = list(data.values())
    n = len(values)
    avg = sum(values) / n
    var = sum((x - avg) ** 2 for x in values) / n
    return var ** 0.5

def deviation_value(name, data): #偏差値
    values = list(data.values())
    avg = sum(values) / len(values)
    return (data[name] - avg) / stdev(data) * 10 + 50

#UI部分
st.title("偏差値計算")
data_input = st.text_area("データを辞書形式で入力（例：{\"A\":50,\"B\":65,\"C\":70,\"D\":30})")
name = st.text_input("調べたい偏差値（例：A）")

if st.button("計算"):
    try:
        data = eval(data_input)
        score = deviation_value(name, data)
        st.success(f"{name} の偏差値は {score:.2f} です")
    except:
        st.error("入力形式が正しくありません")

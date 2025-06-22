import streamlit as st

def stdev(data):
    values = list(data.values())
    n = len(values)
    avg = sum(values) / n
    var = sum((x - avg) ** 2 for x in values) / n
    return var ** 0.5

def deviation_value(name, data):
    values = list(data.values())
    avg = sum(values) / len(values)
    return (data[name] - avg) / stdev(data) * 10 + 50

# UI部分
st.title("偏差値計算ツール")
data_input = st.text_area("データを辞書形式で入力（例：{\"A\":56,\"B\":67})")
name = st.text_input("偏差値を調べる名前（例：A）")

if st.button("計算"):
    try:
        data = eval(data_input)
        score = deviation_value(name, data)
        st.success(f"{name} の偏差値は {score:.2f} です")
    except:
        st.error("入力形式が正しくありません")

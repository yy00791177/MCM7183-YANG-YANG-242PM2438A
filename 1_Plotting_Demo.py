

import time

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code


def plotting_demo():
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


st.set_page_config(page_title="绘图演示", page_icon="📈")
st.markdown("# 绘图演示")
st.sidebar.header("绘图演示")
st.write(
    """此演示演示了使用Streamlit进行绘图和动画的组合。我们正在循环生成一堆随机数，持续约5秒。享受!"""
)

plotting_demo()

show_code(plotting_demo)

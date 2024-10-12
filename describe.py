# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("MCM7183  YANG YANG 242PM2438A 👋")

    st.sidebar.success("MCM7183  YANG YANG 242PM2438A.")

    st.markdown(
        """
        
       - Animation_Demo
        此应用程序展示了如何使用Streamlit构建酷炫的动画。它显示基于Julia集的动画分形。使用滑块调整不同的参数.
       - Plotting_Demo
        此演示演示了使用Streamlit进行绘图和动画的组合。我们正在循环生成一堆随机数，持续约5秒。享受!
       - Mapping_Demo
       此演示显示了如何使用[`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)st.pydeck_chart显示地理空间数据.
       - DataFrame_Demo
       此演示展示了如何使用 `st.write` 可视化Pandas DataFrames.(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)
    """
    )


if __name__ == "__main__":
    run()

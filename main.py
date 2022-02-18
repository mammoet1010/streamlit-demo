import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

"""
### イテレーションバー
"""

"Start!!"

latest_iteration = st.empty() #空を追加
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f"Iteration {i + 1}")
  bar.progress(i + 1)
  time.sleep(0.001)

"Done!!!!"

"""
### データフレームの表示
"""

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

#st.dataframe(df, width = 1000, height = 1000) 
st.dataframe(df.style.highlight_max(axis=0))

st.write('マジックコマンドが書ける')

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

st.write('図はこうやって書く')

"""
`st.line_chart()`
`st.area_chart()`
`st.bar_chart()`
"""

df2 = pd.DataFrame(
  np.random.rand(20, 3),
  columns = ["a", "b", "c"]
)

st.dataframe(df2.style.highlight_max(axis=0))

st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

st.write('地図はこうやって書く')

"""
"lat"と"lon"のカラムに緯度経度を記述したデータフレームを用意
↓
`st.map(df)`
"""


df3 = pd.DataFrame(
  np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
  columns = ["lat", "lon"]
)

st.map(df3)


st.write('Display Image + チェックボックス') #本文

if st.checkbox('Show Image'):
  img = Image.open('Markdown.png') #画像のパス
  st.image(img, caption='MarkDown', use_column_width=True)


"""
### セレクトボックス
"""

st.selectbox(
  'あなたの好きな数字を教えてください',
  list(range(1, 11))
  
)

lis = list(range(10, 22))

option = st.selectbox(
  'あなたの好きな数字を教えてください',
  lis
  
)

"あなたの好きな数字は", option, "です"

"""
### テキストボックス
"""
text = st.text_input("あなたの趣味を教えてください")

"あなたの趣味は", text, "です"

"""
### スライダー
"""

condition = st.slider("あなたの今の調子は？", 0, 100, 50)

"あなたの調子は", condition, "です"



"""
### サイドバー
"""
st.sidebar.write("Sidebar")

text2 = st.sidebar.text_input("あなたの趣味を教えてください。")

"あなたの趣味は", text2

condition2 = st.sidebar.slider("あなたの今の調子はどう？", 0, 100, 50)

"あなたの調子は", condition2

"""
### 2カラムレイアウト
"""
left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button: 
  right_column.write("ここは右カラム")

"""
### エクスパンダー
"""
expander1 = st.expander("問い合わせ1")
expander1 = expander1.write("問い合わせ1の回答")
expander2 = st.expander("問い合わせ2")
expander2 = expander2.write("問い合わせ2の回答")
expander3 = st.expander("問い合わせ3")
expander3 = expander3.write("問い合わせ3の回答")










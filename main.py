import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')

'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)


for i in range(100):

    latest_iteration.text(f'Iteration {i+1}%')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!'

st.write('DataFrame')


df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.write(df)
st.dataframe(df, width=400, height=100)
st.dataframe(df.style.highlight_max(axis=0))
st.table(df.style.highlight_max(axis=0))
st.json(df.to_json())  # json形式で出力

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

st.text('あいうえお')
st.title('あいうえお')
st.markdown('#### 赤字')

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)

st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img, caption='sample', use_column_width=True)

option = st.selectbox('あなたの好きな数値を選択してください', list(range(1, 11)))

st.write('あなたの選択した数字は', option, 'です')

st.write('Interactive Widgets')

# text = st.text_input('あなたの趣味を教えてください')
# st.write('あなたの趣味は', text, 'です')

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# # st.write('コンディション：', condition)
# 'コンディション：', condition

# sidebar に表示
# text = st.sidebar.text_input('あなたの趣味を教えてください')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'あなたの趣味は', text, 'です'
# 'コンディション：', condition

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ1')
expander.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')


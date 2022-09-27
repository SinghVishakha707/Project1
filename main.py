import streamlit as st
import pandas as pd
import numpy as np
st.title('Vishakha Singh')

st.write("MSCDSAI")

st.header("Python")

st.caption('This is a string that explains something above.')

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

st.text('This is some text.')
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.area_chart(chart_data)

st.columns()

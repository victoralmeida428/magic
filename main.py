import streamlit as st
import pandas as pd

st.set_page_config(page_title='Magic - The Gathering',
                   page_icon='data\logo.png')

st.title('Magic: The Gathering')

df = pd.read_parquet('data\database.parquet')

nome = st.sidebar.selectbox('Card', options=df.name.unique())
imagens = [image for image in df.loc[df.name == nome, 'imageUrl'].unique() if image is not None]

# st.write(df.loc[df.name == nome])
cols = st.columns(len(imagens))
for i in range(len(imagens)):
    cols[i].image(imagens[i])


# df = df.explode('foreignNames')
st.write(df.loc[(df.name==nome)])



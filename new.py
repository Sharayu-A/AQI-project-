import streamlit as st

st.title(" Interactive Air Quality Insights")
st.markdown(
    """
    <iframe width="100%" height="400" src="https://app.powerbi.com/view?r=eyJrIjoiNGQ3NTZkY2ItNDZhYi00MjMyLWI3ZGQtODdhMzc2NzRhNDUxIiwidCI6IjkzZTljMTgyLTdhOWMtNGI4YS04YzY1LTM3OTMyNDZlYzgzMyJ9" frameborder="0" allowFullScreen="true"></iframe>
    """,
    unsafe_allow_html=True,
)


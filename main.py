import streamlit as st

from multiapp import MultiApp
from Models import Model1, Model2,Model3,Model4,Model5,Model6

app = MultiApp()



st.set_page_config(page_title="Dashboard", layout="wide")
st.subheader("Hello")
st.markdown("", unsafe_allow_html=True)


st.sidebar.image("Image/logo.png",caption="64 Squares LLC")



# Add all your application here
app.add_app("Medication Adherence", Model1.app)
app.add_app("NPS", Model2.app)
app.add_app("Obesity", Model3.app)
app.add_app("Prior Auth Final", Model4.app)
app.add_app("Prod Isolation", Model5.app)
app.add_app("PTO", Model6.app)
# The main app
app.run()


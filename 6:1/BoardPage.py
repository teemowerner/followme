import sys
import os
import streamlit as st
from streamlit_option_menu import option_menu
from st_on_hover_tabs import on_hover_tabs
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Follow Me!",
    page_icon="👋",
)
st.markdown("""
<style>
.big-font {
    font-size:60px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Welcome to Follow Me! 👋</p>', unsafe_allow_html=True)

st.markdown('<style>' + open('./style/side.css').read() + '</style>', unsafe_allow_html=True)
def select():
    with st.form('time'):
        time_slider = st.slider('',0,12,1)
        submitted = st.form_submit_button('Submit')
    
        if submitted:
            st.switch_page("pages/1_UserPage.py")
    
def ChangeWidgetFontSize(wgt_txt, wch_font_size = '12px'):
    htmlstr = """<script>var elements = window.parent.document.querySelectorAll('p'), i;
                for (i = 0; i < elements.length; ++i) 
                    { if (elements[i].textContent.includes(|wgt_txt|)) 
                        { elements[i].style.fontSize ='""" + wch_font_size + """'; } }</script>  """

    htmlstr = htmlstr.replace('|wgt_txt|', "'" + wgt_txt + "'")
    components.html(f"{htmlstr}", height=0, width=0)

tab_titles = ['Introduction', 'Check Time']
tabs = st.tabs(tab_titles)
ChangeWidgetFontSize(tab_titles[0], '15px')
ChangeWidgetFontSize(tab_titles[1], '20px')

with tabs[0]:
    st.markdown(
    """
    ##### **Follow me** recommends cafes, restaurants, and tourist attractions for my trip to Jeonju.
    ### Each page function
     - UserPage : 
     - SurveyPage : 
     - ChatPage :    
    """
)


    
with tabs[1]:
    st.markdown(
    """
    ### 🕰️ Please choose a time for your trip
    """
    )
    st.write(select())


        

        


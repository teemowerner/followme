from streamlit_extras.stylable_container import stylable_container 
import streamlit as st

def example():
    with stylable_container(
        key="green_button",
        css_styles="""
            button {
                background-color: green;
                color: white;
                border-radius: 20px;
            }
            """,
    ):
        st.button("Green button")

    st.button("Normal button")

    with stylable_container(
        key="container_with_border",
        css_styles="""
            {
                background-color: green;
                border: 1px solid rgba(49, 51, 63, 0.2);
                border-radius: 0.5rem;
                padding: calc(1em - 1px)
            }
            """,
    ):
        st.markdown("This is a container with a border.")

example()

# import streamlit as st
# import time
# css = """
# <style>
#     [data-testid="stForm"]:nth-child(4) {
#         background: LightBlue;
#         position: relative;
#         animation: slideIn 0.5s ease-out;
#     }
    
#     @keyframes slideIn {
#         from {
#             transform: translateX(100%);
#         }
#         to {
#             transform: translateX(0%);
#         }
#     }
# </style>
# """
# css2 = """
# <style>
#     [data-testid="stForm"]:nth-child(5) {
#         background: Pink;
#         position: relative;
#         animation: slideIn 0.5s ease-out;
#     }
    
#     @keyframes slideIn {
#         from {
#             transform: translateX(100%);
#         }
#         to {
#             transform: translateX(0%);
#         }
#     }
# </style>
# """
# css3 = """
# <style>
#     [data-testid="stForm"]:nth-child(6) {
#         background: LightGreen;
#         position: relative;
#         animation: slideIn 0.5s ease-out;
#     }
    
#     @keyframes slideIn {
#         from {
#             transform: translateX(100%);
#         }
#         to {
#             transform: translateX(0%);
#         }
#     }
# </style>
# """
# st.markdown(css, unsafe_allow_html=True)
# st.markdown(css2, unsafe_allow_html=True)
# st.markdown(css3, unsafe_allow_html=True)




# # 첫 번째 폼
# with st.form(key="My form_1"):
#     first = st.text_input("First name")
#     last = st.text_input("Last name")
#     if st.form_submit_button("Submit"):
#         st.write(first + " " + last)
# time.sleep(1)

# with st.form(key="My form_2"):
#     first = st.text_input("First name")
#     last = st.text_input("Last name")
#     if st.form_submit_button("Submit"):
#         st.write(first + " " + last)
# time.sleep(1)

# with st.form(key="My form_3"):
#     first = st.text_input("First name")
#     last = st.text_input("Last name")
#     if st.form_submit_button("Submit"):
#         st.write(first + " " + last)
# # 스타일링 코드


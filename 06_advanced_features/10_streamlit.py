import streamlit as st

# 设置页面配置信息
st.set_page_config(
    page_title="easonchan.net",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
# 标题：_xxx_表示斜体；：blue[xxx]表示蓝色 :xxx:表示emoji
st.title("_This is a :blue[title]_ :sunglasses:")

# 显示文本
st.write("Hello, Fear and Dreams!")

# 显示图片
st.image("https://www.easonchan.net/hk/wp-content/uploads/2022/09/Eason-Concert-Horizontal-01-2-3c.jpg")
# 显示视频
st.video(
    "https://scontent-sin6-4.cdninstagram.com/v/t51.36329-15/347068208_147837701597778_6032578291169025634_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=8ae9d6&_nc_ohc=eXsGlnAVLqcAX-gUeaY&_nc_ht=scontent-sin6-4.cdninstagram.com&edm=ANo9K5cEAAAA&oh=00_AfBkhr9QLVnFL9CDsWNdpBxBN0PE_yLJYjpEpra2CHoWgw&oe=6473DEBD")

# 显示图表
st.line_chart([1, 20, 30, 32, 7, 18])
# 显示进度条
st.progress(0.1)
# 显示进度条
st.progress(0.5)
# 显示进度条
st.progress(1.0)

# 输入框
name = st.text_input("What is your name?")

# 聊天
st.chat_message("user").write("Hello, World!")
st.chat_message("assistant").write("Hi, How can I help you?")
st.chat_message("user").write("I want to know more about Streamlit.")
st.chat_message("assistant").write("Sure, what do you want to know?")

# 聊天输入框
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

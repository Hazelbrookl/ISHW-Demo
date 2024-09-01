import streamlit as st
import pandas as pd
import json

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
periods = ['第1节\n08:00-09:35', '第2节\n09:50-12:15', '第3节\n13:30-15:05', '第4节\n15:20-16:55', '第5节\n17:05-18:40', '第6节\n19:20-21:45']

df = pd.read_csv('data/course_data.csv')
df_timetable = pd.DataFrame(index=periods, columns=days)
df_owncourse = pd.read_csv('data/own_course.csv')

def remove_dollarsigns(x):
    if isinstance(x, str):
        return x.strip("$")
    return x

def call_back_viewCourseDetail(index):
    st.session_state.detail_index = index

for _, course in df.iterrows():
    c_period = course['上课时间'].strip("$")
    c_period = c_period.split("-")
    c_info = f"{course['课程名']}"
    df_timetable.at[periods[int(c_period[1]) - 1], days[int(c_period[0]) - 1]] = c_info

df_owncourse['课程编号'] = df_owncourse['课程编号'].apply(remove_dollarsigns)
df_owncourse['上课时间'] = df_owncourse['上课时间'].apply(remove_dollarsigns)
df_owncourse['课序号'] = df_owncourse['课序号'].astype(str)
df_owncourse['学分'] = df_owncourse['学分'].astype(str)
df_owncourse['起始周'] = df_owncourse['起始周'].astype(str)
df_owncourse['结束周'] = df_owncourse['结束周'].astype(str)
df_timetable.fillna("", inplace=True)
df_owncourse.index += 1



if __name__ == "__main__":

    st.set_page_config(
        page_title="My Tsinghua Homepage",
        page_icon="",
         layout="wide",
    )
    if "detail_index" not in st.session_state:
        st.session_state.detail_index = 0

    st.markdown('<h1 style="color: #5c307d;">创意软件</h1>', unsafe_allow_html=True)

    tab_guide, tab_info, tab_timetable, tab_owncourse = st.tabs(["作业介绍","个人主页", "整体课表", "课程资源"])

    with tab_guide:
        st.header("作业介绍")
        st.markdown("要求使用python开源框架streamlit构建一个静态/可交互的数据信息创意展示页面。Streamlit是一个专门用于数据科学展示的开源框架，\
                    优点是无需深入学习复杂的前端开发技术也可轻松地创建交互式的Web应用。其渲染逻辑简单，每次刷新由上至下执行符合条件的所有语句，\
                    用近似“搭积木”的形式简单拼装出一个完整页面。")
        st.header("作业要求")
        st.markdown("test")
        st.header("环境配置")
        st.markdown("- **Visual Studio Code**：在电脑上安装VSCode以编辑和运行代码。")
        st.markdown("- **Python**：在电脑上安装Python解释器。")
        st.markdown("- **参考**：https://www.sohu.com/a/769613173_121124362")
        st.header("上手教程")
        st.subheader("安装依赖")
        st.markdown("在StreamlitDemo文件夹下打开终端，运行以下代码，确保依赖已满足：")
        st.code("pip install -r requirements.txt")
        st.subheader("文件结构")
        st.markdown("- main.py为主程序，所有用于页面组件的Python代码均在其中编写。")
        st.markdown("- /data文件夹中存放了数据文件，如课程信息和个人头像等。")
        st.markdown("- /.streamlit文件夹存放了部分配置，无需修改。")
        st.subheader("本地运行")
        st.markdown("在StreamlitDemo文件夹下打开终端，运行以下代码，即可本地运行Streamlit：")
        st.code("streamlit run main.py")
        st.markdown("可以通过浏览器输入 http://localhost:8501/ 查看当前页面，内容与此处完全相同。此后即可通过本地运行查看修改代码后的效果。")
        st.subheader("组件使用")
        st.markdown("**Streamlit官方组件文档**：https://docs.streamlit.io/")
        st.markdown("**中文版**：https://blog.csdn.net/weixin_44458771/article/details/135495928")
        st.header("快速部署")
        st.markdown("开发完成之后，要通过应用部署将编写好的软件放到服务器上，让其他人可以通过互联网或局域网来使用这个软件。其他人无法通过localhost来访问你开发好的页面，\
                    但将其部署在test之后，大家就都可以访问了。")
        st.markdown("Streamlit提供了云服务器和方便的部署方式，可以快速地部署你的页面。")
        st.subheader("部署流程")
        st.markdown("- 1.注册**Github**账户，将完整的代码和数据文件上传至一个新的Github仓库，需保证主文件和配置文件位置与初始一致。")
        st.markdown("- 2.前往Streamlit官网 https://streamlit.io/ 注册账号，按照 https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app \
                    流程指引，链接Github仓库发布应用。")


    with tab_info:
        st.subheader("个人信息")
        col1, col2 = st.columns([2,5])
        col1.image("data/avatar.jpg", width=200)
        with col2.container():
            col2_1, col2_2 = st.columns(2)
            col2_1.markdown("**姓名**：软小宣")
            col2_2.markdown("**年龄**：23")
            col2_1, col2_2 = st.columns(2)
            col2_1.markdown("**性别**：无")
            col2_2.markdown("**种族**：猴")
            col2_1, col2_2 = st.columns(2)
            col2_1.markdown("**学校**：清华大学")
            col2_2.markdown("**专业**：软件工程")
            col2_1, col2_2 = st.columns(2)
            col2_1.markdown("**爱好**：编程、吃香蕉")
            col2_2.markdown("**梦想**：Life-Long Learning")
            col2_1, col2_2 = st.columns(2)
            col2_1.markdown("**Tel**：xxxxxxxxxxx")
            col2_2.markdown("**E-Mail**：ruan24@mails.tsinghua.edu.cn")
            col2_1, col2_2 = st.columns(2)
            col2_1.markdown("**地址**：北京市海淀区清华大学东配楼11-421")
            col2_2.markdown("**座右铭**：自强不息，厚德载物")

        st.write("大家好，我叫软小宣，欢迎访问我的个人页面。我是清华大学软件学院的吉祥物，陪伴同学们一起在清华园里学习生活。我平时最爱做的事情就是写程序，我学习过包括C、C++、Java、Python等多种编程语言以及各种信息领域前沿技术。目前我选修了刘璘老师开设的创意软件课程，期待与大家在见面，度过一段开心的时光。也希望大家在课余时间多找我玩。")

    with tab_timetable:
        st.subheader("学期课表")
        st.dataframe(df_timetable, use_container_width=True)
        csv_download = df_timetable.to_csv().encode('utf-8')
        st.download_button(
            label="获取我的课表",
            data=csv_download,
            file_name='timetable_Ruanxx.csv',
            mime='text/csv',
        )

    with tab_owncourse:
        st.subheader("本院开课")
        st.dataframe(df_owncourse[['课程名', '课程编号', '课序号', '学分', '任课教师', '上课时间']], use_container_width=True, height=400)
        index_input = st.number_input(min_value=1,max_value=len(df_owncourse),label="查找详情",placeholder="输入序号")
        st.button("查看", on_click=lambda: call_back_viewCourseDetail(index_input))

        if st.session_state.detail_index != 0:
            course = df_owncourse.iloc[st.session_state.detail_index - 1]
            course_dict = course.to_dict()
            course_json = json.dumps(course_dict, ensure_ascii=False)
            st.json(course_json, expanded=2)
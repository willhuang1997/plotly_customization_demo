import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

@st.experimental_memo
def get_chart_1111():
    st.header("Define a custom colorscale")
    df = px.data.iris() # replace with your own data source
    fig = px.scatter(
            df, x="sepal_width", y="sepal_length", 
            color="sepal_length", color_continuous_scale="reds"
    )
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    get_chart_1111()
except Exception as e:
    st.exception(e)

@st.experimental_memo
def get_chart_3333():
    st.header("")
    df = px.data.gapminder()
    df_2007 = df.query("year==2007")

    fig = px.scatter(
            df_2007,
            x="gdpPercap", y="lifeExp", size="pop", color="continent",
            log_x=True, size_max=60,
            template="plotly_dark", title="Gapminder 2007: 'plotly_dark' theme"
    )
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)


try:
    get_chart_3333()
except Exception as e:
    st.exception(e)

st.title("Modifying the grid...")

@st.experimental_memo
def get_chart_4444():
    st.header("No grid")
    fig = px.line(y=[1, 0])
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    get_chart_4444()
except Exception as e:
    st.exception(e)

@st.experimental_memo
def get_chart_5555():
    st.header("Only vertical grid")
    fig = px.line(y=[1, 0])
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=False)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    get_chart_5555()
except Exception as e:
    st.exception(e)

@st.experimental_memo
def get_chart_5555():
    st.header("Only horizontal grid")
    fig = px.line(y=[1, 0])
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    get_chart_5555()
except Exception as e:
    st.exception(e)

@st.experimental_memo
def get_chart_6666():
    st.header("Both grid")
    fig = px.line(y=[1, 0])
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    get_chart_6666()
except Exception as e:
    st.exception(e)

@st.experimental_memo
def get_chart_7777():
    st.header("Log axis")
    df = px.data.gapminder().query("year == 2007")

    fig = px.scatter(df, x="gdpPercap", y="lifeExp", hover_name="country", log_x=True)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    get_chart_7777()
except Exception as e:
    st.exception(e)
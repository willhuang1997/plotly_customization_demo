import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import inspect

@st.experimental_memo
def get_chart_99416():
    import plotly.express as px
    import pandas as pd
    
    df = pd.DataFrame([
        dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
        dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
        dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')
    ])
    
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task")
    fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_99416))
    get_chart_99416()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_67608():
    import plotly.express as px
    import pandas as pd
    
    df = pd.DataFrame([
        dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Resource="Alex"),
        dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource="Alex"),
        dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Resource="Max")
    ])
    
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource")
    fig.update_yaxes(autorange="reversed")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_67608))
    get_chart_67608()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_63243():
    import plotly.express as px
    import pandas as pd
    
    df = pd.DataFrame([
        dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Completion_pct=50),
        dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Completion_pct=25),
        dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Completion_pct=75)
    ])
    
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Completion_pct")
    fig.update_yaxes(autorange="reversed")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_63243))
    get_chart_63243()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_23826():
    import plotly.express as px
    import pandas as pd
    
    df = pd.DataFrame([
        dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Resource="Alex"),
        dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource="Alex"),
        dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Resource="Max")
    ])
    
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Resource")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_23826))
    get_chart_23826()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_56013():
    import plotly.figure_factory as ff
    
    df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
          dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
          dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]
    
    fig = ff.create_gantt(df)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_56013))
    get_chart_56013()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_81438():
    import plotly.figure_factory as ff
    
    df = [dict(Task="Job-1", Start='2017-01-01', Finish='2017-02-02', Resource='Complete'),
          dict(Task="Job-1", Start='2017-02-15', Finish='2017-03-15', Resource='Incomplete'),
          dict(Task="Job-2", Start='2017-01-17', Finish='2017-02-17', Resource='Not Started'),
          dict(Task="Job-2", Start='2017-01-17', Finish='2017-02-17', Resource='Complete'),
          dict(Task="Job-3", Start='2017-03-10', Finish='2017-03-20', Resource='Not Started'),
          dict(Task="Job-3", Start='2017-04-01', Finish='2017-04-20', Resource='Not Started'),
          dict(Task="Job-3", Start='2017-05-18', Finish='2017-06-18', Resource='Not Started'),
          dict(Task="Job-4", Start='2017-01-14', Finish='2017-03-14', Resource='Complete')]
    
    colors = {'Not Started': 'rgb(220, 0, 0)',
              'Incomplete': (1, 0.9, 0.16),
              'Complete': 'rgb(0, 255, 100)'}
    
    fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True,
                          group_tasks=True)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_81438))
    get_chart_81438()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_1249():
    import plotly.figure_factory as ff
    
    df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Complete=10),
          dict(Task="Job B", Start='2008-12-05', Finish='2009-04-15', Complete=60),
          dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Complete=95)]
    
    fig = ff.create_gantt(df, colors='Viridis', index_col='Complete', show_colorbar=True)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_1249))
    get_chart_1249()
except Exception as e:
    st.exception(e)


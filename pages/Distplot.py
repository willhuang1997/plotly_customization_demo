import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import inspect

@st.experimental_memo
def get_chart_28502():
    import plotly.express as px
    df = px.data.tips()
    fig = px.histogram(df, x="total_bill", y="tip", color="sex", marginal="rug",
                       hover_data=df.columns)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_28502))
    get_chart_28502()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_77778():
    import plotly.express as px
    df = px.data.tips()
    fig = px.histogram(df, x="total_bill", y="tip", color="sex",
                       marginal="box", # or violin, rug
                       hover_data=df.columns)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_77778))
    get_chart_77778()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_62983():
    import plotly.figure_factory as ff
    import numpy as np
    np.random.seed(1)
    
    x = np.random.randn(1000)
    hist_data = [x]
    group_labels = ['distplot'] # name of the dataset
    
    fig = ff.create_distplot(hist_data, group_labels)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_62983))
    get_chart_62983()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_53456():
    import plotly.figure_factory as ff
    import numpy as np
    
    # Add histogram data
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2
    x4 = np.random.randn(200) + 4
    
    # Group data together
    hist_data = [x1, x2, x3, x4]
    
    group_labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4']
    
    # Create distplot with custom bin_size
    fig = ff.create_distplot(hist_data, group_labels, bin_size=.2)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_53456))
    get_chart_53456()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_70579():
    import plotly.figure_factory as ff
    import numpy as np
    
    # Add histogram data
    x1 = np.random.randn(200)-2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200)+2
    x4 = np.random.randn(200)+4
    
    # Group data together
    hist_data = [x1, x2, x3, x4]
    
    group_labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4']
    
    # Create distplot with custom bin_size
    fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5, 1])
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_70579))
    get_chart_70579()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_75069():
    import plotly.figure_factory as ff
    import numpy as np
    
    x1 = np.random.randn(26)
    x2 = np.random.randn(26) + .5
    
    group_labels = ['2014', '2015']
    
    rug_text_one = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
    
    rug_text_two = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj',
                    'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt',
                    'uu', 'vv', 'ww', 'xx', 'yy', 'zz']
    
    rug_text = [rug_text_one, rug_text_two] # for hover in rug plot
    colors = ['rgb(0, 0, 100)', 'rgb(0, 200, 200)']
    
    # Create distplot with custom bin_size
    fig = ff.create_distplot(
        [x1, x2], group_labels, bin_size=.2,
        rug_text=rug_text, colors=colors)
    
    fig.update_layout(title_text='Customized Distplot')
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_75069))
    get_chart_75069()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_53746():
    import plotly.figure_factory as ff
    import numpy as np
    
    x1 = np.random.randn(200)
    x2 = np.random.randn(200) + 2
    
    group_labels = ['Group 1', 'Group 2']
    
    colors = ['slategray', 'magenta']
    
    # Create distplot with curve_type set to 'normal'
    fig = ff.create_distplot([x1, x2], group_labels, bin_size=.5,
                             curve_type='normal', # override default 'kde'
                             colors=colors)
    
    # Add title
    fig.update_layout(title_text='Distplot with Normal Distribution')
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_53746))
    get_chart_53746()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_4932():
    import plotly.figure_factory as ff
    import numpy as np
    
    x1 = np.random.randn(200) - 1
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 1
    
    hist_data = [x1, x2, x3]
    
    group_labels = ['Group 1', 'Group 2', 'Group 3']
    colors = ['#333F44', '#37AA9C', '#94F3E4']
    
    # Create distplot with curve_type set to 'normal'
    fig = ff.create_distplot(hist_data, group_labels, show_hist=False, colors=colors)
    
    # Add title
    fig.update_layout(title_text='Curve and Rug Plot')
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_4932))
    get_chart_4932()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_38004():
    import plotly.figure_factory as ff
    import numpy as np
    
    x1 = np.random.randn(200) - 1
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 1
    
    hist_data = [x1, x2, x3]
    
    group_labels = ['Group 1', 'Group 2', 'Group 3']
    colors = ['#835AF1', '#7FA6EE', '#B8F7D4']
    
    # Create distplot with curve_type set to 'normal'
    fig = ff.create_distplot(hist_data, group_labels, colors=colors, bin_size=.25,
                             show_curve=False)
    
    # Add title
    fig.update_layout(title_text='Hist and Rug Plot')
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_38004))
    get_chart_38004()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_57794():
    import plotly.figure_factory as ff
    import numpy as np
    
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2
    
    hist_data = [x1, x2, x3]
    
    group_labels = ['Group 1', 'Group 2', 'Group 3']
    colors = ['#393E46', '#2BCDC1', '#F66095']
    
    fig = ff.create_distplot(hist_data, group_labels, colors=colors,
                             bin_size=[0.3, 0.2, 0.1], show_curve=False)
    
    # Add title
    fig.update(layout_title_text='Hist and Rug Plot')
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_57794))
    get_chart_57794()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_85381():
    import plotly.figure_factory as ff
    import numpy as np
    
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2
    
    hist_data = [x1, x2, x3]
    
    group_labels = ['Group 1', 'Group 2', 'Group 3']
    colors = ['#A56CC1', '#A6ACEC', '#63F5EF']
    
    # Create distplot with curve_type set to 'normal'
    fig = ff.create_distplot(hist_data, group_labels, colors=colors,
                             bin_size=.2, show_rug=False)
    
    # Add title
    fig.update_layout(title_text='Hist and Curve Plot')
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_85381))
    get_chart_85381()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_501():
    import plotly.figure_factory as ff
    import numpy as np
    import pandas as pd
    
    df = pd.DataFrame({'2012': np.random.randn(200),
                       '2013': np.random.randn(200)+1})
    fig = ff.create_distplot([df[c] for c in df.columns], df.columns, bin_size=.25)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_501))
    get_chart_501()
except Exception as e:
    st.exception(e)


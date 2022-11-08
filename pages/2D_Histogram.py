import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import inspect

@st.experimental_memo
def get_chart_38810():
    import plotly.express as px
    df = px.data.tips()
    
    fig = px.density_heatmap(df, x="total_bill", y="tip")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_38810))
    get_chart_38810()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_98560():
    import plotly.express as px
    df = px.data.tips()
    
    fig = px.density_heatmap(df, x="total_bill", y="tip", nbinsx=20, nbinsy=20, color_continuous_scale="Viridis")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_98560))
    get_chart_98560()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_40670():
    import plotly.express as px
    df = px.data.tips()
    
    fig = px.density_heatmap(df, x="total_bill", y="tip", marginal_x="histogram", marginal_y="histogram")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_40670))
    get_chart_40670()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_22070():
    import plotly.express as px
    df = px.data.tips()
    
    fig = px.density_heatmap(df, x="total_bill", y="tip", facet_row="sex", facet_col="smoker")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_22070))
    get_chart_22070()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_19213():
    import plotly.express as px
    df = px.data.tips()
    
    fig = px.density_heatmap(df, x="total_bill", y="tip", text_auto=True)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_19213))
    get_chart_19213()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_14727():
    import plotly.express as px
    df = px.data.iris()
    
    fig = px.density_heatmap(df, x="petal_length", y="petal_width", z="sepal_length", histfunc="avg")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_14727))
    get_chart_14727()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_50865():
    import plotly.graph_objects as go
    
    import numpy as np
    np.random.seed(1)
    
    x = np.random.randn(500)
    y = np.random.randn(500)+1
    
    fig = go.Figure(go.Histogram2d(
            x=x,
            y=y
        ))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_50865))
    get_chart_50865()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_68438():
    import plotly.graph_objects as go
    
    import numpy as np
    
    x = np.random.randn(500)
    y = np.random.randn(500)+1
    
    fig = go.Figure(go.Histogram2d(x=x, y=y, histnorm='probability',
            autobinx=False,
            xbins=dict(start=-3, end=3, size=0.1),
            autobiny=False,
            ybins=dict(start=-2.5, end=4, size=0.1),
            colorscale=[[0, 'rgb(12,51,131)'], [0.25, 'rgb(10,136,186)'], [0.5, 'rgb(242,211,56)'], [0.75, 'rgb(242,143,56)'], [1, 'rgb(217,30,30)']]
        ))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_68438))
    get_chart_68438()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_43120():
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    
    fig = make_subplots(2,2)
    fig.add_trace(go.Histogram2d(
        x = [ 1, 2, 2, 3, 4 ],
        y = [ 1, 2, 2, 3, 4 ],
        coloraxis = "coloraxis",
        xbins = {'start':1, 'size':1}), 1,1)
    fig.add_trace(go.Histogram2d(
        x = [ 4, 5, 5, 5, 6 ],
        y = [ 4, 5, 5, 5, 6 ],
        coloraxis = "coloraxis",
        ybins = {'start': 3, 'size': 1}),1,2)
    fig.add_trace(go.Histogram2d(
        x = [ 1, 2, 2, 3, 4 ],
        y = [ 1, 2, 2, 3, 4 ],
        bingroup = 1,
        coloraxis = "coloraxis",
        xbins = {'start':1, 'size':1}), 2,1)
    fig.add_trace(go.Histogram2d(
        x = [ 4, 5, 5, 5, 6 ],
        y = [ 4, 5, 5, 5, 6 ],
        bingroup = 1,
        coloraxis = "coloraxis",
        ybins = {'start': 3, 'size': 1}),2,2)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_43120))
    get_chart_43120()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_12214():
    import plotly.graph_objects as go
    
    import numpy as np
    
    x0 = np.random.randn(100)/5. + 0.5  # 5. enforces float division
    y0 = np.random.randn(100)/5. + 0.5
    x1 = np.random.rand(50)
    y1 = np.random.rand(50) + 1.0
    
    x = np.concatenate([x0, x1])
    y = np.concatenate([y0, y1])
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=x0,
        y=y0,
        mode='markers',
        showlegend=False,
        marker=dict(
            symbol='x',
            opacity=0.7,
            color='white',
            size=8,
            line=dict(width=1),
        )
    ))
    fig.add_trace(go.Scatter(
        x=x1,
        y=y1,
        mode='markers',
        showlegend=False,
        marker=dict(
            symbol='circle',
            opacity=0.7,
            color='white',
            size=8,
            line=dict(width=1),
        )
    ))
    fig.add_trace(go.Histogram2d(
        x=x,
        y=y,
        colorscale='YlGnBu',
        zmax=10,
        nbinsx=14,
        nbinsy=14,
        zauto=False,
    ))
    
    fig.update_layout(
        xaxis=dict( ticks='', showgrid=False, zeroline=False, nticks=20 ),
        yaxis=dict( ticks='', showgrid=False, zeroline=False, nticks=20 ),
        autosize=False,
        height=550,
        width=550,
        hovermode='closest',
    
    )
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_12214))
    get_chart_12214()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_72652():
    import plotly.graph_objects as go
    from plotly import data
    
    df = data.tips()
    
    fig = go.Figure(go.Histogram2d(
            x=df.total_bill,
            y=df.tip,
            texttemplate= "%{z}"
        ))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_72652))
    get_chart_72652()
except Exception as e:
    st.exception(e)


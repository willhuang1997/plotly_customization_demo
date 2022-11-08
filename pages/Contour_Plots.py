import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import inspect

@st.experimental_memo
def get_chart_23822():
    import plotly.graph_objects as go
    
    fig = go.Figure(data =
        go.Contour(
            z=[[10, 10.625, 12.5, 15.625, 20],
               [5.625, 6.25, 8.125, 11.25, 15.625],
               [2.5, 3.125, 5., 8.125, 12.5],
               [0.625, 1.25, 3.125, 6.25, 10.625],
               [0, 0.625, 2.5, 5.625, 10]]
        ))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_23822))
    get_chart_23822()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_58885():
    import plotly.graph_objects as go
    
    fig = go.Figure(data =
        go.Contour(
            z=[[10, 10.625, 12.5, 15.625, 20],
               [5.625, 6.25, 8.125, 11.25, 15.625],
               [2.5, 3.125, 5., 8.125, 12.5],
               [0.625, 1.25, 3.125, 6.25, 10.625],
               [0, 0.625, 2.5, 5.625, 10]],
            x=[-9, -6, -5 , -3, -1], # horizontal axis
            y=[0, 1, 4, 5, 7] # vertical axis
        ))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_58885))
    get_chart_58885()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_38125():
    import plotly.graph_objects as go
    
    fig = go.Figure(data =
         go.Contour(
            z=[[10, 10.625, 12.5, 15.625, 20],
               [5.625, 6.25, 8.125, 11.25, 15.625],
               [2.5, 3.125, 5., 8.125, 12.5],
               [0.625, 1.25, 3.125, 6.25, 10.625],
               [0, 0.625, 2.5, 5.625, 10]],
            colorscale='Electric',
        ))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_38125))
    get_chart_38125()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_3731():
    import plotly.graph_objects as go
    
    fig = go.Figure(data =
        go.Contour(
            z=[[10, 10.625, 12.5, 15.625, 20],
               [5.625, 6.25, 8.125, 11.25, 15.625],
               [2.5, 3.125, 5., 8.125, 12.5],
               [0.625, 1.25, 3.125, 6.25, 10.625],
               [0, 0.625, 2.5, 5.625, 10]],
            colorscale='Hot',
            contours=dict(
                start=0,
                end=8,
                size=2,
            ),
        ))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_3731))
    get_chart_3731()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_46393():
    import plotly.graph_objects as go
    
    fig = go.Figure(data =
        go.Contour(
            z= [[10, 10.625, 12.5, 15.625, 20],
                  [5.625, 6.25, 8.125, 11.25, 15.625],
                  [2.5, 3.125, 5., 8.125, 12.5],
                  [0.625, 1.25, 3.125, 6.25, 10.625],
                  [0, 0.625, 2.5, 5.625, 10]],
            dx=10,
            x0=5,
            dy=10,
            y0=10,
        )
    )
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_46393))
    get_chart_46393()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_42156():
    import plotly.graph_objs as go
    from plotly.subplots import make_subplots
    
    fig = make_subplots(rows=2, cols=2, subplot_titles=('connectgaps = False',
                                                            'connectgaps = True'))
    z = [[None, None, None, 12, 13, 14, 15, 16],
         [None, 1, None, 11, None, None, None, 17],
         [None, 2, 6, 7, None, None, None, 18],
         [None, 3, None, 8, None, None, None, 19],
         [5, 4, 10, 9, None, None, None, 20],
         [None, None, None, 27, None, None, None, 21],
         [None, None, None, 26, 25, 24, 23, 22]]
    
    fig.add_trace(go.Contour(z=z, showscale=False), 1, 1)
    fig.add_trace(go.Contour(z=z, showscale=False, connectgaps=True), 1, 2)
    fig.add_trace(go.Heatmap(z=z, showscale=False, zsmooth='best'), 2, 1)
    fig.add_trace(go.Heatmap(z=z, showscale=False, connectgaps=True, zsmooth='best'), 2, 2)
    
    fig['layout']['yaxis1'].update(title='Contour map')
    fig['layout']['yaxis3'].update(title='Heatmap')
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_42156))
    get_chart_42156()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_69506():
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    import numpy as np
    
    z =   [[2, 4, 7, 12, 13, 14, 15, 16],
           [3, 1, 6, 11, 12, 13, 16, 17],
           [4, 2, 7, 7, 11, 14, 17, 18],
           [5, 3, 8, 8, 13, 15, 18, 19],
           [7, 4, 10, 9, 16, 18, 20, 19],
           [9, 10, 5, 27, 23, 21, 21, 21],
           [11, 14, 17, 26, 25, 24, 23, 22]]
    
    fig = make_subplots(rows=1, cols=2,
                        subplot_titles=('Without Smoothing', 'With Smoothing'))
    
    fig.add_trace(go.Contour(z=z, line_smoothing=0), 1, 1)
    fig.add_trace(go.Contour(z=z, line_smoothing=0.85), 1, 2)
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_69506))
    get_chart_69506()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_7578():
    import plotly.graph_objects as go
    
    fig = go.Figure(data=
        go.Contour(
            z=[[10, 10.625, 12.5, 15.625, 20],
               [5.625, 6.25, 8.125, 11.25, 15.625],
               [2.5, 3.125, 5., 8.125, 12.5],
               [0.625, 1.25, 3.125, 6.25, 10.625],
               [0, 0.625, 2.5, 5.625, 10]],
            # heatmap gradient coloring is applied between each contour level
            contours_coloring='heatmap' # can also be 'lines', or 'none'
        )
    )
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_7578))
    get_chart_7578()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_99583():
    import plotly.graph_objects as go
    
    fig = go.Figure(data=
        go.Contour(
            z=[[10, 10.625, 12.5, 15.625, 20],
               [5.625, 6.25, 8.125, 11.25, 15.625],
               [2.5, 3.125, 5., 8.125, 12.5],
               [0.625, 1.25, 3.125, 6.25, 10.625],
               [0, 0.625, 2.5, 5.625, 10]],
            contours=dict(
                coloring ='heatmap',
                showlabels = True, # show labels on contours
                labelfont = dict( # label font properties
                    size = 12,
                    color = 'white',
                )
            )))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_99583))
    get_chart_99583()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_31697():
    import plotly.graph_objects as go
    
    fig = go.Figure(data=
        go.Contour(
            z=[[10, 10.625, 12.5, 15.625, 20],
               [5.625, 6.25, 8.125, 11.25, 15.625],
               [2.5, 3.125, 5., 8.125, 12.5],
               [0.625, 1.25, 3.125, 6.25, 10.625],
               [0, 0.625, 2.5, 5.625, 10]],
            contours_coloring='lines',
            line_width=2,
        )
    )
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_31697))
    get_chart_31697()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_81587():
    import plotly.graph_objects as go
    
    # Valid color strings are CSS colors, rgb or hex strings
    colorscale = [[0, 'gold'], [0.5, 'mediumturquoise'], [1, 'lightsalmon']]
    
    fig = go.Figure(data =
        go.Contour(
            z=[[10, 10.625, 12.5, 15.625, 20],
               [5.625, 6.25, 8.125, 11.25, 15.625],
               [2.5, 3.125, 5., 8.125, 12.5],
               [0.625, 1.25, 3.125, 6.25, 10.625],
               [0, 0.625, 2.5, 5.625, 10]],
            colorscale=colorscale)
    )
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_81587))
    get_chart_81587()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_84997():
    import plotly.graph_objects as go
    
    fig = go.Figure(data=
        go.Contour(
            z=[[10, 10.625, 12.5, 15.625, 20],
               [5.625, 6.25, 8.125, 11.25, 15.625],
               [2.5, 3.125, 5., 8.125, 12.5],
               [0.625, 1.25, 3.125, 6.25, 10.625],
               [0, 0.625, 2.5, 5.625, 10]],
            colorbar=dict(
                title='Color bar title', # title here
                titleside='right',
                titlefont=dict(
                    size=14,
                    family='Arial, sans-serif')
            )))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_84997))
    get_chart_84997()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_55686():
    import plotly.graph_objects as go
    
    fig = go.Figure(data=
        go.Contour(
            z=[[10, 10.625, 12.5, 15.625, 20],
               [5.625, 6.25, 8.125, 11.25, 15.625],
               [2.5, 3.125, 5., 8.125, 12.5],
               [0.625, 1.25, 3.125, 6.25, 10.625],
               [0, 0.625, 2.5, 5.625, 10]],
            colorbar=dict(
                thickness=25,
                thicknessmode='pixels',
                len=0.6,
                lenmode='fraction',
                outlinewidth=0
            )
        ))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_55686))
    get_chart_55686()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_58084():
    import plotly.graph_objects as go
    
    fig = go.Figure(data =
             go.Contour(
               z=[[10, 10.625, 12.5, 15.625, 20],
                  [5.625, 6.25, 8.125, 11.25, 15.625],
                  [2.5, 3.125, 5., 8.125, 12.5],
                  [0.625, 1.25, 3.125, 6.25, 10.625],
                  [0, 0.625, 2.5, 5.625, 10]],
               colorbar=dict(nticks=10, ticks='outside',
                             ticklen=5, tickwidth=1,
                             showticklabels=True,
                             tickangle=0, tickfont_size=12)
                ))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_58084))
    get_chart_58084()
except Exception as e:
    st.exception(e)


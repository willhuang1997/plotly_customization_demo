import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

@st.experimental_memo
def get_chart_1513():
    import plotly.express as px
    
    fig = px.imshow([[1, 20, 30],
                     [20, 1, 60],
                     [30, 60, 1]])
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    get_chart_1513()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_4493():
    import plotly.express as px
    
    df = px.data.medals_wide(indexed=True)
    fig = px.imshow(df)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    get_chart_4493()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_50142():
    import plotly.express as px
    
    z = [[.1, .3, .5, .7, .9],
         [1, .8, .6, .4, .2],
         [.2, 0, .5, .7, .9],
         [.9, .8, .4, .2, 0],
         [.3, .4, .5, .7, 1]]
    
    fig = px.imshow(z, text_auto=True)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    get_chart_50142()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_49561():
    import plotly.express as px
    
    z = [[.1, .3, .5, .7, .9],
         [1, .8, .6, .4, .2],
         [.2, 0, .5, .7, .9],
         [.9, .8, .4, .2, 0],
         [.3, .4, .5, .7, 1]]
    
    fig = px.imshow(z, text_auto=True, aspect="auto")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    get_chart_49561()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_42689():
    import plotly.express as px
    data=[[1, 25, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, 5, 20]]
    fig = px.imshow(data,
                    labels=dict(x="Day of Week", y="Time of Day", color="Productivity"),
                    x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                    y=['Morning', 'Afternoon', 'Evening']
                   )
    fig.update_xaxes(side="top")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    get_chart_42689()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_90635():
    import plotly.express as px
    import xarray as xr
    # Load xarray from dataset included in the xarray tutorial
    airtemps = xr.tutorial.open_dataset('air_temperature').air.sel(lon=250.0)
    fig = px.imshow(airtemps.T, color_continuous_scale='RdBu_r', origin='lower')
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    get_chart_90635()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_33042():
    import plotly.graph_objects as go
    
    fig = go.Figure(data=go.Heatmap(
                        z=[[1, 20, 30],
                          [20, 1, 60],
                          [30, 60, 1]]))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    get_chart_33042()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_11178():
    import plotly.graph_objects as go
    
    fig = go.Figure(data=go.Heatmap(
                       z=[[1, None, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
                       x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                       y=['Morning', 'Afternoon', 'Evening'],
                       hoverongaps = False))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    get_chart_11178()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_84540():
    import plotly.graph_objects as go
    import numpy as np
    
    # Build the rectangles as a heatmap
    # specify the edges of the heatmap squares
    phi = (1 + np.sqrt(5) )/2. # golden ratio
    xe = [0, 1, 1+(1/(phi**4)), 1+(1/(phi**3)), phi]
    ye = [0, 1/(phi**3), 1/phi**3+1/phi**4, 1/(phi**2), 1]
    
    z = [ [13,3,3,5],
          [13,2,1,5],
          [13,10,11,12],
          [13,8,8,8]
        ]
    
    fig = go.Figure(data=go.Heatmap(
              x = np.sort(xe),
              y = np.sort(ye),
              z = z,
              type = 'heatmap',
              colorscale = 'Viridis'))
    
    # Add spiral line plot
    
    def spiral(th):
        a = 1.120529
        b = 0.306349
        r = a*np.exp(-b*th)
        return (r*np.cos(th), r*np.sin(th))
    
    theta = np.linspace(-np.pi/13,4*np.pi,1000); # angle
    (x,y) = spiral(theta)
    
    fig.add_trace(go.Scatter(x= -x+x[0], y= y-y[0],
         line =dict(color='white',width=3)))
    
    axis_template = dict(range = [0,1.6], autorange = False,
                 showgrid = False, zeroline = False,
                 linecolor = 'black', showticklabels = False,
                 ticks = '' )
    
    fig.update_layout(margin = dict(t=200,r=200,b=200,l=200),
        xaxis = axis_template,
        yaxis = axis_template,
        showlegend = False,
        width = 700, height = 700,
        autosize = False )
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    get_chart_84540()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_61264():
    import plotly.graph_objects as go
    import datetime
    import numpy as np
    np.random.seed(1)
    
    programmers = ['Alex','Nicole','Sara','Etienne','Chelsea','Jody','Marianne']
    
    base = datetime.datetime.today()
    dates = base - np.arange(180) * datetime.timedelta(days=1)
    z = np.random.poisson(size=(len(programmers), len(dates)))
    
    fig = go.Figure(data=go.Heatmap(
            z=z,
            x=dates,
            y=programmers,
            colorscale='Viridis'))
    
    fig.update_layout(
        title='GitHub commits per day',
        xaxis_nticks=36)
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    get_chart_61264()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_70838():
    import plotly.graph_objects as go
    
    fig = go.Figure(data=go.Heatmap(
                        z=[[1, 20, 30],
                          [20, 1, 60],
                          [30, 60, 1]],
                        text=[['one', 'twenty', 'thirty'],
                              ['twenty', 'one', 'sixty'],
                              ['thirty', 'sixty', 'one']],
                        texttemplate="%{text}",
                        textfont={"size":20}))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    get_chart_70838()
except Exception as e:
    st.exception(e)

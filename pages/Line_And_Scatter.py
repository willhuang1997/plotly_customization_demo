import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import inspect

@st.experimental_memo
def get_chart_82943():
    # x and y given as array_like objects
    import plotly.express as px
    fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_82943))
    get_chart_82943()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_26749():
    # x and y given as DataFrame columns
    import plotly.express as px
    df = px.data.iris() # iris is a pandas DataFrame
    fig = px.scatter(df, x="sepal_width", y="sepal_length")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_26749))
    get_chart_26749()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_8909():
    import plotly.express as px
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                     size='petal_length', hover_data=['petal_width'])
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_8909))
    get_chart_8909()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_9743():
    import plotly.express as px
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color='petal_length')
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_9743))
    get_chart_9743()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_84610():
    import plotly.express as px
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", symbol="species")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_84610))
    get_chart_84610()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_50689():
    import plotly.express as px
    df = px.data.medals_long()
    
    fig = px.scatter(df, y="nation", x="count", color="medal", symbol="medal")
    fig.update_traces(marker_size=10)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_50689))
    get_chart_50689()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_67277():
    import plotly.express as px
    df = px.data.iris()
    df["e"] = df["sepal_width"]/100
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                     error_x="e", error_y="e")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_67277))
    get_chart_67277()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_92874():
    import plotly.express as px
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_length", y="sepal_width", marginal_x="histogram", marginal_y="rug")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_92874))
    get_chart_92874()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_64960():
    import plotly.express as px
    df = px.data.tips()
    fig = px.scatter(df, x="total_bill", y="tip", color="smoker", facet_col="sex", facet_row="time")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_64960))
    get_chart_64960()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_95193():
    import plotly.express as px
    
    df = px.data.tips()
    fig = px.scatter(df, x="total_bill", y="tip", trendline="ols")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_95193))
    get_chart_95193()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_34452():
    import plotly.express as px
    import numpy as np
    
    t = np.linspace(0, 2*np.pi, 100)
    
    fig = px.line(x=t, y=np.cos(t), labels={'x':'t', 'y':'cos(t)'})
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_34452))
    get_chart_34452()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_66593():
    import plotly.express as px
    df = px.data.gapminder().query("continent == 'Oceania'")
    fig = px.line(df, x='year', y='lifeExp', color='country')
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_66593))
    get_chart_66593()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_54371():
    import plotly.express as px
    df = px.data.gapminder().query("continent == 'Oceania'")
    fig = px.line(df, x='year', y='lifeExp', color='country', markers=True)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_54371))
    get_chart_54371()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_72806():
    import plotly.express as px
    df = px.data.gapminder().query("continent == 'Oceania'")
    fig = px.line(df, x='year', y='lifeExp', color='country', symbol="country")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_72806))
    get_chart_72806()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_21639():
    import plotly.express as px
    
    df = px.data.stocks()
    fig = px.line(df, x='date', y="GOOG")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_21639))
    get_chart_21639()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_52094():
    import plotly.express as px
    import pandas as pd
    
    df = pd.DataFrame(dict(
        x = [1, 3, 2, 4],
        y = [1, 2, 3, 4]
    ))
    fig = px.line(df, x="x", y="y", title="Unsorted Input") 
    
    df = df.sort_values(by="x")
    fig = px.line(df, x="x", y="y", title="Sorted Input") 
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_52094))
    get_chart_52094()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_87526():
    import plotly.express as px
    
    df = px.data.gapminder().query("country in ['Canada', 'Botswana']")
    
    fig = px.line(df, x="lifeExp", y="gdpPercap", color="country", text="year")
    fig.update_traces(textposition="bottom right")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_87526))
    get_chart_87526()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_38392():
    import plotly.graph_objects as go
    import numpy as np
    
    N = 1000
    t = np.linspace(0, 10, 100)
    y = np.sin(t)
    
    fig = go.Figure(data=go.Scatter(x=t, y=y, mode='markers'))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_38392))
    get_chart_38392()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_80962():
    import plotly.graph_objects as go
    
    # Create random data with numpy
    import numpy as np
    np.random.seed(1)
    
    N = 100
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N) + 5
    random_y1 = np.random.randn(N)
    random_y2 = np.random.randn(N) - 5
    
    fig = go.Figure()
    
    # Add traces
    fig.add_trace(go.Scatter(x=random_x, y=random_y0,
                        mode='markers',
                        name='markers'))
    fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                        mode='lines+markers',
                        name='lines+markers'))
    fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                        mode='lines',
                        name='lines'))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_80962))
    get_chart_80962()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_3655():
    import plotly.graph_objects as go
    
    fig = go.Figure(data=go.Scatter(
        x=[1, 2, 3, 4],
        y=[10, 11, 12, 13],
        mode='markers',
        marker=dict(size=[40, 60, 80, 100],
                    color=[0, 1, 2, 3])
    ))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_3655))
    get_chart_3655()
except Exception as e:
    st.exception(e)


@st.experimental_memo
def get_chart_71685():
    import plotly.graph_objects as go
    import numpy as np
    
    
    t = np.linspace(0, 10, 100)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=t, y=np.sin(t),
        name='sin',
        mode='markers',
        marker_color='rgba(152, 0, 0, .8)'
    ))
    
    fig.add_trace(go.Scatter(
        x=t, y=np.cos(t),
        name='cos',
        marker_color='rgba(255, 182, 193, .9)'
    ))
    
    # Set options common to all traces with fig.update_traces
    fig.update_traces(mode='markers', marker_line_width=2, marker_size=10)
    fig.update_layout(title='Styled Scatter',
                      yaxis_zeroline=False, xaxis_zeroline=False)
    
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_71685))
    get_chart_71685()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_39976():
    import plotly.graph_objects as go
    import pandas as pd
    
    data= pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv")
    
    fig = go.Figure(data=go.Scatter(x=data['Postal'],
                                    y=data['Population'],
                                    mode='markers',
                                    marker_color=data['Population'],
                                    text=data['State'])) # hover text goes here
    
    fig.update_layout(title='Population of USA States')
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_39976))
    get_chart_39976()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_35736():
    import plotly.graph_objects as go
    import numpy as np
    
    fig = go.Figure(data=go.Scatter(
        y = np.random.randn(500),
        mode='markers',
        marker=dict(
            size=16,
            color=np.random.randn(500), #set color equal to a variable
            colorscale='Viridis', # one of plotly colorscales
            showscale=True
        )
    ))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_35736))
    get_chart_35736()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_40719():
    import plotly.graph_objects as go
    import numpy as np
    
    N = 100000
    fig = go.Figure(data=go.Scattergl(
        x = np.random.randn(N),
        y = np.random.randn(N),
        mode='markers',
        marker=dict(
            color=np.random.randn(N),
            colorscale='Viridis',
            line_width=1
        )
    ))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_40719))
    get_chart_40719()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_82696():
    import plotly.graph_objects as go
    import numpy as np
    
    N = 100000
    r = np.random.uniform(0, 1, N)
    theta = np.random.uniform(0, 2*np.pi, N)
    
    fig = go.Figure(data=go.Scattergl(
        x = r * np.cos(theta), # non-uniform distribution
        y = r * np.sin(theta), # zoom to see more points at the center
        mode='markers',
        marker=dict(
            color=np.random.randn(N),
            colorscale='Viridis',
            line_width=1
        )
    ))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_82696))
    get_chart_82696()
except Exception as e:
    st.exception(e)


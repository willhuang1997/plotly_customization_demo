import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import inspect

@st.experimental_memo
def get_chart_88209():
    # Using plotly.express
    import plotly.express as px
    
    df = px.data.stocks()
    fig = px.line(df, x='date', y="GOOG")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_88209))
    get_chart_88209()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_70907():
    # Using graph_objects
    import plotly.graph_objects as go
    
    import pandas as pd
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    
    fig = go.Figure([go.Scatter(x=df['Date'], y=df['AAPL.High'])])
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_70907))
    get_chart_70907()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_41280():
    import plotly.express as px
    
    df = px.data.stocks(indexed=True)-1
    fig = px.bar(df, x=df.index, y="GOOG")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_41280))
    get_chart_41280()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_76361():
    import plotly.express as px
    
    df = px.data.stocks(indexed=True)-1
    fig = px.area(df, facet_col="company", facet_col_wrap=2)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_76361))
    get_chart_76361()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_23419():
    import plotly.express as px
    df = px.data.stocks()
    fig = px.line(df, x="date", y=df.columns,
                  hover_data={"date": "|%B %d, %Y"},
                  title='custom tick labels')
    fig.update_xaxes(
        dtick="M1",
        tickformat="%b\n%Y")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_23419))
    get_chart_23419()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_7290():
    import plotly.express as px
    df = px.data.stocks()
    fig = px.line(df, x="date", y=df.columns,
                  hover_data={"date": "|%B %d, %Y"},
                  title='custom tick labels with ticklabelmode="period"')
    fig.update_xaxes(
        dtick="M1",
        tickformat="%b\n%Y",
        ticklabelmode="period")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_7290))
    get_chart_7290()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_41993():
    import pandas as pd
    import plotly.express as px
    
    df = px.data.stocks()
    fig = px.line(df, x='date', y="GOOG")
    
    fig.update_xaxes(minor=dict(ticks="inside", showgrid=True))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_41993))
    get_chart_41993()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_17328():
    import plotly.express as px
    import plotly.graph_objects as go
    import pandas as pd
    
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    
    fig = px.histogram(df, x="Date", y="AAPL.Close", histfunc="avg", title="Histogram on Date Axes")
    fig.update_traces(xbins_size="M1")
    fig.update_xaxes(showgrid=True, ticklabelmode="period", dtick="M1", tickformat="%b\n%Y")
    fig.update_layout(bargap=0.1)
    fig.add_trace(go.Scatter(mode="markers", x=df["Date"], y=df["AAPL.Close"], name="daily"))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_17328))
    get_chart_17328()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_77508():
    import plotly.graph_objects as go
    import pandas as pd
    
    df = pd.DataFrame(dict(
        date=["2020-01-10", "2020-02-10", "2020-03-10", "2020-04-10", "2020-05-10", "2020-06-10"],
        value=[1,2,3,1,2,3]
    ))
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        name="Raw Data",
        mode="markers+lines", x=df["date"], y=df["value"],
        marker_symbol="star"
    ))
    fig.add_trace(go.Scatter(
        name="Start-aligned",
        mode="markers+lines", x=df["date"], y=df["value"],
        xperiod="M1",
        xperiodalignment="start"
    ))
    fig.add_trace(go.Scatter(
        name="Middle-aligned",
        mode="markers+lines", x=df["date"], y=df["value"],
        xperiod="M1",
        xperiodalignment="middle"
    ))
    fig.add_trace(go.Scatter(
        name="End-aligned",
        mode="markers+lines", x=df["date"], y=df["value"],
        xperiod="M1",
        xperiodalignment="end"
    ))
    fig.add_trace(go.Bar(
        name="Middle-aligned",
        x=df["date"], y=df["value"],
        xperiod="M1",
        xperiodalignment="middle"
    ))
    fig.update_xaxes(showgrid=True, ticklabelmode="period")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_77508))
    get_chart_77508()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_26177():
    import plotly.graph_objects as go
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=["2020-01-01", "2020-04-01", "2020-07-01"],
        y=[1000, 1500, 1700],
        xperiod="M3",
        xperiodalignment="middle",
        xhoverformat="Q%q",
        hovertemplate="%{y}%{_xother}"
    ))
    
    fig.add_trace(go.Scatter(
        x=["2020-01-01", "2020-02-01", "2020-03-01",
          "2020-04-01", "2020-05-01", "2020-06-01",
          "2020-07-01", "2020-08-01", "2020-09-01"],
        y=[1100,1050,1200,1300,1400,1700,1500,1400,1600],
        xperiod="M1",
        xperiodalignment="middle",
        hovertemplate="%{y}%{_xother}"
    ))
    
    fig.update_layout(hovermode="x unified")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_26177))
    get_chart_26177()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_96859():
    # Using plotly.express
    import plotly.express as px
    
    import pandas as pd
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    
    fig = px.line(df, x='Date', y='AAPL.High', range_x=['2016-07-01','2016-12-31'])
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_96859))
    get_chart_96859()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_51286():
    # Using graph_objects
    
    import plotly.graph_objects as go
    import datetime
    
    x = [datetime.datetime(year=2013, month=10, day=4),
         datetime.datetime(year=2013, month=11, day=5),
         datetime.datetime(year=2013, month=12, day=6)]
    
    fig = go.Figure(data=[go.Scatter(x=x, y=[1, 3, 6])])
    # Use datetime objects to set xaxis range
    fig.update_layout(xaxis_range=[datetime.datetime(2013, 10, 17),
                                   datetime.datetime(2013, 11, 20)])
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_51286))
    get_chart_51286()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_70944():
    import plotly.graph_objects as go
    import pandas as pd
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    
    fig = px.line(df, x='Date', y='AAPL.High')
    
    # Use date string to set xaxis range
    fig.update_layout(xaxis_range=['2016-07-01','2016-12-31'],
                      title_text="Manually Set Date Range")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_70944))
    get_chart_70944()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_72072():
    import plotly.express as px
    import pandas as pd
    
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    
    fig = px.line(df, x='Date', y='AAPL.High', title='Time Series with Rangeslider')
    
    fig.update_xaxes(rangeslider_visible=True)
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_72072))
    get_chart_72072()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_52596():
    import plotly.express as px
    import pandas as pd
    
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    
    fig = px.line(df, x='Date', y='AAPL.High', title='Time Series with Range Slider and Selectors')
    
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_52596))
    get_chart_52596()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_36143():
    import plotly.graph_objects as go
    import pandas as pd
    
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    
    fig = go.Figure(go.Scatter(
        x = df['Date'],
        y = df['mavg']
    ))
    
    fig.update_xaxes(
        rangeslider_visible=True,
        tickformatstops = [
            dict(dtickrange=[None, 1000], value="%H:%M:%S.%L ms"),
            dict(dtickrange=[1000, 60000], value="%H:%M:%S s"),
            dict(dtickrange=[60000, 3600000], value="%H:%M m"),
            dict(dtickrange=[3600000, 86400000], value="%H:%M h"),
            dict(dtickrange=[86400000, 604800000], value="%e. %b d"),
            dict(dtickrange=[604800000, "M1"], value="%e. %b w"),
            dict(dtickrange=["M1", "M12"], value="%b '%y M"),
            dict(dtickrange=["M12", None], value="%Y Y")
        ]
    )
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_36143))
    get_chart_36143()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_48658():
    import plotly.express as px
    import pandas as pd
    
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    
    fig = px.scatter(df, x='Date', y='AAPL.High', range_x=['2015-12-01', '2016-01-15'],
                     title="Default Display with Gaps")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_48658))
    get_chart_48658()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_46766():
    import plotly.express as px
    import pandas as pd
    
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    
    fig = px.scatter(df, x='Date', y='AAPL.High', range_x=['2015-12-01', '2016-01-15'],
                     title="Hide Weekend and Holiday Gaps with rangebreaks")
    fig.update_xaxes(
        rangebreaks=[
            dict(bounds=["sat", "mon"]), #hide weekends
            dict(values=["2015-12-25", "2016-01-01"])  # hide Christmas and New Year's
        ]
    )
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_46766))
    get_chart_46766()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_72475():
    import plotly.express as px
    import pandas as pd
    import numpy as np
    np.random.seed(1)
    
    work_week_40h = pd.date_range(start='2020-03-01', end='2020-03-07', freq="BH")
    
    df = pd.DataFrame(dict(
        date = work_week_40h,
        value = np.cumsum(np.random.rand(40)-0.5)
    ))
    
    fig = px.scatter(df, x="date", y="value",
                     title="Default Display with Gaps")
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_72475))
    get_chart_72475()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_67643():
    import plotly.express as px
    import pandas as pd
    import numpy as np
    np.random.seed(1)
    
    work_week_40h = pd.date_range(start='2020-03-01', end='2020-03-07', freq="BH")
    
    df = pd.DataFrame(dict(
        date = work_week_40h,
        value = np.cumsum(np.random.rand(40)-0.5)
    ))
    
    fig = px.scatter(df, x="date", y="value",
                     title="Hide Non-Business Hour Gaps with rangebreaks")
    fig.update_xaxes(
        rangebreaks=[
            dict(bounds=[17, 9], pattern="hour"), #hide hours outside of 9am-5pm
        ]
    )
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_67643))
    get_chart_67643()
except Exception as e:
    st.exception(e)


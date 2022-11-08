import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import inspect

@st.experimental_memo
def get_chart_99359():
    import plotly.express as px
    data = dict(
        character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
        parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
        value=[10, 14, 12, 10, 2, 6, 6, 4, 4])
    
    fig = px.sunburst(
        data,
        names='character',
        parents='parent',
        values='value',
    )
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_99359))
    get_chart_99359()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_8156():
    import plotly.express as px
    df = px.data.tips()
    fig = px.sunburst(df, path=['day', 'time', 'sex'], values='total_bill')
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_8156))
    get_chart_8156()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_24007():
    import plotly.express as px
    import numpy as np
    df = px.data.gapminder().query("year == 2007")
    fig = px.sunburst(df, path=['continent', 'country'], values='pop',
                      color='lifeExp', hover_data=['iso_alpha'],
                      color_continuous_scale='RdBu',
                      color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_24007))
    get_chart_24007()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_54664():
    import plotly.express as px
    df = px.data.tips()
    fig = px.sunburst(df, path=['sex', 'day', 'time'], values='total_bill', color='day')
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_54664))
    get_chart_54664()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_50730():
    import plotly.express as px
    df = px.data.tips()
    fig = px.sunburst(df, path=['sex', 'day', 'time'], values='total_bill', color='time')
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_50730))
    get_chart_50730()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_76456():
    import plotly.express as px
    df = px.data.tips()
    fig = px.sunburst(df, path=['sex', 'day', 'time'], values='total_bill', color='time',
                      color_discrete_map={'(?)':'black', 'Lunch':'gold', 'Dinner':'darkblue'})
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_76456))
    get_chart_76456()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_19363():
    import plotly.express as px
    import pandas as pd
    vendors = ["A", "B", "C", "D", None, "E", "F", "G", "H", None]
    sectors = ["Tech", "Tech", "Finance", "Finance", "Other",
               "Tech", "Tech", "Finance", "Finance", "Other"]
    regions = ["North", "North", "North", "North", "North",
               "South", "South", "South", "South", "South"]
    sales = [1, 3, 2, 4, 1, 2, 2, 1, 4, 1]
    df = pd.DataFrame(
        dict(vendors=vendors, sectors=sectors, regions=regions, sales=sales)
    )
    print(df)
    fig = px.sunburst(df, path=['regions', 'sectors', 'vendors'], values='sales')
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_19363))
    get_chart_19363()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_41():
    import plotly.graph_objects as go
    
    fig =go.Figure(go.Sunburst(
        labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
        parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
        values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
    ))
    # Update layout for tight margin
    # See https://plotly.com/python/creating-and-updating-figures/
    fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_41))
    get_chart_41()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_70667():
    import plotly.graph_objects as go
    
    fig =go.Figure(go.Sunburst(
     ids=[
        "North America", "Europe", "Australia", "North America - Football", "Soccer",
        "North America - Rugby", "Europe - Football", "Rugby",
        "Europe - American Football","Australia - Football", "Association",
        "Australian Rules", "Autstralia - American Football", "Australia - Rugby",
        "Rugby League", "Rugby Union"
      ],
      labels= [
        "North<br>America", "Europe", "Australia", "Football", "Soccer", "Rugby",
        "Football", "Rugby", "American<br>Football", "Football", "Association",
        "Australian<br>Rules", "American<br>Football", "Rugby", "Rugby<br>League",
        "Rugby<br>Union"
      ],
      parents=[
        "", "", "", "North America", "North America", "North America", "Europe",
        "Europe", "Europe","Australia", "Australia - Football", "Australia - Football",
        "Australia - Football", "Australia - Football", "Australia - Rugby",
        "Australia - Rugby"
      ],
    ))
    fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_70667))
    get_chart_70667()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_8006():
    import plotly.graph_objects as go
    
    fig =go.Figure(go.Sunburst(
        labels=[ "Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
        parents=["",    "Eve",  "Eve",  "Seth", "Seth", "Eve",  "Eve",  "Awan",  "Eve" ],
        values=[  65,    14,     12,     10,     2,      6,      6,      4,       4],
        branchvalues="total",
    ))
    fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_8006))
    get_chart_8006()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_38085():
    import plotly.graph_objects as go
    
    import pandas as pd
    
    df1 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/sunburst-coffee-flavors-complete.csv')
    df2 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/coffee-flavors.csv')
    
    fig = go.Figure()
    
    fig.add_trace(go.Sunburst(
        ids=df1.ids,
        labels=df1.labels,
        parents=df1.parents,
        domain=dict(column=0)
    ))
    
    fig.add_trace(go.Sunburst(
        ids=df2.ids,
        labels=df2.labels,
        parents=df2.parents,
        domain=dict(column=1),
        maxdepth=2
    ))
    
    fig.update_layout(
        grid= dict(columns=2, rows=1),
        margin = dict(t=0, l=0, r=0, b=0)
    )
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_38085))
    get_chart_38085()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_53681():
    import plotly.graph_objects as go
    import pandas as pd
    
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/coffee-flavors.csv')
    
    fig = go.Figure()
    
    fig.add_trace(go.Sunburst(
        ids=df.ids,
        labels=df.labels,
        parents=df.parents,
        domain=dict(column=1),
        maxdepth=2,
        insidetextorientation='radial'
    ))
    
    fig.update_layout(
        margin = dict(t=10, l=10, r=10, b=10)
    )
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_53681))
    get_chart_53681()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_82833():
    import plotly.graph_objects as go
    import pandas as pd
    
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/sunburst-coffee-flavors-complete.csv')
    
    fig = go.Figure(go.Sunburst(
            ids = df.ids,
            labels = df.labels,
            parents = df.parents))
    fig.update_layout(uniformtext=dict(minsize=10, mode='hide'))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_82833))
    get_chart_82833()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_18609():
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    import pandas as pd
    
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/sales_success.csv')
    print(df.head())
    
    levels = ['salesperson', 'county', 'region'] # levels used for the hierarchical chart
    color_columns = ['sales', 'calls']
    value_column = 'calls'
    
    def build_hierarchical_dataframe(df, levels, value_column, color_columns=None):
        """
        Build a hierarchy of levels for Sunburst or Treemap charts.
    
        Levels are given starting from the bottom to the top of the hierarchy,
        ie the last level corresponds to the root.
        """
        df_all_trees = pd.DataFrame(columns=['id', 'parent', 'value', 'color'])
        for i, level in enumerate(levels):
            df_tree = pd.DataFrame(columns=['id', 'parent', 'value', 'color'])
            dfg = df.groupby(levels[i:]).sum()
            dfg = dfg.reset_index()
            df_tree['id'] = dfg[level].copy()
            if i < len(levels) - 1:
                df_tree['parent'] = dfg[levels[i+1]].copy()
            else:
                df_tree['parent'] = 'total'
            df_tree['value'] = dfg[value_column]
            df_tree['color'] = dfg[color_columns[0]] / dfg[color_columns[1]]
            df_all_trees = df_all_trees.append(df_tree, ignore_index=True)
        total = pd.Series(dict(id='total', parent='',
                                  value=df[value_column].sum(),
                                  color=df[color_columns[0]].sum() / df[color_columns[1]].sum()))
        df_all_trees = df_all_trees.append(total, ignore_index=True)
        return df_all_trees
    
    
    df_all_trees = build_hierarchical_dataframe(df, levels, value_column, color_columns)
    average_score = df['sales'].sum() / df['calls'].sum()
    
    fig = make_subplots(1, 2, specs=[[{"type": "domain"}, {"type": "domain"}]],)
    
    fig.add_trace(go.Sunburst(
        labels=df_all_trees['id'],
        parents=df_all_trees['parent'],
        values=df_all_trees['value'],
        branchvalues='total',
        marker=dict(
            colors=df_all_trees['color'],
            colorscale='RdBu',
            cmid=average_score),
        hovertemplate='<b>%{label} </b> <br> Sales: %{value}<br> Success rate: %{color:.2f}',
        name=''
        ), 1, 1)
    
    fig.add_trace(go.Sunburst(
        labels=df_all_trees['id'],
        parents=df_all_trees['parent'],
        values=df_all_trees['value'],
        branchvalues='total',
        marker=dict(
            colors=df_all_trees['color'],
            colorscale='RdBu',
            cmid=average_score),
        hovertemplate='<b>%{label} </b> <br> Sales: %{value}<br> Success rate: %{color:.2f}',
        maxdepth=2
        ), 1, 2)
    
    fig.update_layout(margin=dict(t=10, b=10, r=10, l=10))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_18609))
    get_chart_18609()
except Exception as e:
    st.exception(e)


import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import inspect

@st.experimental_memo
def get_chart_97263():
    import plotly.express as px
    data = dict(
        character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
        parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
        value=[10, 14, 12, 10, 2, 6, 6, 4, 4])
    
    fig =px.icicle(
        data,
        names='character',
        parents='parent',
        values='value',
    )
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_97263))
    get_chart_97263()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_40055():
    import plotly.express as px
    df = px.data.tips()
    fig = px.icicle(df, path=[px.Constant("all"), 'day', 'time', 'sex'], values='total_bill')
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_40055))
    get_chart_40055()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_1235():
    import plotly.express as px
    import numpy as np
    df = px.data.gapminder().query("year == 2007")
    fig = px.icicle(df, path=[px.Constant("world"), 'continent', 'country'], values='pop',
                      color='lifeExp', hover_data=['iso_alpha'],
                      color_continuous_scale='RdBu',
                      color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_1235))
    get_chart_1235()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_32745():
    import plotly.express as px
    df = px.data.tips()
    fig = px.icicle(df, path=[px.Constant("all"), 'sex', 'day', 'time'],
                    values='total_bill', color='day')
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_32745))
    get_chart_32745()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_89315():
    import plotly.express as px
    df = px.data.tips()
    fig = px.icicle(df, path=[px.Constant("all"), 'sex', 'day', 'time'],
                    values='total_bill', color='time')
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_89315))
    get_chart_89315()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_59352():
    import plotly.express as px
    df = px.data.tips()
    fig = px.icicle(df, path=[px.Constant("all"), 'sex', 'day', 'time'],
                    values='total_bill', color='time',
                    color_discrete_map={'(?)':'lightgrey', 'Lunch':'gold', 'Dinner':'darkblue'})
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_59352))
    get_chart_59352()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_55415():
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
    df["all"] = "all" # in order to have a single root node
    print(df)
    fig = px.icicle(df, path=['all', 'regions', 'sectors', 'vendors'], values='sales')
    fig.update_traces(root_color='lightgrey')
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_55415))
    get_chart_55415()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_74134():
    import plotly.graph_objects as go
    
    fig =go.Figure(go.Icicle(
        labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
        parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
        values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
        root_color="lightgrey"
    ))
    
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_74134))
    get_chart_74134()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_60038():
    import plotly.graph_objects as go
    
    fig =go.Figure(go.Icicle(
     ids=["Sports",
        "North America", "Europe", "Australia", "North America - Football", "Soccer",
        "North America - Rugby", "Europe - Football", "Rugby",
        "Europe - American Football","Australia - Football", "Association",
        "Australian Rules", "Autstralia - American Football", "Australia - Rugby",
        "Rugby League", "Rugby Union"
      ],
      labels= ["Sports",
        "North<br>America", "Europe", "Australia", "Football", "Soccer", "Rugby",
        "Football", "Rugby", "American<br>Football", "Football", "Association",
        "Australian<br>Rules", "American<br>Football", "Rugby", "Rugby<br>League",
        "Rugby<br>Union"
      ],
      parents=["",
        "Sports", "Sports", "Sports", "North America", "North America", "North America", "Europe",
        "Europe", "Europe","Australia", "Australia - Football", "Australia - Football",
        "Australia - Football", "Australia - Football", "Australia - Rugby",
        "Australia - Rugby"
      ],
        root_color="lightgrey"
    ))
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_60038))
    get_chart_60038()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_74532():
    import plotly.graph_objects as go
    
    fig =go.Figure(go.Icicle(
        labels=[ "Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
        parents=["",    "Eve",  "Eve",  "Seth", "Seth", "Eve",  "Eve",  "Awan",  "Eve" ],
        values=[  65,    14,     12,     10,     2,      6,      6,      4,       4],
        branchvalues="total",
        root_color="lightgrey"
    ))
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_74532))
    get_chart_74532()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_73165():
    import plotly.graph_objects as go
    
    import pandas as pd
    
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/96c0bd/sunburst-coffee-flavors-complete.csv')
    
    fig = go.Figure()
    
    fig.add_trace(go.Icicle(
        ids=df.ids,
        labels=df.labels,
        parents=df.parents,
        root_color="lightgrey"
    ))
    
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_73165))
    get_chart_73165()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_17366():
    import plotly.graph_objects as go
    import pandas as pd
    
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/96c0bd/sunburst-coffee-flavors-complete.csv')
    
    fig = go.Figure(go.Icicle(
        ids = df.ids,
        labels = df.labels,
        parents = df.parents,
        root_color="lightgrey"
    ))
    fig.update_layout(
        uniformtext=dict(minsize=10, mode='hide'),
        margin = dict(t=50, l=25, r=25, b=25)
    )
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_17366))
    get_chart_17366()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_47666():
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
        Build a hierarchy of levels for Icicle charts.
    
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
    
    fig.add_trace(go.Icicle(
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
    
    fig.add_trace(go.Icicle(
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
    
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_47666))
    get_chart_47666()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_78609():
    import plotly.graph_objects as go
    
    labels = ["container", "A1", "A2", "A3", "A4", "A5", "B1", "B2"]
    parents = ["", "container", "A1", "A2", "A3", "A4", "container", "B1"]
    
    fig = go.Figure(go.Icicle(
        labels = labels,
        parents = parents,
        marker_colors = ["pink", "royalblue", "lightgray", "purple",
                         "cyan", "lightgray", "lightblue", "lightgreen"]))
    
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_78609))
    get_chart_78609()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_77252():
    import plotly.graph_objects as go
    
    values = [0, 11, 12, 13, 14, 15, 20, 30]
    labels = ["container", "A1", "A2", "A3", "A4", "A5", "B1", "B2"]
    parents = ["", "container", "A1", "A2", "A3", "A4", "container", "B1"]
    
    fig = go.Figure(go.Icicle(
        labels = labels,
        parents = parents,
        values=values,
        root_color="lightblue"
    ))
    
    fig.update_layout(
        iciclecolorway = ["pink", "lightgray"],
        margin = dict(t=50, l=25, r=25, b=25)
    )
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_77252))
    get_chart_77252()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_62148():
    import plotly.graph_objects as go
    
    values = [0, 11, 12, 13, 14, 15, 20, 30]
    labels = ["container", "A1", "A2", "A3", "A4", "A5", "B1", "B2"]
    parents = ["", "container", "A1", "A2", "A3", "A4", "container", "B1"]
    
    fig = go.Figure(go.Icicle(
        labels = labels,
        values = values,
        parents = parents,
        marker_colorscale = 'Blues'))
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_62148))
    get_chart_62148()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_98947():
    import plotly.graph_objects as go
    import pandas as pd
    
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/96c0bd/sunburst-coffee-flavors-complete.csv')
    
    fig = go.Figure(
        go.Icicle(
            ids = df.ids,
            labels = df.labels,
            parents = df.parents,
            root_color="lightgrey",
            tiling = dict(
                orientation='v',
                flip='y'
            )
        )
    )
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_98947))
    get_chart_98947()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_85982():
    import plotly.graph_objects as go
    import pandas as pd
    
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/96c0bd/sunburst-coffee-flavors-complete.csv')
    
    fig = go.Figure(
        go.Icicle(
            ids = df.ids,
            labels = df.labels,
            parents = df.parents,
            root_color="lightgrey",
            tiling = dict(
                orientation='v'
            )
        )
    )
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_85982))
    get_chart_85982()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_86778():
    import plotly.graph_objects as go
    import pandas as pd
    
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/96c0bd/sunburst-coffee-flavors-complete.csv')
    
    fig = go.Figure(
        go.Icicle(
            ids = df.ids,
            labels = df.labels,
            parents = df.parents,
            root_color="lightgrey",
            tiling = dict(
                orientation='h'
            )
        )
    )
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_86778))
    get_chart_86778()
except Exception as e:
    st.exception(e)



@st.experimental_memo
def get_chart_55963():
    import plotly.graph_objects as go
    import pandas as pd
    
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/96c0bd/sunburst-coffee-flavors-complete.csv')
    
    fig = go.Figure(
        go.Icicle(
            ids = df.ids,
            labels = df.labels,
            parents = df.parents,
            root_color="lightgrey",
            tiling = dict(
                orientation='h',
                flip='x'
            )
        )
    )
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    tab1, tab2 = st.tabs(["Streamlit theme", "Default theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

try:
    st.expander("See code").code(inspect.getsource(get_chart_55963))
    get_chart_55963()
except Exception as e:
    st.exception(e)


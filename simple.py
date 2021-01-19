import streamlit as st
import numpy as np
import pandas as pd

st.title('My first app')

st.write('Here\'s our first attempt at using data to create a table:')
st.write(pd.DataFrame({
'first column':[1,2,3,4],
'second column':[10,20,30,40]
}))

"""
## Second title
This is a second title with different method
"""

df = pd.DataFrame({
'first column':[1,2,3,4],
'second column':[10,20,30,40]
})
df

"""
## Lets add some more features

### Draw a line chart
"""
chart_data = pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.line_chart(chart_data)
"""
### Plot a map
"""
map_data = pd.DataFrame(np.random.randn(1000,2) / [50,50] + [37.76,-122.4], columns=['lat','lon'])
st.map(map_data)


"""
## Add interativity
> https://docs.streamlit.io/en/stable/api.html
"""

"""
### Use checkboxes to show/hide data
"""
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
    st.line_chart(chart_data)

"""
### Use a selectbox for options
"""
option = st.selectbox('Which number do you like best?',df['first column'])
'You selected: ', option

"""
### Lay out your app
For a cleaner look, you can move your widgets into a sidebar.
Most of the elements you can put into your app can also be put into a sidebar using this syntax: `st.sidebar.[element_name]()`
"""
option2 = st.sidebar.selectbox('Which number you like More?',df['first column'])
'You selected: ', option2


"""
### More widgets
Buttons & actions, collapsibles, multiple column rows
"""

left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")


expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")


"""
## Show progress
When adding long running computations to an app, you can use st.progress() to display status in real time.
"""
import time
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

































#

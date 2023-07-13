import pandas

data = pandas.read_csv("list_of_states_in_india-28j.csv")
states = data.State

states_data = pandas.DataFrame(states)
states_data.to_csv("all_states_in_India")
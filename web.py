import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["entered_todo"].title()+'\n'
    print(new_todo)
    todos.append(new_todo)
    functions.write_todos(todos)
    st.session_state["entered_todo"] = ""

st.title("My Todo App")
st.subheader("This is obviously a TO DO app")
st.write("This app is to improve my productivity")

for index, todo in enumerate(todos):
    display_list = f'{index+1} -  {todo}'
    checkbox = st.checkbox(display_list,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.experimental_rerun()

st.text_input(value="",label="Enter a todo", placeholder="Enter a todo: ",
              on_change=add_todo, key="entered_todo",label_visibility="hidden")

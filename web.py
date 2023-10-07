import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("ToDos")
st.subheader("Increase your productivity")


for index, todo in enumerate(todos):
    cb = st.checkbox(todo, key=todo)
    if cb:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(
    label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo"
)

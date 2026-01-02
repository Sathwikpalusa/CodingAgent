from langgraph.graph import StateGraph
import streamlit as st
from agents.code import coding_agent
from agents.planning import plan
from agents.review import review
from agents.test import test
from state import Coding

graph=StateGraph(Coding)
graph.add_node("planning_agent",plan)
graph.add_node("coding_agent",coding_agent)
graph.add_node("testing_agent",test)
graph.add_node("review_agent",review)
graph.set_entry_point("planning_agent")



graph.add_edge("planning_agent","coding_agent")
graph.add_edge("coding_agent","testing_agent")
graph.add_edge("testing_agent","review_agent")
graph.set_finish_point("review_agent")

app=graph.compile()

st.title("🧠 Multi-Agent AI Code Generator")
task = st.text_area("Describe your coding task")
if st.button("Generate Code"):
    result = app.invoke({
        "task": task,
        "plan": "",
        "code": "",
        "test_report": "",
        "final_code": ""
    })

    st.subheader("✅ Final Code")
    st.code(result["final_code"], language="python")


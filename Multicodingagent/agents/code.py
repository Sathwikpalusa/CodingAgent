from llm1 import getllm

def coding_agent(state):
    llm=getllm()
    prompt=f"""
    you are a pro python developer,
    plan={state['plan']}
    write a clean and production ready python code for the given plan
    """
    response=llm.invoke(prompt)
    state["code"]=response.content
    return state

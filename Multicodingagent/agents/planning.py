from llm1 import getllm


def plan(state):
    llm=getllm()
    prompt=f""""
    
    you have a excellent knowledge in coding
    create a step by step process to solve the given task.
    task={state['task']}

    """
    response=llm.invoke(prompt)
    state["plan"]=response.content
    return state
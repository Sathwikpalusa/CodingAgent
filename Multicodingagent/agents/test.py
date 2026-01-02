from llm1 import getllm

def test(state):
    llm=getllm()
    prompt=f"""
    you are a highend pro testing engineer,
    test the given code and give the errors bugs and all that need to be fixed.
    code={state['code']}
    """
    response=llm.invoke(prompt)
    state["test_report"]=response.content
    return state
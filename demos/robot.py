from langchain_openai import ChatOpenAI
import os

# 演示的是会话，记录会话信息，具备多伦对话的功能

model = ChatOpenAI(model="gpt-3.5-turbo")


os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = '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'



from langchain_core.messages import HumanMessage

print(model.invoke([HumanMessage(content="Hi! I'm Bob")]))

print(model.invoke([HumanMessage(content="What's my name???")]))



# 传入对话上下文
from langchain_core.messages import AIMessage

result2 = model.invoke(
    [
        HumanMessage(content="Hi! I'm Bob"),
        AIMessage(content="Hello Bob! How can I assist you today?"),
        HumanMessage(content="What's my name?"),
    ]
)

print(result2)


from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


with_message_history = RunnableWithMessageHistory(model, get_session_history)


config = {"configurable": {"session_id": "abc2"}}


response = with_message_history.invoke(
    [HumanMessage(content="Hi! I'm Bob")],
    config=config,
)

print(response.content)


response = with_message_history.invoke(
    [HumanMessage(content="What's my name?")],
    config=config,
)

print(response.content)


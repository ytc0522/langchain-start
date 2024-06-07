from langchain_openai import ChatOpenAI
import os


model = ChatOpenAI(model="gpt-3.5-turbo")


os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = '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'


from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
from langchain_core.messages import HumanMessage


chain = prompt | model

response = chain.invoke({"messages": [HumanMessage(content="hi! I'm bob")]})

print(response.content)

with_message_history = RunnableWithMessageHistory(chain, get_session_history)



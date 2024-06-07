import getpass
import os

# os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-3.5-turbo")


from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="Translate the following from English into Chinese"),
    HumanMessage(content="hi! Where are you from ?"),
]

result = model.invoke(messages)
print(result)


from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

print(parser.invoke(result))



# 可以使用运算符轻松创建链|。|运算符在 LangChain 中用于将两个元素组合在一起。

chain = model | parser

print(chain.invoke(messages))



from langchain_core.prompts import ChatPromptTemplate

system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)


result = prompt_template.invoke({"language": "Chinese", "text": "Go Go Go "})
print(result)



chain = prompt_template | model | parser

result2 = chain.invoke({"language": "italian", "text": "hi"})
print(result2)




from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationTokenBufferMemory

def build_chat_chain(openai_api_key, max_token_limit, temperature):
    # LLM 
    llm = ChatOpenAI(openai_api_key=openai_api_key, model_name = "gpt-3.5-turbo", temperature=temperature)

    # system message prompt
    system_message_prompt = SystemMessagePromptTemplate(
        prompt=PromptTemplate(
            input_variables=[],
            template="你是一個貼心的助手，用中文回答問題時，會用繁體中文回答。不知道答案時，會如實回答不知道答案。",
        )
    )

    # human message prompt
    human_message_prompt = HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            input_variables=["message"],
            template="{message}",
        )
    )
    # memory prompt
    memory_prompt = MessagesPlaceholder(variable_name="chat_history")

    # chat prompt
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, memory_prompt, human_message_prompt])

    # conversation chain
    chain = LLMChain(
        llm=llm,
        prompt=chat_prompt,
        memory=ConversationTokenBufferMemory(llm=llm, memory_key="chat_history", max_token_limit=max_token_limit, return_messages=True),
        verbose=False,
    )
    return chain
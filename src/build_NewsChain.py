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

def build_news_chain(openai_api_key, max_token_limit, temperature):
    # LLM 
    llm = ChatOpenAI(openai_api_key=openai_api_key, model_name = "gpt-3.5-turbo", temperature=temperature)

    # system message prompt
    system_message_prompt = SystemMessagePromptTemplate(
        prompt=PromptTemplate(
            input_variables=[],
            template="你是身經百戰的新聞評論員，擅長解密媒體訊息，深諳批判思考，邏輯縝密。心胸開闊，言之有物，從不拘泥於官方辭令。喜歡以輕鬆幽默的語句，呈現你的睿智。",
        )
    )

    # human message prompt
    human_message_prompt = HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            input_variables=["message"],
            template="***\n{message}\n***\n請問你認為這篇報導是否公正客觀？請就其中的標題、觀點和呈現方式提供你的看法。論述至少要有三段。",
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
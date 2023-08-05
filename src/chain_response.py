from langchain.memory import MongoDBChatMessageHistory
from src.history.feed_history import feed_history
from src.history.write_history import write_history

# generate response from Chain
def chain_response(chain, mongodb_message_history, msg):

    # feed user's message history to chain memory
    chain = feed_history(mongodb_message_history, chain)    

    # generate response Chain with memory
    response = chain.run({"message": msg})

    # write user's message history to MongoDB
    write_history(chain, mongodb_message_history)

    return response
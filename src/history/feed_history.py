# feed user's message history to chain memory
def feed_history(mongodb_message_history, chain):

    # clear human/AI conversation (since it can be other user's)
    chain.memory.chat_memory.clear()

    # if message history is not empty, feed history
    if mongodb_message_history.messages:
        # feed conversation memory
        for memory in (mongodb_message_history.messages):
            chain.memory.chat_memory.add_message(memory)

    return chain
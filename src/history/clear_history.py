# clear user's message history on MongoDB
def clear_history(mongodb_message_history):
    mongodb_message_history.clear()
    # print("History cleared")
    return
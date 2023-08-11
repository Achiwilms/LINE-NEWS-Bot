# write user's message history to MongoDB
def write_history(chain, mongodb_message_history):
    
    # don't write history when chain memory is empty
    if not chain.memory.chat_memory.messages:
        return
       
    # Mongo memory is not empty and chain memory is flushed 
    if (mongodb_message_history.messages and 
        (mongodb_message_history.messages[0] != chain.memory.chat_memory.messages[0])):
        # clear stale memory in MongoDB
        mongodb_message_history.clear()
        # write all chain memory to MongoDB
        for memory in chain.memory.chat_memory.messages:
            mongodb_message_history.add_message(memory)
        # print("Clear Mongo and Write all")
    # Mongo memory is empty or chain memory is not flushed 
    else:
        # write last two chain memory to MongoDB
        for memory in chain.memory.chat_memory.messages[-2:]:
            mongodb_message_history.add_message(memory)
        # print("Write last two msg to Mongo")
        
    return

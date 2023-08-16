# LINE-NEWS-Bot_en

An AI-driven LINE chatbot providing different news perspectives: AI, what's your take?

## Introduction

Have you ever read a news article and felt that something about the report was a bit off, but couldn't quite put your finger on it?

If you're interested in hearing alternative viewpoints, this LINE chatbot is more than happy to offer its insights 🎙️. 

Simply share a news link with it, and it will provide comments based on the article's headline, perspectives, and presentation, offering them as a reference for you.

Of course, it's important not to fully accept its opinions, as AI can easily make mistakes, and its comments might not always be impartial 😅. This isn't professional news critique; the AI's viewpoints are merely for consideration, so please don't take them too seriously⚠️.

Additionally, because the bot is powered by the same GPT-3.5 as ChatGPT 🧠, feel free to have casual conversations with it or ask questions beyond news!

<p align="center">
    <img src="https://github.com/Achiwilms/LINE-NEWS-Bot/blob/main/icon/demo.gif?raw=true" alt="GUI" width="200">
</p>

Click to add as a friend👉👉 [AI, what's your take?](https://liff.line.me/1645278921-kWRPP32q/?accountId=606bncqu)

## Environment Setup
### Set up environment variables

- [ ] **CHANNEL_SECRET**
The key for the *LINE Messaging API*, which can be obtained as outlined in [Connecting ChatGPT to LINE](https://www.explainthis.io/zh-hant/chatgpt/line).
- [ ] **CHANNEL_ACCESS_TOKEN**
Another key for the *LINE Messaging API*, obtainable following the instructions in [Connecting ChatGPT to LINE](https://www.explainthis.io/zh-hant/chatgpt/line).
- [ ] **OPENAI_API_KEY**
The OpenAI API key, attainable as explained in [Connecting ChatGPT to LINE](https://www.explainthis.io/zh-hant/chatgpt/line).
- [ ] **MONGO_CONNECTION_STR**
The connection key for the [MongoDB](https://www.mongodb.com/) database, details available at [An Introduction to MongoDB Connection Strings](https://www.mongodb.com/basics/mongodb-connection-string#:~:text=The%20MongoDB%20connection%20string%20for,port%20number%20you%20are%20using.).
- [ ] **TEMPERATURE**
The response temperature for the OpenAI API, ranging from 0 to 2, as described in the [API reference - OpenAI API](https://platform.openai.com/docs/api-reference/chat/create).
- [ ] **MAX_TOKEN_LIMIT**
The number of tokens to retain in the conversation memory, consult [LangChain- ConversationTokenBufferMemory](https://python.langchain.com/docs/modules/memory/types/token_buffer).

### Building Command
```bash
    pip install -r requirements.txt
```
### Start Command
```bash
    gunicorn app:app --timeout 3600
```
(Due to occasionally long response times from the OpenAI API, a longer timeout is set.)

## Reference Resources
- Repositories
    - [TheExplainthis/ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)
    - [line/line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master)
    - [langchain-ai/langchain](https://github.com/langchain-ai/langchain)
- Articles/Documentation
    - [Connecting ChatGPT to LINE - Making AI Your Personal Assistant](https://www.explainthis.io/zh-hant/chatgpt/line)
    - [Creating a Simple LineBot Chatbot in 30 Days](https://ithelp.ithome.com.tw/articles/10296331)
    - [LINE Developers Documentation](https://developers.line.biz/en/docs/)
    - [OpenAI Documentation](https://platform.openai.com/docs/introduction)
    - [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction.html)

## Contributing

Pull requests are welcome! For significant changes, please open an issue to discuss the proposed modifications.

## License
[MIT License](https://choosealicense.com/licenses/mit/)

This project's flexibility and scalability are substantial. Changing a prompt immediately transforms it into a different type of bot, and the use of [LangChain](https://github.com/langchain-ai/langchain) framework makes adding advanced features like embedding queries a straightforward task.

Feel free to use the code from this project to create various useful conversational bots by unleashing your imagination.
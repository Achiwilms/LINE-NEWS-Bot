# LINE-NEWS-Bot

一個提供新聞觀點的LINE對話機器人: AI, 你怎麼看?
## 介紹

在閱讀新聞時，是否曾覺得報導有些怪怪的，但又講不出怪在哪裡呢?

如果想聽聽其他觀點，這個LINE機器人很樂意提供它的看法🎙️  

將新聞連結分享給它，它會就報導的標題、觀點和呈現方式來評論這篇新聞，供你作為參考。

當然，不要完全接受它的意見，因為AI很容易出錯，評論也時常不正義😅  這不是什麼專業新聞評論，AI的看法僅供參考，請勿過於認真⚠️

另外，因為機器人是由與ChatGPT相同的GPT-3.5所驅動 🧠，所以如果你只是想輕鬆地跟我聊天，或想問新聞以外的問題，都是可以的喔！

<p align="center">
    <img src="https://github.com/Achiwilms/LINE-NEWS-Bot/blob/main/icon/demo.gif?raw=true" alt="GUI" width="200">
</p>


點擊加入好友👉👉 [AI, 你怎麼看?](https://liff.line.me/1645278921-kWRPP32q/?accountId=606bncqu)


## 環境設置
### 設置環境變數
    
- [ ] **CHANNEL_SECRET** 
*LINE Messaging API*的密鑰, 可參考[ChatGPT串接到LINE](https://www.explainthis.io/zh-hant/chatgpt/line)取得Line Token的段落
- [ ] **CHANNEL_ACCESS_TOKEN**
    *LINE Messaging API*的另一個密鑰, 可參考[ChatGPT串接到LINE](https://www.explainthis.io/zh-hant/chatgpt/line)取得Line Token的段落
- [ ] **OPENAI_API_KEY**
    OpenAI API密鑰, 可參考[ChatGPT串接到LINE](https://www.explainthis.io/zh-hant/chatgpt/line)取得OpenAI Token的段落
- [ ] **MONGO_CONNECTION_STR**
資料庫 [MongoDB](https://www.mongodb.com/)的連接密鑰, 可參考 [An Introduction to MongoDB Connection Strings](https://www.mongodb.com/basics/mongodb-connection-string#:~:text=The%20MongoDB%20connection%20string%20for,port%20number%20you%20are%20using.)
- [ ] **TEMPERATURE**
OpenAI API回應溫度, 介於0到2, 可參考 [API reference- OpenAI API](https://platform.openai.com/docs/api-reference/chat/create)
- [ ] **MAX_TOKEN_LIMIT**
保留對話記憶的Token數量, 可參考 [LangChain- ConversationTokenBufferMemory](https://python.langchain.com/docs/modules/memory/types/token_buffer)

### 建置指令
```bash
    pip install -r requirements.txt
```
### 開始指令
```bash
    gunicorn app:app --timeout 3600
```
(因為OpenAI API回應有時需要很久，故將Timeout時間設長)


## 參考資源
- Repository
    - [TheExplainthis/ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)
    - [line/line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master)
    - [langchain-ai/langchain](https://github.com/langchain-ai/langchain)
- 文章/說明文檔
    - [ChatGPT 串接到 LINE - 讓 AI 成為個人助理](https://www.explainthis.io/zh-hant/chatgpt/line)
    - [30天建構出一個簡單 LineBot 機器人系列](https://ithelp.ithome.com.tw/articles/10296331)
    - [LINE Developers -Documentation
](https://developers.line.biz/en/docs/)
    - [OpenAI -Documentation](https://platform.openai.com/docs/introduction)
    - [LangChain -Documentation](https://python.langchain.com/docs/get_started/introduction.html)

## 參與貢獻

歡迎發Pull request! 對於重大變更，請先開個Issue來討論你想更改的內容。

## License
[MIT License](https://choosealicense.com/licenses/mit/)

此專案的彈性與可擴充性我想是蠻大的。因為只要改個prompt馬上就能變另一種用途的機器人，而且使用了[LangChain](https://github.com/langchain-ai/langchain) 框架，要加上embedding query等進階功能都不是難事。

歡迎使用此專案的程式碼，發揮想像力造出各種好用的對話機器人。
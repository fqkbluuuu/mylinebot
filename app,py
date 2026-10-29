import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# TODO: 填入你在 LINE Developers 後台拿到金鑰
line_bot_api = LineBotApi('C6I5XayRb3R/QnjXtluHlWholOOv1KUzObEKcbI99VhIZ84CHFE7p3GgRnv1yGY/P7NHHwsShXLEgWGrVoqmc5GvyK4gkaOpWHXM3lDqHeWs4bxyhssC1nfg7E+CuWZIb6BIwGox9hqYhAAFw+PgtwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c7f6afa59cf241e8be7d81d37c098ae8')

@app.route("/callback", methods=['POST'])
def callback():
    # 取得 signature 驗證標頭
    signature = request.headers['X-Line-Signature']

    # 取得請求內容本文
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # 驗證簽章並處理訊息
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 處理使用者傳來的文字訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_text = event.message.text.strip()
    
    # 簡單的邏輯判斷
    if "天氣" in user_text:
        reply_text = "【天氣小幫手】今天全台天氣晴朗，出門記得注意防曬與補充水分喔！"
    elif "星座" in user_text:
        reply_text = "【星座運勢】今天運勢超級旺！尤其是牡羊座與天蠍座，做什麼事情都得心應手！"
    else:
        reply_text = f"你剛剛說的是：「{user_text}」嗎？你可以輸入「天氣」或「星座」來查詢對應資訊喔！"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )

if __name__ == "__main__":
    app.run(port=5000)


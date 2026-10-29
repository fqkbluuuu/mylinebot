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

    # --- 天氣查詢邏輯 ---
    if "基隆" in user_text:
        reply_text = "【基隆天氣】今日陰雨綿綿，氣溫 20~24°C，出門記得帶傘。"
    elif "台北" in user_text:
        reply_text = "【台北天氣】今日多雲短暫雨，氣溫 22~26°C，出門記得帶傘喔！"
    elif "新北" in user_text:
        reply_text = "【新北天氣】今日多雲時陰，氣溫 21~26°C，局部地區有雨。"
    elif "桃園" in user_text:
        reply_text = "【桃園天氣】今日多雲時晴，氣溫 21~26°C，午後風勢較大。"
    elif "新竹" in user_text:
        reply_text = "【新竹天氣】今日晴時多雲，風力較強，氣溫 21~25°C，注意保暖！"
    elif "苗栗" in user_text:
        reply_text = "【苗栗天氣】今日多雲時晴，氣溫 21~27°C，舒適宜人。"
    elif "台中" in user_text:
        reply_text = "【台中天氣】今日晴朗舒適，氣溫 23~28°C，非常適合出遊！"
    elif "彰化" in user_text:
        reply_text = "【彰化天氣】今日晴到多雲，氣溫 22~27°C，風力稍大。"
    elif "南投" in user_text:
        reply_text = "【南投天氣】今日多雲午後短暫陣雨，氣溫 20~27°C。"
    elif "雲林" in user_text:
        reply_text = "【雲林天氣】今日晴時多雲，氣溫 22~28°C，天氣穩定。"
    elif "嘉義" in user_text:
        reply_text = "【嘉義天氣】今日晴朗穩定，氣溫 22~28°C，陽光普照。"
    elif "台南" in user_text:
        reply_text = "【台南天氣】今日晴朗穩定，氣溫 24~29°C，溫暖舒適。"
    elif "高雄" in user_text:
        reply_text = "【高雄天氣】今日多雲到晴，氣溫 25~30°C，白天感受偏熱！"
    elif "屏東" in user_text:
        reply_text = "【屏東天氣】今日多雲時晴，氣溫 24~30°C，午後天氣炎熱。"
    elif "宜蘭" in user_text:
        reply_text = "【宜蘭天氣】今日陰時多雲短暫雨，氣溫 21~25°C，出門記得攜帶雨具。"
    elif "花蓮" in user_text:
        reply_text = "【花蓮天氣】今日多雲短暫雨，氣溫 22~26°C。"
    elif "台東" in user_text:
        reply_text = "【台東天氣】今日多雲時晴，氣溫 23~27°C，天氣舒適。"
    elif "澎湖" in user_text:
        reply_text = "【澎湖天氣】今日多雲，風浪較大，氣溫 23~26°C。"
    elif "金門" in user_text:
        reply_text = "【金門天氣】今日晴時多雲，早晚偏涼，氣溫 20~25°C。"
    elif "馬祖" in user_text:
        reply_text = "【馬祖天氣】今日多雲時陰，氣溫 18~22°C，注意保暖。"
    elif "天氣" in user_text:
        reply_text = "【天氣小幫手】你可以直接輸入想查詢的縣市（例如：新竹天氣、苗栗天氣）來查看喔！"

    # --- 星座運勢邏輯 ---
    elif "牡羊" in user_text:
        reply_text = "【牡羊座運勢】今日運勢 ★★★★☆！事業運極佳，有機會獲得意外的讚賞！"
    elif "金牛" in user_text:
        reply_text = "【金牛座運勢】今日運勢 ★★★☆☆！財運平穩，適合做好理財規劃。"
    elif "雙子" in user_text:
        reply_text = "【雙子座運勢】今日運勢 ★★★★★！靈感爆棚，社交運勢非常強勁！"
    elif "巨蟹" in user_text:
        reply_text = "【巨蟹座運勢】今日運勢 ★★★☆☆！感情運溫馨，多給家人與另一半一些關心。"
    elif "獅子" in user_text:
        reply_text = "【獅子座運勢】今日運勢 ★★★★☆！領導力大增，適合主動推進新計畫。"
    elif "處女" in user_text:
        reply_text = "【處女座運勢】今日運勢 ★★★★☆！細心度滿分，工作效率特別高。"
    elif "天秤" in user_text:
        reply_text = "【天秤座運勢】今日運勢 ★★★☆☆！人際關係和諧，適合參加聚會。"
    elif "天蠍" in user_text:
        reply_text = "【天蠍座運勢】今日運勢 ★★★★★！直覺敏銳，做決定時相信自己的第一直覺！"
    elif "射手" in user_text:
        reply_text = "【射手座運勢】今日運勢 ★★★★☆！充滿活力，適合出外走走放鬆心情。"
    elif "摩羯" in user_text:
        reply_text = "【摩羯座運勢】今日運勢 ★★★☆☆！努力會看到成果，保持耐性。"
    elif "水瓶" in user_text:
        reply_text = "【水瓶座運勢】今日運勢 ★★★★☆！創意無限，多嘗試新的想法。"
    elif "雙魚" in user_text:
        reply_text = "【雙魚座運勢】今日運勢 ★★★★☆！桃花運上升，保持微笑會帶來好運！"
    elif "星座" in user_text:
        reply_text = "【星座運勢】請輸入你的星座（例如：巨蟹座、雙子座）來查詢今天的運勢喔！"

    # --- 預設回覆 ---
    else:
        reply_text = f"你剛剛說的是：「{user_text}」嗎？你可以輸入「城市天氣」（如：新竹天氣）或「你的星座」（如：天蠍座）來查詢喔！"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )

if __name__ == "__main__":
    app.run(port=5000)


from flask import Flask, request
app = Flask(__name__)

# サーバールートへアクセスがあった時 --- (*1)
@app.route('/')
def index():
    # フォームを表示する --- (*2)
    return """
        <html><body>
        <form action="/hello" method="GET">
          名前: <input type="text" name="name"><br>
           ひとこと: <input type="text" name="message"><br>
          <input type="submit" value="送信">
        </form>
        </body></html>
    """

# /hello へアクセスがあった時 --- (*3)
@app.route('/hello')
def hello():
    # nameのパラメータを得る --- (*4)
    name = request.args.get('name')
    message = request.args.get('message')
    if name is None: 
        name = '名無し'
    if message is None: 
        message = 'ひとこと無し'
        
    # 自己紹介を自動作成
    return"""
    <h1>{0}さん、こんにちは！</h1>
    ひとこと :{1}
    """.format(name,message)

if __name__ == '__main__':
    app.run(host='0.0.0.0')



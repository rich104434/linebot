from flask import Flask  #匯入flask套件中的Flask類別
app = Flask(__name__)  #建立類別實體app（你也可以命名為別的）
#將__name__傳給Flask，讓直接呼叫本模組或透過其他模組呼叫本模組時，都可以使程式工作。

@app.route('/')  #@app.route來定義路由

def hello(): #執行的function
    return 'hello man'

if __name__ == '__main__':
    app.run() 

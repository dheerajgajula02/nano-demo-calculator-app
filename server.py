from flask import Flask, request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():

    data = request.json
    val1 = data['first']
    val2= data['second']
    print(val1,val2)

    return {  
        "result": int(data['first'])+int(data['second']),
    }  

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json
    val1 = data['first']
    val2= data['second']
    print(val1,val2)
    return {  
        "result": int(data['first'])-int(data['second']),
    } 

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')

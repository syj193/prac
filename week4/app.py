from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

 
## API 역할을 하는 부분
## { user_give: orderUser, quantity_give: quantity, address_give: address, phone_give:phonenumber,total_give:totalAmount }
@app.route('/orders', methods=['POST'])
def write_order():
    user_receive = request.form['user_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']
    total_receive = request.form['total_give'] 


    orders = {
       'user': user_receive,
       'quantity': quantity_receive,
       'address': address_receive,
       'phone': phone_receive,
       'total': total_receive
    }

    db.orders.insert_one(orders)
    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})


@app.route('/orders', methods=['GET'])
def read_orders():
    orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

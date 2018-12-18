from flask import Flask,jsonify,request
from flask_cors import CORS
import psycopg2
import datetime
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/burgers',methods=['GET'])
def get_burgers():
    conn = psycopg2.connect(database="postgres", user = "postgres", password = "post123", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute("SELECT *  from burger")
    burgers=[]
    rows = cur.fetchall()
    for row in rows:
        row[1]['id']=row[0]
        burgers.append(row[1])
    return jsonify({'burgers':burgers})


@app.route('/shakes',methods=['GET'])
def get_shakes():
    conn = psycopg2.connect(database="postgres", user = "postgres", password = "post123", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute("SELECT *  from shake")
    shakes=[]
    rows = cur.fetchall()
    for row in rows:
        row[1]['id']=row[0]
        shakes.append(row[1])
    return jsonify({'shakes':shakes})


@app.route('/salads',methods=['GET'])
def get_salads():
    conn = psycopg2.connect(database="postgres", user = "postgres", password = "post123", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute("SELECT *  from salad")
    salads=[]
    rows = cur.fetchall()
    for row in rows:
        row[1]['id']=row[0]
        salads.append(row[1])
    return jsonify({'salads':salads})


@app.route('/pastas',methods=['GET'])
def get_pastas():
    conn = psycopg2.connect(database="postgres", user = "postgres", password = "post123", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute("SELECT *  from pasta")
    pastas=[]
    rows = cur.fetchall()
    for row in rows:
        row[1]['id']=row[0]
        pastas.append(row[1])
    return jsonify({'pastas':pastas})


@app.route('/beverages',methods=['GET'])
def get_beverages():
    conn = psycopg2.connect(database="postgres", user = "postgres", password = "post123", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute("SELECT *  from beverage")
    beverages=[]
    rows = cur.fetchall()
    for row in rows:
        row[1]['id']=row[0]
        beverages.append(row[1])
    return jsonify({'beverages':beverages})

@app.route('/prevOrders',methods=['GET'])
def get_prevOrders():
    conn = psycopg2.connect(database="postgres", user = "postgres", password = "post123", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    customerId=request.args['customerId']
    cur.execute("select id,date from bill where customer_id=%s order by date desc limit 10",[customerId])
    rows = cur.fetchall()
    print("sql done")
    ids = []
    dates = []
    for row in rows:
        ids.append(row[0])
        dates.append(row[1].strftime('%d/%m/%Y'))
    conn.close()
    x = {"id":ids,"date":dates}
    return json.dumps(x)

@app.route('/getSalesData',methods=['GET'])
def get_salesData():
    conn = psycopg2.connect(database="postgres", user = "postgres", password = "post123", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    startDate=request.args['startDate']
    endDate=request.args['endDate']
    print(startDate,endDate)
    if not startDate:
        cur.execute("select id,final_total,date from bill where date <= %s;",[endDate])
    elif not endDate:
        cur.execute("select id,final_total,date from bill where date >= %s;",[startDate])
    else:
        cur.execute("select id,final_total,date from bill where date between %s and %s;",(startDate,endDate))
    rows = cur.fetchall()
    conn.close()
    length = len(rows)
    x = {
    "id":[length],
    "price":[length],
    "date":[length]
    }
    for record in rows:
        x['id'].append(record[0])
        x['price'].append(str(record[1]))
        x['date'].append(record[2].strftime('%d/%m/%Y'))
    print(len(rows))
    return json.dumps(x)


@app.route('/getOrder',methods=['GET'])
def getOrder():
    conn = psycopg2.connect(database="postgres", user = "postgres", password = "post123", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    orderId=request.args['orderId']
    cur.execute("select * from bill where id=%s",[orderId])
    rows=cur.fetchall()
    conn.close()
    orderDate = rows[0][5].strftime('%d/%m/%Y')
    x = {
        "orderId":rows[0][0],
        "cart":rows[0][1],
        "cartTotal":str(rows[0][2]),
        "gst":str(rows[0][3]*100)+'%',
        "finalTotal":str(rows[0][4]),
        "orderDate":orderDate
        }
    return json.dumps(x)


@app.route('/bill', methods=['POST'])
def create_bill():
    cart = request.json['cart']
    customerId=request.json['customerId']
    date = datetime.datetime.now()
    gst = 0.05
    cartTotal=0
    for item in cart:
        cartTotal+=item['price']
    finalTotal=cartTotal+cartTotal*0.05
    #db
    conn = psycopg2.connect(database="postgres", user = "postgres", password = "post123", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    sql = """INSERT INTO bill(cart,cart_total,gst,final_total,date,customer_id)
             VALUES(%s,%s,%s,%s,%s,%s) returning id;"""
    cur.execute(sql,(json.dumps(cart),cartTotal,gst,finalTotal,date,customerId))
    rows=cur.fetchall()
    conn.commit()
    cur.close()
    return str(rows[0][0])

@app.route('/login',methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']
    #db
    conn = psycopg2.connect(database="postgres", user = "postgres", password = "post123", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute("SELECT id from CUSTOMER where email=%s and password = %s",(email,password))
    rows=cur.fetchall()
    if(cur.rowcount==1):
        return str(rows[0][0])
    else:
        return str(0)
    conn.close()

@app.route('/addBurger',methods=['POST'])
def addBurger():
    burger={}
    burger['name']=request.json['name']
    burger['category']=request.json['category']
    burger['price']=request.json['price']
    s=json.dumps(burger)
    #db
    conn = psycopg2.connect(database="postgres", user = "postgres", password = "post123", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute("Insert into burger(data) values(%s)",[s])
    conn.commit()
    conn.close()
    return "1"

@app.route('/addSalad',methods=['POST'])
def addSalad():
    salad={}
    salad['name']=request.json['name']
    salad['category']=request.json['category']
    salad['price']=request.json['price']
    s=json.dumps(salad)
    #db
    conn = psycopg2.connect(database="postgres", user = "postgres", password = "post123", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute("Insert into salad(data) values(%s)",[s])
    conn.commit()
    conn.close()
    return "1"

@app.route('/addPasta',methods=['POST'])
def addPasta():
    pasta={}
    pasta['name']=request.json['name']
    pasta['category']=request.json['category']
    pasta['price']=request.json['price']
    s=json.dumps(pasta)
    #db
    conn = psycopg2.connect(database="postgres", user = "postgres", password = "post123", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute("Insert into pasta(data) values(%s)",[s])
    conn.commit()
    conn.close()
    return "1"

@app.route('/addShake',methods=['POST'])
def addShake():
    shake={}
    shake['name']=request.json['name']
    shake['price']=request.json['price']
    s=json.dumps(shake)
    #db
    conn = psycopg2.connect(database="postgres", user = "postgres", password = "post123", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute("Insert into shake(data) values(%s)",[s])
    conn.commit()
    conn.close()
    return "1"

@app.route('/addBeverage',methods=['POST'])
def addBeverage():
    beverage={}
    beverage['name']=request.json['name']
    beverage['price']=request.json['price']
    s=json.dumps(beverage)
    #db
    conn = psycopg2.connect(database="postgres", user = "postgres", password = "post123", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute("Insert into beverage(data) values(%s)",[s])
    conn.commit()
    conn.close()
    return "1"


@app.route('/register',methods=['POST'])
def register():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    address = request.json['address']
    #db
    conn = psycopg2.connect(database="postgres", user = "postgres", password = "post123", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    sql = """INSERT INTO customer(name,email,password,address)
             VALUES(%s,%s,%s,%s);"""
    try:
        cur.execute(sql,(name,email,password,address))
    except psycopg2.IntegrityError:
        return "2"
    conn.commit()
    conn.close()
    return "1" 




if __name__ == "__main__":
    app.run(debug='true')


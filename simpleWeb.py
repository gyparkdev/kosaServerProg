from flask import Flask, request, render_template, jsonify, _app_ctx_stack

# sqlite를 사용할 수 있도록 구성해 보자.
import sqlite3

'''
CREATE TABLE appdata (
    id INTEGER AUTO_INCREMENT,
    time datetime DEFAULT current_timestamp,
    kor INTEGER,
    math INTEGER,
    PRIMARY KEY(id)
)
'''

DATABASE = 'data.db'

app = Flask(__name__, static_folder='static', template_folder='template')

@app.route('/')
def hello():
    return 'Hello'

@app.route('/hi')
def hi():
    return 'Hi~~~'

@app.route('/sample')
def sample():
    return render_template('sample.html')

# add() 덧셈에 해당하는 라우터를 추가
@app.route('/add', methods=['GET', 'POST'])
def add():
    a = 0
    b = 0
    
    if request.method == 'GET':
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
    if request.method == 'POST':
        data = request.get_json()
        a = int(data['a'])
        b = int(data['b'])
        
    return str(a+b)
    
# 데이터베이스 열기
def get_db():
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        top.sqlite_db = sqlite3.connect(DATABASE)
    return top.sqlite_db

# 데이터베이스 정리
@app.teardown_appcontext
def close_connection(exception):
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()  
       
# reset을 허가된 (인가된) 요청에만 대응
# ==> POST로 변경하고 JSON에 {“API_KEY” : “abcd”}
 
@app.route('/reset', methods = ['POST'])
def reset():
    if request.is_json:
        data = request.get_json()
        
        if data["API_KEY"] == "1234":   
            try:
                cur = get_db().cursor()
                cur.execute('DROP TABLE IF EXISTS appdata')
                cur.execute('CREATE TABLE appdata (id INTEGER AUTO_INCREMENT,time datetime DEFAULT current_timestamp,kor INTEGER, math INTEGER,PRIMARY KEY(id))')
                get_db().commit()
            except:
                get_db().rollback()
            return "Successfully reset"
        else:
            return "Invalid API_KEY"
    else:
        return "Invalid request"
    
# DB 입력
@app.route('/insert', methods = ['POST'])
def insert():
    data = request.get_json()
    kor = data['kor']
    math = data['math']
    
    try:
        cur = get_db().cursor()
        cur.execute("insert into appdata(kor,math) values(?,?)", (kor,math))
        get_db().commit()
    except:
        get_db().rollback()
    return jsonify(code=0)

# DB 가져오는 것(암기해서 사용)
# 데이터베이스 처리 결과를 딕셔너리 형태로 반환
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# DB 조회
@app.route('/select')
def select():
    result = []
    try:
        get_db().row_factory = dict_factory
        cur = get_db().cursor()
        cur.execute('SELECT time, kor, math FROM appdata')
        result = cur.fetchall()
        print(result)
    except:
        get_db().rollback()
    return render_template('select.html', data = result)
    
if __name__ == '__main__':
    app.run(
    host="127.0.0.1",
    port=7777,
    debug=True)
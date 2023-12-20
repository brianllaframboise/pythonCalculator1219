from flask import Flask, render_template, url_for, request # url_for 추가

app = Flask(__name__, static_url_path='/static') # ,static_url_path='/static/ 추가

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/enter/<name>')
def enter(name):
	return render_template('page.html', name=name)

global inputNum

@app.route('/sideLength', methods=['POST', 'GET'])
def sideLength():
	globals()["inputNum"] = request.args.get('num')
	localNum = int(globals()["inputNum"])
	return render_template('page.html', num=localNum) # , char1=temp1)

@app.route('/getNumOne', methods=['POST', 'GET'])
def getNumOne():
	localNum = int(globals()["inputNum"])
	return render_template('page.html', num=localNum,num1=localNum)

@app.route('/getNumTwo', methods=['POST', 'GET'])
def getNumTwo():
	localNum = int(globals()["inputNum"])
	return render_template('page.html', num=localNum,num2=localNum)

@app.route('/getNumThree', methods=['POST', 'GET'])
def getNumThree():
	localNum = int(globals()["inputNum"])
	return render_template('page.html', num=localNum,num3=localNum)

	# elif request.method == 'GET':
	# 	## 넘겨받은 숫자
	# 	temp = request.args.get('num')
	# 	temp = int(temp)
	# 	## 넘겨받은 문자
	# 	# temp1 = request.args.get('char1')
	# 	## 넘겨받은 값을 원래 페이지로 리다이렉트
	# 	return render_template('page.html', num2=temp) # , char1=temp1)
	# ## else 로 하지 않은 것은 POST, GET 이외에 다른 method로 넘어왔을 때를 구분하기 위함

	# elif request.method == 'GET':
	# 	## 넘겨받은 숫자
	# 	temp = request.args.get('num')
	# 	temp = int(temp)
	# 	## 넘겨받은 문자
	# 	# temp1 = request.args.get('char1')
	# 	## 넘겨받은 값을 원래 페이지로 리다이렉트
	# 	return render_template('page.html', num3=temp) # , char1=temp1)
	# ## else 로 하지 않은 것은 POST, GET 이외에 다른 method로 넘어왔을 때를 구분하기 위함

if __name__=='__main__':
	# threaded=Ture로 넘기면 multiple plot이 가능해집니다.
	app.run(debug=True, threaded=True) #, host="0.0.0.0",port=5000)
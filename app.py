from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

accounts={}

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/dashboard',methods=['POST'])
def Dashboard():
    acc_no=request.form['acc_no']
    name=request.form['name']
    balance=int(request.form['balance'])
    accounts[acc_no]={'name':name,'balance':balance} 
    data=accounts[acc_no]
    return render_template('dashboard.html',data=data,acc_no=acc_no)

@app.route('/deposit/<acc_no>',methods=['POST'])
def Deposit(acc_no):
    amount=int(request.form['amount'])
    if amount>0:
        accounts[acc_no]['balance']+=amount
        data=accounts[acc_no]
        return render_template('dashboard.html',data=data,acc_no=acc_no)
    else:
        return render_template('error.html')   

@app.route('/withdraw/<acc_no>',methods=['POST'])
def withdraw(acc_no):
    amount=int(request.form['amount'])
    if 0<amount<accounts[acc_no]['balance']:
        accounts[acc_no]['balance']-=amount
        data=accounts[acc_no]
        return render_template('dashboard.html',data=data,acc_no=acc_no)
    else:
        return render_template('error.html')    

if __name__=="__main__":
    app.run(debug=True)
    
from flask import Flask, render_template,request
import os
import module.calculator

app = Flask(__name__)

@app.route("/")
def search():
    return "Hello World"

@app.route("/tax")
def test():
    return render_template("main.html")

@app.route("/result" , methods=['POST'])
def calc():
    kifu = int(request.form['kifu'])
    syotoku = int(request.form['syotoku'])
    songai = int(request.form['songai'])
    sisyutu = int(request.form['sisyutu'])
    hoken = int(request.form['hoken'])
    child = int(request.form['child'])
    haigu = int(request.form['haigu'])
    kifu_ans = module.calculator.kifukin(syotoku,kifu)
    zasson_ans = module.calculator.zasson(syotoku,songai,sisyutu,hoken)
    hitori_ans = module.calculator.hitorioya(syotoku,child)
    haigu_ans = module.calculator.haigu_tokubetu(syotoku,haigu)
    result = '寄付金控除は'+str(kifu_ans)+'円です。<br>'
    result += '雑損控除は'+str(zasson_ans)+'円です。<br>'
    result += '一人親控除は'+str(hitori_ans)+'円です。<br>'
    result += '配偶者特別控除は'+str(haigu_ans)+'円です。<br>'
    return result

if __name__ == "__main__":
    app.run(debug=True)
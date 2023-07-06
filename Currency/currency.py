from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        to = request.form["Tcurrency"]
        fro = request.form["Fcurrency"]
        money = float(request.form["money"])
        return convert(fro, to, money)
    return render_template("currency.html")

@app.route("/convert", methods=["GET", "POST"])
def convert(from_currency, to_currency, money):
    converted_currency = {
        "from" : from_currency,
        "to" : to_currency,
        "money" : money,
        "converted" : 0
    }
    if from_currency == "Doller":
        if to_currency == "Euro":
            converted_currency["converted"] = "{:.2f}".format(money * 0.92)
        elif to_currency == "Rupee":
            converted_currency["converted"] = "{:.2f}".format(money * 82.53)
        else:
            converted_currency["converted"] = money
    if from_currency == "Euro":
        if to_currency == "Doller":
            converted_currency["converted"] = "{:.2f}".format(money * 1.09)
        elif to_currency == "Rupee":
            converted_currency["converted"] = "{:.2f}".format(money * 82.53)
        else:
            converted_currency["converted"] = money
    if from_currency == "Rupee":
        if to_currency == "Euro":
            converted_currency["converted"] = "{:.2f}".format(money * 0.011)
        elif to_currency == "Doller":
            converted_currency["converted"] = "{:.2f}".format(money * 0.012)
        else:
            converted_currency["converted"] = money
    return render_template("currency.html", converted_currency=converted_currency)
if __name__ == "__main__":
    app.run(debug=True)


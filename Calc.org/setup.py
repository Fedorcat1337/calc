from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def Home():
	a = request.args.get('a', None)
	b = request.args.get('b', None)
	c = request.args.get('c', None)
	try:

		if (a.strip('-')).isnumeric() and (b.strip("-")).isnumeric() and (c.strip("-")).isnumeric() and a != "0" and b != "0" and c != "0":

			a = int(a)
			b = int(b)
			c = int(c)
			D = b**2-4*a*c
		
			if D < 0:

				am = "У этого уравнения нет корней."
				x1 = ""
				x2 = ""
		
			elif D == 0:

				am = "У этого уравнения 1 корень."
				x1 = str(-b/2*a)
				x2 = ""

			elif D > 0:

				am = "У этого уравнения 2 корня."
				x1 = str((-b+(b**2-4*a*c)**0.5)/(2*a))
				x2 = str((-b-(b**2-4*a*c)**0.5)/(2*a))

			return render_template("calc.html", a = a, b = b, c = c, x1 = x1, x2 = x2, am = am)

		else:

			return render_template("calc.html", a = "a", b = "b", c = "c", x1 = "", x2 = "", am = "Введите уравнение вида:")

	except AttributeError:

		return render_template("calc.html", a = "a", b = "b", c = "c", x1 = "", x2 = "", am = "Введите уравнение вида:")

app.run(debug = True)
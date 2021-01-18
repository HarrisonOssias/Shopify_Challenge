from flask import Flask, redirect, url_for, render_template, request
import sort_compare

app = Flask(__name__)

# Defining the home page of our site
# arrayq = list(map(int, input("Please enter all values separated by spaces\n").split()))




@ app.route("/", methods=["POST", "GET"])  # this sets the route to this page
def home():
    if request.method == "POST":
            array = request.form["nm"].split()
            mapped = map(int, array)
            arrayq = list(mapped)
            print(arrayq)
            arrayb=arrayq[:]
            arraym=arrayq[:]
            quicktime= sort_compare.track_quick(arrayq, 0, len(arrayq) - 1)

            mergetime= sort_compare.track_merge(arraym)

            bubtime= sort_compare.track_bubble(arrayb)

            return render_template("index.html", sorted=arrayq, quick=quicktime, merge=mergetime, bub=bubtime)

    else:
	    return render_template("index.html")

    



if __name__ == "__main__":
    app.run()

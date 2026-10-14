from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    name = request.form.get("name")
    email = request.form.get("email")
    course = request.form.get("course")

    return render_template(
        "success.html",
        name=name,
        email=email,
        course=course
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
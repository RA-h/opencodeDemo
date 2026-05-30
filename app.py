from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "dev-secret-key-change-in-production"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        flash(f"Thanks {name}! We'll get back to you at {email} soon.")
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

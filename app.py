from flask import Flask, render_template, request

app = Flask(__name__)

# demo-only (in-memory)
users = {}

@app.get("/")
def home():
    return render_template("home.html")

@app.get("/signup")
def signup_form():
    return render_template("signup.html")

@app.post("/signup")
def signup_submit():
    first = request.form.get("first_name", "").strip()
    last = request.form.get("last_name", "").strip()
    email = request.form.get("email", "").strip().lower()

    if not first or not last or not email:
        return render_template("signup.html", error="Please fill all fields.")

    users[email] = {"first": first, "last": last}
    return render_template("thanks.html", message=f"Thanks for signing up, {first}!")

@app.get("/login")
def login_form():
    return render_template("login.html")

@app.post("/login")
def login_submit():
    email = request.form.get("email", "").strip().lower()
    _password = request.form.get("password", "").strip()  # dummy

    if email in users:
        return render_template("thanks.html", message=f"Welcome back, {users[email]['first']}!")
    return render_template("login.html", error="User not found. Please sign up first.")

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
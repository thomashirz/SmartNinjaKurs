from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route("/", methods=["GET"]) #method ist eine Liste --> man kann mehrere hinzufügen
def index():
    page_title = "Homepage"

    cities = ["Wien", "Prag", "Bratislava", "London"]

    return render_template("index.html", page_title=page_title, cities=cities)


@app.route("/impressum")
def impressum():
    return render_template("impressum.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST"])
def success():
    if request.method == "GET":
        user_name = request.cookies.get("user_name")
        return render_template("success.html", name=user_name)
    else:
        contact_name = request.form.get("contact-name")
        contact_mail = request.form.get("contact-email")
        contact_textbox = request.form.get("contact-message")

        response = make_response(render_template(success.html, name=contact_name, mail=contact_mail, user_message=contact_textbox))
        response.set_cookie("user_name", contact_name)

        return response


if __name__ == "__main__":
    app.debug = False
    app.run()

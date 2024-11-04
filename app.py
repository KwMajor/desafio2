from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = ""
app.config["AQLALCHEMY_TRACK_MODIFICARIONS"] = False
db = SQLAlchemy(app)

class Contato(db.Model):
    __tablename__ = "contato"
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20))
    mensagem = db.column(db.Text, nullable=False)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/contacts")
def listar_contatos():
    contatos = Contato.query.all()
    return render_template("contacts.html", contatos = contatos)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        contato = Contato(
            nome_completo = request.form["nome_completo"],
            email = request.form["email"],
            telefone = request.form["telefone"],
            mensagem = request.form["mensagem"]
        )
        db.session.add(contato)
        db.session.commit()
        return redirect(url_for("contato"))
    return render_template("contact.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


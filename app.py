from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:fatec@localhost/desafiodevweb"
app.config["SQLALCHEMY_TRACK_MODIFICARIONS"] = False
db = SQLAlchemy(app)

class Contato(db.Model):
    __tablename__ = "contato"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    assunto = db.Column(db.Text, nullable=False)
    mensagem = db.Column(db.Text, nullable=False)


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
    # Busca todos os registros da tabela contato
    contatos = Contato.query.all()
    return render_template("contacts.html", contatos=contatos)

@app.route("/addCC", methods=["POST"])
def add():
    if request.method == "POST":
        contato = Contato(
            email = request.form["email"],
            assunto = request.form["assunto"],
            mensagem = request.form["mensagem"]
        )
        db.session.add(contato)
        db.session.commit()
        return redirect(url_for("contact"))
    return render_template("contact.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


from flask import Flask, render_template, request, jsonify
from config import Config
from models import db, Empresa, Usuario, Atividade, Comentario
from math import ceil

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route("/")
def index():
    tipo = request.args.get("tipo")
    page = request.args.get("page", 1, type=int)

    query = Atividade.query
    if tipo:
        query = query.filter_by(tipo=tipo)

    total = query.count()
    por_pagina = 4
    paginas = ceil(total / por_pagina)

    atividades = query.order_by(
        Atividade.criado_em.desc()
    ).offset((page-1)*por_pagina).limit(por_pagina)

    empresa = Empresa.query.first()

    total_cal = db.session.query(
        db.func.sum(Atividade.calorias)
    ).scalar() or 0

    total_ativ = Atividade.query.count()

    return render_template("index.html",
        atividades=atividades,
        empresa=empresa,
        paginas=paginas,
        page=page,
        tipo=tipo,
        total_cal=total_cal,
        total_ativ=total_ativ)

@app.route("/like/<int:id>", methods=["POST"])
def like(id):
    a = Atividade.query.get(id)
    a.likes_count += 1
    db.session.commit()
    return jsonify({"likes": a.likes_count})

@app.route("/comentario", methods=["POST"])
def comentar():
    data = request.json
    texto = data["texto"]

    if len(texto) < 3:
        return jsonify({"erro":"Inválido"}),400

    c = Comentario(
        atividade_id=data["atividade_id"],
        texto=texto
    )

    db.session.add(c)
    db.session.commit()

    return jsonify({
        "texto": c.texto,
        "data": c.criado_em.strftime("%H:%M - %d/%m/%y")
    })

if __name__=="__main__":
    app.run(debug=True)

from flask import Flask, render_template, abort, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from models import Projet, db
from forms import ProjetForm
import secrets

app = Flask(__name__)

# Configuration BDD SQLAlchemy 
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "faye123" # Clé secrète pour les sessions



# Initialisation de la base de données
# db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)


# Simule une base de données de projets
projets = [
    {
        "id": 1,
        "slug": "ai-portfolio",
        "titre": "Projet AI Portfolio",
        "description": "Un projet de génération de portfolio automatique avec GPT & Flask.",
        "image": "images/site00.png",
        "tech": ["Python", "Flask", "OpenAI API"]
    },
    {
        "id": 2,
        "slug": "ecommerce-django",
        "titre": "Site e-commerce Django",
        "description": "Un site de vente en ligne avec panier et paiement Stripe.",
        "image": "images/site01.png",
        "tech": ["Django", "Stripe", "PostgreSQL"]
    },
    {
        "id": 3,
        "slug": "api-flask",
        "titre": "API RESTful Flask",
        "description": "Une API complète pour gérer des utilisateurs et des tâches.",
        "image": "images/site03.png",
        "tech": ["Flask-RESTful", "JWT", "SQLAlchemy"]
    },
    {
        "id": 4,
        "slug": "api-django",
        "titre": "API RESTful Django",
        "description": "Une API complète pour gérer des utilisateurs et des tâches.",
        "image": "images/site04.png",
        "tech": ["Flask-RESTful", "JWT", "SQLAlchemy"]
    }
]

@app.route('/')
def home():
    projets = Projet.query.all()  # Récupère tous les projets de la base de données
    return render_template('index.html', title="Mon Portofolio", name="OUSSEYNOU", projets=projets)

@app.route('/projet/<slug>')
def projet_detail(slug):
    # Recherche du projet par son slug
    projet = Projet.query.filter_by(slug=slug).first()
    if projet:
        return render_template('projet.html', projet=projet)
    else:
        abort(404)


# Erreur 404 - Page non trouvée
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', title="Page non trouvée"), 404

# Erreur 500 - Erreur interne du serveur
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', title="Erreur interne du serveur"), 500


@app.route('/generic')
def generic():
    return render_template('generic.html', title="Generic Page")

@app.route('/elements')
def elements():
    return render_template('elements.html', title="Elements Page")

@app.route('/ajouter-projet', methods=['GET', 'POST'])
def ajouter_projet():
    
    form = ProjetForm()
    
    if form.validate_on_submit():
        # Création d'un nouveau projet
        nouveau_projet = Projet(
            title=form.titre.data,
            slug=form.slug.data,
            description=form.description.data,
            image=form.image.data or 'images/site01.png',  # Valeur par défaut si aucune image n'est fournie
            tech=form.tech.data or 'Python, Flask'  # Valeur par défaut si aucune technologie n'est fournie
        )
        
        # Enregistrement du projet dans la base de données
        db.session.add(nouveau_projet)
        db.session.commit()
        
        return redirect(url_for('home'))
    
    return render_template('ajouter_projet.html', title="Ajouter un Projet", form=form)
        







if __name__ == '__main__':
    app.run(debug=True)
    

"""
    Ajouter des données manuellement dans la base de données
"""
@app.cli.command('seed')
def seed():
    """Command to seed the database with initial data."""
    from models import Projet
    
    db.session.query(Projet).delete()  # Clear existing data
    db.session.commit()  # Commit the deletion
    
    
    p1 = Projet(
        slug="ai-portfolio",
        title="Projet AI Portfolio",
        description="Un projet de génération de portfolio automatique avec GPT & Flask.",
        image="images/site00.png",
        tech="Python, Flask, OpenAI API"
    )
    p2 = Projet(
        slug="ecommerce-django",
        title="Site e-commerce Django",
        description="Un site de vente en ligne avec panier et paiement Stripe.",
        image="images/site01.png",
        tech="Django, Stripe, PostgreSQL"
    )
    p3 = Projet(
        slug="api-flask",
        title="API RESTful Flask",
        description="Une API complète pour gérer des utilisateurs et des tâches.",
        image="images/site03.png",
        tech="Flask-RESTful, JWT, SQLAlchemy"
    )
    p4 = Projet(
        slug="api-django",
        title="API RESTful Django Flask",
        description="Une API complète pour gérer des utilisateurs et des tâches.",
        image="images/site04.png",
        tech="Flask-RESTful, JWT, SQLAlchemy"
    )
    p5 = Projet(
        slug="api-django-flask",
        title="API RESTful Django Flask",
        description="Une API complète pour gérer des utilisateurs et des tâches.",
        image="images/site00.png",
        tech="Flask-RESTful, JWT, SQLAlchemy"
    )
    
    db.session.add_all([p1, p2, p3, p4, p5])
    db.session.commit()
    print("Database seeded with initial projects.")


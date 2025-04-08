from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fragrance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Create tables before any request
with app.app_context():
    db.create_all()
    print("Database tables created!")

# Database Models
class Fragrance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    top_notes = db.Column(db.String(200))
    middle_notes = db.Column(db.String(200))
    base_notes = db.Column(db.String(200))
    price = db.Column(db.Float)
    gender = db.Column(db.String(20))
    season = db.Column(db.String(20))
    occasion = db.Column(db.String(50))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preferences', methods=['GET', 'POST'])
def preferences():
    if request.method == 'POST':
        try:
            # Store preferences in session
            session['preferences'] = {
                'preferred_notes': request.form.get('preferred_notes', ''),
                'preferred_families': request.form.get('preferred_families', ''),
                'intensity': request.form.get('intensity'),
                'season': request.form.get('season'),
                'occasion': request.form.get('occasion'),
                'price_range': request.form.get('price_range')
            }
            flash('Preferences saved successfully!', 'success')
            return redirect(url_for('recommendations'))
            
        except Exception as e:
            flash(f'Error saving preferences: {str(e)}', 'error')
            return redirect(url_for('preferences'))
    
    return render_template('preferences.html')

@app.route('/recommendations')
def recommendations():
    # Get preferences from session
    preferences = session.get('preferences')
    if not preferences:
        flash('Please set your preferences first', 'info')
        return redirect(url_for('preferences'))
    
    # Get preferred notes and families
    preferred_notes = preferences['preferred_notes'].split(',') if preferences['preferred_notes'] else []
    preferred_families = preferences['preferred_families'].split(',') if preferences['preferred_families'] else []
    
    # Start with all fragrances
    query = Fragrance.query
    
    # Filter by preferred notes if any
    if preferred_notes:
        note_conditions = []
        for note in preferred_notes:
            note_conditions.append(Fragrance.top_notes.contains(note))
            note_conditions.append(Fragrance.middle_notes.contains(note))
            note_conditions.append(Fragrance.base_notes.contains(note))
        query = query.filter(db.or_(*note_conditions))
    
    # Filter by season if specified
    if preferences['season'] and preferences['season'] != 'all':
        query = query.filter(Fragrance.season == preferences['season'])
    
    # Filter by occasion if specified
    if preferences['occasion']:
        query = query.filter(Fragrance.occasion == preferences['occasion'])
    
    # Filter by price range if specified
    if preferences['price_range']:
        if preferences['price_range'] == 'budget':
            query = query.filter(Fragrance.price <= 50)
        elif preferences['price_range'] == 'mid':
            query = query.filter(Fragrance.price > 50, Fragrance.price <= 150)
        elif preferences['price_range'] == 'luxury':
            query = query.filter(Fragrance.price > 150)
    
    # Get recommended fragrances
    recommended_fragrances = query.limit(5).all()
    
    if not recommended_fragrances:
        flash('No exact matches found. Here are some general recommendations:', 'info')
        recommended_fragrances = Fragrance.query.limit(5).all()
    
    return render_template('recommendations.html', fragrances=recommended_fragrances)

@app.route('/creator')
def creator():
    return render_template('creator.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 
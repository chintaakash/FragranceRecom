from app import app, db, Fragrance

def init_db():
    with app.app_context():
        # Drop all existing tables
        db.drop_all()
        print("Dropped existing tables!")
        
        # Create all tables
        db.create_all()
        print("Created database tables!")

        # Sample fragrances
        fragrances = [
            {
                'name': 'Sauvage',
                'brand': 'Dior',
                'top_notes': 'Bergamot, Pepper',
                'middle_notes': 'Lavender, Pink Pepper',
                'base_notes': 'Ambroxan, Cedar',
                'price': 95.00,
                'gender': 'Men',
                'season': 'all',
                'occasion': 'daytime'
            },
            {
                'name': 'Black Orchid',
                'brand': 'Tom Ford',
                'top_notes': 'Truffle, Ylang-Ylang',
                'middle_notes': 'Black Orchid, Spices',
                'base_notes': 'Patchouli, Vanilla',
                'price': 150.00,
                'gender': 'Unisex',
                'season': 'winter',
                'occasion': 'evening'
            },
            {
                'name': 'Light Blue',
                'brand': 'Dolce & Gabbana',
                'top_notes': 'Sicilian Lemon, Apple',
                'middle_notes': 'Bamboo, Jasmine',
                'base_notes': 'Cedar, Musk',
                'price': 75.00,
                'gender': 'Women',
                'season': 'summer',
                'occasion': 'daytime'
            },
            {
                'name': 'Acqua di Gio',
                'brand': 'Giorgio Armani',
                'top_notes': 'Lemon, Neroli',
                'middle_notes': 'Jasmine, Rosemary',
                'base_notes': 'Patchouli, Musk',
                'price': 85.00,
                'gender': 'Men',
                'season': 'summer',
                'occasion': 'daytime'
            },
            {
                'name': 'La Vie Est Belle',
                'brand': 'Lancôme',
                'top_notes': 'Black Currant, Pear',
                'middle_notes': 'Iris, Jasmine',
                'base_notes': 'Patchouli, Vanilla',
                'price': 120.00,
                'gender': 'Women',
                'season': 'all',
                'occasion': 'evening'
            }
        ]

        # Add fragrances to database
        for fragrance_data in fragrances:
            fragrance = Fragrance(**fragrance_data)
            db.session.add(fragrance)

        db.session.commit()
        print("Database initialized with sample data!")

if __name__ == '__main__':
    init_db() 
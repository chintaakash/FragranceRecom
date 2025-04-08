# Fragrance Recommender

A web application that recommends fragrances based on user preferences.

## Local Development

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python src/app.py
```

## Deployment to Render.com

1. Create a new Web Service on Render.com
2. Connect your GitHub repository
3. Set the following environment variables:
   - `FLASK_APP`: src/app.py
   - `FLASK_ENV`: production
4. Deploy!

The application will be available at: https://your-app-name.onrender.com

## Features

- User preference collection
- Fragrance database
- Recommendation engine
- User profiles
- Rating system
- Social features

## Project Structure

- `data/`: Contains fragrance database and user data
- `src/`: Source code
- `tests/`: Test files

## License

MIT License
# FragranceRecom


from flask import Flask, render_template, request
from pathlib import Path
from flask import send_from_directory

app = Flask(__name__)

@app.route('/image.png')
def serve_image():
    return send_from_directory(Path(app.root_path) / 'images', 'image.png')


def recommend_perfume(mood, scent, occasion):

    fragrances = {
        "floral": {
            "name": "Miss Dior",
            "description": "A beautiful floral fragrance with a romantic character."
        },
        "citrus": {
            "name" : "Nishane Hacivat",
            "description": "A warm citrus fragrance with woody appeal."
        },
        "woody": {
            "name": "Le Labo Santal 33",
            "description": "A distinctive woody fragrance with a sophisticated feel."
        },
        "gourmand": {
            "name": "Kayali Vanilla 28",
            "description": "A warm, sweet fragrance with rich vanilla notes."
        },
        "fresh": {
            "name": "Dolce & Gabbana Light Blue",
            "description": "A fresh, clean fragrance with a bright character."
        },
        "amber-oriental": {
            "name": "Givenchy L'Interdit",
            "description": "A well-blended oriental fragrance with warm amber notes."

        }
    }

    mood_messages = {
        "romantic": "Perfect for your romantic side.",
        "confident": "A fragrance to match your confident energy.",
        "relaxed": "Something effortless for your relaxed mood.",
        "mysterious": "A scent for your mysterious side.",
        "sensual": "A fragrance that enhances your sensuality."
        
    }

    occasion_messages = {
        "everyday": "An easy choice for everyday wear.",
        "date night": "A lovely choice for date night.",
        "special occasion": "Something memorable for a special occasion.",
        "casual": "A fragrance for casual outings and relaxed settings."
    }

    perfume = fragrances.get(scent, fragrances["floral"])

    mood_message = mood_messages.get(mood, "")
    occasion_message = occasion_messages.get(occasion, "")

    return {
        "name": perfume["name"],
        "description": perfume["description"],
        "reason": f"{mood_message} {occasion_message}"
    }


@app.route('/')
def home():
    return render_template(
        'index.html',
        recommendation=None,
        mood='romantic',
        scent='floral',
        occasion='date night'
    )

@app.route('/recommend', methods=['POST'])
def recommend():

    mood = request.form.get('mood')
    scent = request.form.get('scent')
    occasion = request.form.get('occasion')

    recommendation = recommend_perfume(mood, scent, occasion)

    return render_template(
        'index.html',
        recommendation=recommendation,
        mood=mood,
        scent=scent,
        occasion=occasion
    )


if __name__ == '__main__':
    app.run(debug=True)


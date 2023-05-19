import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for


def loadClubs():
    with open('clubs.json') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


def loadCompetitions():
    with open('competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


app = Flask(__name__)
app.secret_key = 'something_special'


competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html', club=club, competitions=competitions)
    except IndexError:
        if request.form['email'] == '':
            message = "Enter an email"
        else:
            message = 'Invalid email'
        flash(message)
        return redirect(url_for('index'), code=302)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    found_club = [c for c in clubs if c['name'] == club][0]
    found_competition = [c for c in competitions if c['name'] == competition][0]

    if found_club and found_competition and (datetime.strptime(found_competition['date'],
                                                               "%Y-%m-%d %H:%M:%S") > datetime.now()):
        return render_template('booking.html', club=found_club, competition=found_competition)
    else:
        flash("You cannot reserve seats, expired date.")
        return render_template('welcome.html', club=found_club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])

    # places_required ne depasse pas le nombres de places que possede le club
    if places_required > int(club["points"]):
        flash(f"Your selected place number is superior than {club['points']}")
    # places_required ne dépasse pas le nombres de places disponible pour la compétition
    elif places_required > int(competition['numberOfPlaces']):
        flash(f"""The number of places selected is greater than the place of competition,
                you only have them {competition['numberOfPlaces']}""")
    # vérifie si places_required ne dépasse pas 12
    elif places_required > 12:
        flash("You cannot reserve more than 12 places for this tournament.")
    else:
        competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
        club['points'] = int(club['points']) - places_required
        flash(f'Great-booking complete! {places_required} places')
    return render_template('welcome.html', club=club, competitions=competitions)

# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)

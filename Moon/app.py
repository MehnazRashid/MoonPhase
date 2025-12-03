from flask import Flask, render_template
from datetime import datetime
import math

app = Flask(__name__)


def calculate_moon_phase(date):
    Y = date.year
    M = date.month
    D = date.day

    if M == 1 or M == 2:
        Y -= 1
        M += 12

    A = math.floor(Y / 100)
    B = math.floor(A / 4)
    C = 2 - A + B
    E = math.floor(365.25 * (Y + 4716))
    F = math.floor(30.6001 * (M + 1))
    JD = C + D + E + F - 1524.5

    days_since_new = JD - 2451549.5
    new_moons = days_since_new / 29.53
    fraction_of_cycle = new_moons - math.floor(new_moons)
    days_into_cycle = fraction_of_cycle * 29.53

    return round(days_into_cycle, 2)


def get_moon_image(days_into_cycle):
    if days_into_cycle < 1:
        return "new_moon.jpg"
    elif days_into_cycle < 7:
        return "waxing_crescent.jpg"
    elif days_into_cycle < 9:
        return "first_quarter.jpg"
    elif days_into_cycle < 14:
        return "waxing_gibbous.jpg"
    elif days_into_cycle < 15:
        return "full_moon.jpg"
    elif days_into_cycle < 22:
        return "waning_gibbous.jpg"
    elif days_into_cycle < 24:
        return "last_quarter.jpg"
    else:
        return "waning_crescent.jpg"

@app.route('/')
def index():
    today = datetime.now()
    days_into_cycle = calculate_moon_phase(today)
    moon_image = get_moon_image(days_into_cycle)

    return render_template('index.html', moon_image=moon_image)

if __name__ == '__main__':
    app.run()

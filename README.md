# Moon Phase 🌙

## Introduction

Moon Phase is a simple web app that shows the current phase of the moon. Upon visiting the site, one can see what today's moon looks like in the sky. We used **Flask** to create this web app, and the design was implemented using **HTML** and **CSS**. The app calculates the current moon phase and displays an image that corresponds to the moon's current cycle.

---

## Formula to Calculate Moon Phase

To calculate the moon phase, we use a specific formula based on the **Julian Date (JD)** and the lunar cycle. The formula helps determine how many days have passed in the current lunar cycle, which is then used to identify the moon's phase.

The formula for calculating the Julian Date (JD) is as follows:

\[
JD = C + D + E + F - 1524.5
\]

Where:

**\(C\)** is a correction factor based on the century, calculated as:

\[
C = 2 - A + B
\]

Here, **\(A\)** is the integer part of the year divided by 100, and **\(B\)** is the integer part of **\(A / 4\)**.

**\(E\)** represents the number of days in a year adjusted for leap years:

\[
E = \lfloor 365.25 \times (Y + 4716) \rfloor
\]

Where **\(Y\)** is the year for the calculation.

**\(F\)** is a factor based on the month of the year:

\[
F = \lfloor 30.6001 \times (M + 1) \rfloor
\]

Where **\(M\)** is the month (from 1 to 12).

After calculating the Julian Date, we determine the days into the current lunar cycle by subtracting a reference date (2451549.5) and dividing by the length of the lunar cycle (29.53 days). This value is then used to determine the current moon phase by mapping the number of days into the cycle to a specific phase:

We then calculate the days into cycle and map this to a specific moon phase.

---

## Moon Phases and Corresponding Images

Based on the number of days into the lunar cycle, the app maps the value to a moon phase:

| Days Into Cycle | Moon Phase        | Image File Name        |
|------------------|-------------------|------------------------|
| 0 – 1            | New Moon          | new_moon.jpg           |
| 1 – 7            | Waxing Crescent   | waxing_crescent.jpg    |
| 7 – 9            | First Quarter     | first_quarter.jpg      |
| 9 – 14           | Waxing Gibbous    | waxing_gibbous.jpg     |
| 14 – 15          | Full Moon         | full_moon.jpg          |
| 15 – 22          | Waning Gibbous    | waning_gibbous.jpg     |
| 22 – 24          | Last Quarter      | last_quarter.jpg       |
| 24 – 30          | Waning Crescent   | waning_crescent.jpg    |

### Links 
- Font used in this website is [Lora](https://fonts.google.com/specimen/Lora)
- [Image Credit: NASA Science](https://science.nasa.gov/moon/moon-phases/)


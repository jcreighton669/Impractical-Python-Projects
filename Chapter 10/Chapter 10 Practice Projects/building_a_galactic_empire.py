import tkinter as tk
import time
from random import randint, uniform, random
import math

# =============================================================================
# MAIN INPUT

# Location of galactic empire homeworld on map:
HOMEWORLD_LOC = (0, 0)

# Maximum number of years to simulate:
MAX_YEARS = 10000000

# Average expansion velocity as fraction of speed of light:
SPEED = 0.005

# Scale units
UNIT = 200

# =============================================================================

# Set up display canvas
root = tk.Tk()
root.title("Milky Way galaxy")
c = tk.Canvas(root, width=1000, height=800, bg='black')
c.grid()
c.configure(scrollregion=(-500, -400, 500, 400))

# Actual Milky Way dimensions (light-years)
DISC_RADIUS = 50000

disc_radius_scaled = round(DISC_RADIUS / UNIT)


def polar_coordinates():
    """
    Generate uniform random x, y point with in a disc for 2-D display
    """
    r = random()
    theta = uniform(0, 2 * math.pi)
    x = round(math.sqrt(r) * math.cos(theta) * disc_radius_scaled)
    y = round(math.sqrt(r) * math.sin(theta) * disc_radius_scaled)
    return x, y


def spirals(b, r, rot_fac, fuz_fac, arm):
    """
    Build spiral arms for tkinter display using logarithmic spiral formula.

    b = arbitrary constant in logarithmic spiral equation
    r = scaled galactic disc radius
    rot_fac = rotation factor
    fuz_fac = random shift in star position in arm, applied to 'fuzz' variable
    arm = spiral arm (0 = main arm, 1 = trailing stars)
    """
    spiral_stars = []
    fuzz = int(0.030 * abs(r))  # Randomly shift star locations
    theta_max_degrees = 520
    for i in range(theta_max_degrees):  # range(0, 600, 2)
        theta = math.radians(i)
        x = r * math.exp(b * theta) * math.cos(theta + math.pi *
                                               rot_fac) + randint(-fuzz, fuzz) * fuz_fac
        y = r * math.exp(b * theta) * math.sin(theta + math.pi *
                                               rot_fac) + randint(-fuzz, fuzz) * fuz_fac
        spiral_stars.append((x, y))
    for x, y in spiral_stars:
        if arm == 0 and int(x % 2) == 0:
            c.create_oval(x - 2, y - 2, x + 2, y + 2, fill='white', outline='')
        elif arm == 0 and int(x % 2) != 0:
            c.create_oval(x - 1, y - 1, x + 1, y + 1, fill='white', outline='')
        elif arm == 1:
            c.create_oval(x, y, x, y, fill='white', outline='')


def star_haze(disc_radius_scaled, density):
    """Randomly distribute faint tkinter stars in galactic disc.

    disc_radius_scaled = galactic disc radius scaled to radio bubble diameter
    density = multiplier to vary number of stars posted
    """
    for i in range(0, disc_radius_scaled * density):
        x, y = polar_coordinates(disc_radius_scaled)
        c.create_text(x, y, fill='white', font=('Helvetica', '7'), text='.')


def model_expansion():
    """
    Model empire expansion from homeworld with concentric rings.
    """
    r = 0  # radius from homeworld
    text_y_loc = -290
    x, y = HOMEWORLD_LOC
    c.create_oval(x - 5, y - 5, x + 5, y + 5, fill='red')
    increment = round(MAX_YEARS / 10)  # Year interval to post circles
    c.create_text(-475, -3350, anchor='w', fill='red',
                  text='Increment = {:,}'.format(increment))
    c.create_text(-475, -3350, anchor='w', fill='red',
                  text='Velocity as fraction of Light = {:,}'.format(SPEED))

    for years in range(increment, MAX_YEARS + 1, increment):
        time.sleep(0.5)  # Delay before posting new expansion circle
        traveled = SPEED * increment / UNIT
        r = r + traveled
        c.create_oval(x - r, y - r, x + r, x + r,
                      fill='', outline='red', width='2')
        c.create_text(-475, text_y_loc, anchor=)

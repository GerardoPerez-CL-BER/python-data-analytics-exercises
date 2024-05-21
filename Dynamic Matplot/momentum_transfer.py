import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Function to generate Gaussian data with noise
def generate_gaussian_data(Q, peak_position, std_dev, amplitude, noise_level=0):
    data = amplitude * np.exp(-((Q - peak_position)**2) / (2 * std_dev**2))
    noise = np.random.normal(0, noise_level, Q.size)
    return data + noise

# Parameters
Q = np.linspace(1.48, 1.54, 100)

# Generate data for Cu Kα1
Cu_Ka1 = generate_gaussian_data(Q, peak_position=1.51, std_dev=0.005, amplitude=50, noise_level=2)

# Generate data for Mo Kα1
Mo_Ka1 = generate_gaussian_data(Q, peak_position=1.51, std_dev=0.004, amplitude=80, noise_level=2)

# Generate data for Synchrotron high-resolution
Synchrotron = generate_gaussian_data(Q, peak_position=1.51, std_dev=0.003, amplitude=100)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(1.48, 1.54)
ax.set_ylim(0, max(Synchrotron) + 10)
ax.set_xlabel('Q / Å⁻¹')
ax.set_ylabel('Intensity / arb. units')

# Initialize lines
line1, = ax.plot([], [], label='Cu Kα1 (Bragg-Brentano)', color='blue')
line2, = ax.plot([], [], label='Mo Kα1 (Debye-Scherrer, 0.3 mm capillary)', color='orange')
line3, = ax.plot([], [], label='Synchrotron high-resolution (transmission)', color='red')

# Initialization function for animation
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return line1, line2, line3

# Update function for animation
def update(frame):
    line1.set_data(Q[:frame], Cu_Ka1[:frame])
    line2.set_data(Q[:frame], Mo_Ka1[:frame])
    line3.set_data(Q[:frame], Synchrotron[:frame])
    return line1, line2, line3

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(Q), init_func=init, blit=True, interval=50, repeat=False)

# Add legend
ax.legend()

# Show the plot
plt.show()

# Turbulence-Model
Note: The program must be run using the Turtle graphics library in Python. For more information about Turtle, visit the official [Turtle documentation](https://www.turtle.ox.ac.uk/). 

## Objective
This model simulates the behavior of particles within a container under varying levels of turbulence and media viscosity. The primary goal is to investigate how different fluid environments and turbulence levels affect particle dynamics.

## Key Concepts
The model explores:
- **Chaos Theory**: Examining the effects of non-linear dynamics on particle motion.
- **Turbulence**: Simulating random fluctuations in velocity to understand its impact on particle trajectories.
- **Viscosity**: Assessing how a fluid's resistance to flow influences particle movement.

## Initial Parameters and Setup
- **NUM_PARTICLES**: Total number of particles (default: 10).
- **PARTICLE_RADIUS**: Radius of each particle (default: 200 units).
- **MAXSPEED**: Maximum initial velocity for particles, unaffected by turbulence (default: 3 units).
- **CONTAINERWIDTH, CONTAINERHEIGHT**: Dimensions of the container (default: 5000x5000 units).
- **MEDIUM_VISCOSITY**: Adjustable parameter to simulate different fluid viscosities on a scale from 0 (no viscosity) to 100 (maximum viscosity).

## Viscosity Damping
Viscosity damping simulates fluid resistance by reducing particle velocity based on the medium's viscosity. The damping effect is calculated as:
- **damping_factor**: A multiplier that reduces velocity proportionally to the medium's viscosity.
- **MIN_DAMPING**: Baseline damping to ensure some resistance even in low-viscosity media.

The new velocity is computed by multiplying the initial velocity by the **damping_factor** and dividing by 100 for scale adjustment.

## Effect of Turbulence
Turbulence introduces chaotic, unpredictable changes in particle velocity:
- **TURBULENCESPEED**: Controls the maximum possible change in velocity due to turbulence.
- **TURBULENCE_IMPACT**: Scales the intensity of turbulence effects.

Turbulence is simulated by adjusting particle velocities randomly within a range determined by **TURBULENCESPEED**. The impact of turbulence can be increased or decreased using **TURBULENCE_IMPACT**.

## Observations
- **Air**: Low viscosity, fast particle movement, longer travel distances.
- **Water**: Medium viscosity, reduced speed and travel distance.
- **Oil**: High viscosity, slow particle movement, shorter travel distances.

## Effect of Zero Turbulence Speed (No Turbulence)
Setting **TURBULENCESPEED** to zero eliminates random fluctuations, providing a clear view of how viscosity alone affects particle movement.

## Simulating Isotropic and Anisotropic Turbulence
- **Isotropic Turbulence**: Uniform turbulence effects across X and Y axes, leading to homogenous dispersion.
- **Anisotropic Turbulence**: Directionally dependent turbulence effects by adjusting only one axis, resulting in uneven particle dispersion and movement patterns.

## How to Run the Simulation
1. Set the initial parameters as desired.
2. Adjust **MEDIUM_VISCOSITY** based on the fluid you wish to simulate.
3. Run the simulation and observe particle behavior under different conditions.
4. Experiment with **TURBULENCESPEED** and **TURBULENCE_IMPACT** to explore the effects of turbulence.
5. Modify the code to simulate isotropic or anisotropic turbulence as needed.

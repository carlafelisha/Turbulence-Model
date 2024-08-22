# Set up map dimensions and colors
width = 250
height = 250
beaver_color = rgb(5 % 10 + 1)
wolf_color = rgb(6 % 10 + 1)
elk_color = rgb(7 % 10 + 1)
grass_color = green
dark_grass_color = rgb(7 % 10 + 1)

# Set up initial population counts
num_beavers = 10
num_wolves = 5
num_elks = 20
num_dark_grass_patches = 10

# Create a two-dimensional map
ecosystem_map = []
for x in range(width):
    row = []
    for y in range(height):
        row.append(grass_color)
    ecosystem_map.append(row)

# Populate the map with initial entities
for _ in range(num_beavers):
    x = randrange(width)
    y = randrange(height)
    ecosystem_map[x][y] = beaver_color

for _ in range(num_wolves):
    x = randrange(width)
    y = randrange(height)
    ecosystem_map[x][y] = wolf_color

for _ in range(num_elks):
    x = randrange(width)
    y = randrange(height)
    ecosystem_map[x][y] = elk_color

for _ in range(num_dark_grass_patches):
    x = randrange(width)
    y = randrange(height)
    ecosystem_map[x][y] = dark_grass_color

# Simulate the ecosystem
canvas(0, 0, width, height)
resolution(width, height)
noupdate()

while True:
    # Move and reproduce entities
    new_map = []
    cell_color: list[int] = []
    for x in range(width):
        row = []
        for y in range(height):
            cell_color[x][y] = ecosystem_map[x][y]

            # Wolves eat elks
            if cell_color == wolf_color:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (
                            0 <= x + i < width
                            and 0 <= y + j < height
                            and ecosystem_map[x + i][y + j] == elk_color
                        ):
                            num_elks -= 1
                            row.append(wolf_color)
                            break
                    else:
                        continue
                    break
                else:
                    row.append(wolf_color)

            # Elks eat dark grass patches
            elif cell_color == elk_color:
                row.append(elk_color)
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (
                            0 <= x + i < width
                            and 0 <= y + j < height
                            and ecosystem_map[x + i][y + j] == dark_grass_color
                        ):
                            num_dark_grass_patches -= 1
                            break

            # Beavers reproduce in dark grass patches
            elif cell_color == beaver_color:
                if ecosystem_map[x][y] == dark_grass_color:
                    num_beavers += 1
                    new_x = randrange(width)
                    new_y = randrange(height)
                    ecosystem_map[new_x][new_y] = beaver_color
                row.append(beaver_color)

            # Dark grass patches respawn
            elif cell_color == dark_grass_color:
                if randrange(100) < 10:  # 10% chance of respawning
                    num_dark_grass_patches += 1
                row.append(dark_grass_color)

            else:
                row.append(grass_color)

        new_map.append(row)

    # Update the map
    ecosystem_map = new_map

    # Draw the updated map
    for x in range(width):
        for y in range(height):
            colour(ecosystem_map[x][y])
            box(1, 1, ecosystem_map[x][y], True)

    # Display population counts
    colour(black)
    setxy(10, height - 20)
    display("Beavers: " + str(num_beavers), 2, 10)
    setxy(10, height - 30)
    display("Wolves: " + str(num_wolves), 2, 10)
    setxy(10, height - 40)
    display("Elks: " + str(num_elks), 2, 10)
    setxy(10, height - 50)
    display("Dark Grass: " + str(num_dark_grass_patches), 2, 10)

    update()
    pause(250)
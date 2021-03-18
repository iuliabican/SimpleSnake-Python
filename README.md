# Python! - Faculty Given Requirement
Implement a console-based version of the beloved [game of Snake](https://www.google.com/search?q=play+snake) using Python 3 and object-driven layered architecture. User input must be validated. The program must work in the following way:
1. At program start, display the game area.
   - The game area is a `DIM x DIM` matrix of squares that contains the snake and a number of `apple_count` apples. The snake always starts with a head segment (`*`) and two body segments (`+`) and is placed in the middle of the board. Each apple is represented using a dot (`.`). Apples are placed randomly, so that two apples cannot be adjacent on the row or column, and cannot overlap the snake's starting position **[1.5p]**.
   - The values of `DIM` (odd natural number) and `apple_count` (natural number) are read from a settings file and are presumed correct **[0.5p]**.
```
+---+---+---+---+---+---+---+
|   | . |   |   |   | . |   |
+---+---+---+---+---+---+---+
|   |   |   | . |   |   |   |
+---+---+---+---+---+---+---+
| . |   | . | * |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   | + |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   | + |   |   | . |
+---+---+---+---+---+---+---+
| . |   |   | . |   | . |   |
+---+---+---+---+---+---+---+
|   | . |   |   |   |   |   |
+---+---+---+---+---+---+---+
Example starting position, DIM=7, apple_count=10. The snake is pointing up
```

2. Play the game. The user can move the snake using the following commands:
    - `move [n]`. This moves the snake `n` squares, in the direction it is currently facing. `move` with no parameters moves the snake by `1` square **[1p]**.
    - `up | right | down | left` changes the snake's direction accordingly. Trying to change the snake's direction by 180 degrees will result in an error message (a snake going up cannot immediately go down). Entering the direction the snake is currently heading for does nothing **[2p]**.
    - When the snake eats an apple, its tail grows by `1 square`. A new apple is immediately added to the game area, following the rules at `Point 1` **[1.5p]**.

3. Game Over. The game ends when the snake hits the edge of the game area, or one of its own segments **[1.5p]**.

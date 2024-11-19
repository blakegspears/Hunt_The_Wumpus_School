How to Play "Hunt the Wumpus"
Objective:
Your goal is to navigate through a cave system, avoid hazards, and kill the Wumpus using a single arrow before the Wumpus kills you or you fall into a pit.

Game Setup

The cave consists of 20 interconnected rooms arranged in a circular pattern.
Each room has three exits leading to other rooms:
Two adjacent rooms (numerically consecutive, e.g., room 5 connects to rooms 4 and 6).
One random room (non-adjacent, adds unpredictability).
The game includes hazards and threats:
The Wumpus: A deadly monster.
If you enter its room, it kills you instantly.
If you shoot the Wumpus with your arrow, you win!
Bottomless Pits: If you fall into a pit, you lose the game.
Super Bats: These creatures will pick you up and drop you into a random room, which might be hazardous.

Game Mechanics

Start Location:
You begin in a random room with no hazards.
You'll see a description of your current room and its connections.
Sensory Clues:

If hazards are nearby, you'll receive clues:
"You feel a breeze." → A pit is in an adjacent room.
"You hear flapping wings." → Bats are in an adjacent room.
"You smell something terrible." → The Wumpus is in an adjacent room.
Actions:

On each turn, you can choose one of two actions:
Move to an adjacent room:
Type M and select a connected room number.
Shoot your arrow:
Type S and select the room number where you want to shoot.
If you shoot the Wumpus, you win. If you miss, the Wumpus might move to a new room.
Winning the Game:

Successfully shoot the Wumpus with your single arrow.

Losing the Game:
Enter the Wumpus' room.
Fall into a pit.
Run out of arrows without killing the Wumpus.

```mermaid
flowchart TD
    start([Start Game]) --> decide{Move or Shoot?}
    decide --> move[Move to a room]
    decide --> shoot[Shoot into a room]
    
    move --> hazard{Hazard Encountered?}
    hazard --> pit[Fall into a Pit<br>Game Over]
    hazard --> bats[Bats Pick You Up<br>Move to Random Room]
    hazard --> wumpus[Enter Wumpus' Room<br>Game Over]
    hazard --> safe[Room is Safe<br>Continue Exploring]

    shoot --> hit[You Hit the Wumpus<br>Game Won!]
    shoot --> miss[Missed the Wumpus<br>Wumpus Moves]
    miss --> hazard

    safe --> decide
    miss --> decide

    pit --> game_over[Game Over]
    wumpus --> game_over
    bats --> decide
    hit --> victory[You Win!]

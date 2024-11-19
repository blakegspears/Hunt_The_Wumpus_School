
import random

class HuntTheWumpus:
    def __init__(self):
        self.rooms = {i: [] for i in range(1, 21)}  # 20 rooms
        self.wumpus = random.randint(1, 20)
        self.pits = random.sample([i for i in range(1, 21) if i != self.wumpus], 2)
        self.bats = random.sample([i for i in range(1, 21) if i not in self.pits and i != self.wumpus], 2)
        self.player = random.choice([i for i in range(1, 21) if i not in self.pits and i not in self.bats and i != self.wumpus])
        self.arrow = 1  # Player starts with one arrow
        self.create_cave()

    def create_cave(self):
        for room in self.rooms:
            connections = []

            # Add adjacent rooms
            previous_room = room - 1 if room > 1 else len(self.rooms)  # Wrap around for the first room
            next_room = room + 1 if room < len(self.rooms) else 1      # Wrap around for the last room

            connections.append(previous_room)
            connections.append(next_room)

            # Add a third random room, ensuring it's not already connected
            third_room = random.choice([i for i in self.rooms if i != room and i not in connections])
            connections.append(third_room)

            # Assign the connections to the room
            self.rooms[room] = connections

    def print_status(self):
        print(f"You are in room {self.player}")
        print(f"Connected rooms: {self.rooms[self.player]}")
        if any(adj in self.pits for adj in self.rooms[self.player]):
            print("You feel a breeze.")
        if any(adj in self.bats for adj in self.rooms[self.player]):
            print("You hear flapping wings.")
        if any(adj == self.wumpus for adj in self.rooms[self.player]):
            print("You smell something terrible.")

    def move(self, room):
        if room not in self.rooms[self.player]:
            print("You can't move there!")
            return False
        self.player = room
        self.check_hazards()
        return True

    def shoot(self, room):
        if self.arrow == 0:
            print("You have no arrows left!")
            return False
        self.arrow -= 1
        if room == self.wumpus:
            print("You killed the Wumpus! You win!")
            return True
        else:
            print("You missed! The Wumpus may move...")
            if random.random() < 0.5:
                self.wumpus = random.choice(self.rooms[self.wumpus])
            return False

    def check_hazards(self):
        if self.player == self.wumpus:
            print("You entered the Wumpus' room! Game Over!")
            exit()
        elif self.player in self.pits:
            print("You fell into a pit! Game Over!")
            exit()
        elif self.player in self.bats:
            print("A bat picked you up and dropped you in another room!")
            self.player = random.choice([i for i in range(1, 21) if i != self.player])

    def play(self):
        print("Welcome to Hunt the Wumpus!")
        print("Press 'E' at any time to end the game.")
        while True:
            self.print_status()
            action = input("Do you want to (M)ove or (S)hoot? ").strip().upper()
            if action == "E":
                print("You have ended the game. Thank you for playing!")
                break
            elif action == "M":
                try:
                    room = int(input("Enter the room number to move to: "))
                    self.move(room)
                except ValueError:
                    print("Invalid room number!")
            elif action == "S":
                try:
                    room = int(input("Enter the room number to shoot into: "))
                    if self.shoot(room):
                        break
                except ValueError:
                    print("Invalid room number!")
            else:
                print("Invalid action!")

if __name__ == "__main__":
    game = HuntTheWumpus()
    game.play()
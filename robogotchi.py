import random
import sys

interaction_is_valid = False
interaction_chosen = ""
game_isValid = False
input_isValid = False
isExit = False
user_won = 0
robot_won = 0
draws = 0
game = ""
user_input = ""
robot_input = 0
goal = 0
robot_input = ""


class Robot:

    def __init__(self, name=input("How will you call your robot?"), battery_level=100, overheat_level=0, skill_level=0,
                 boredom_level=0, rust_level=0):
        self.name = name
        self.battery_level = battery_level
        self.overheat_level = overheat_level
        self.skill_level = skill_level
        self.boredom_level = boredom_level
        self.rust_level = rust_level

    def interact(self):
        global interaction_chosen, interaction_is_valid
        match interaction_chosen:
            case "exit":
                print("Game over.")
                sys.exit()
            case "info":
                self.display_info()
                interaction_is_valid = False
            case "work":
                self.work()
                interaction_is_valid = False
            case "oil":
                self.oil()
                interaction_is_valid = False
            case "learn":
                self.learn()
                interaction_is_valid = False
            case "recharge":
                self.recharge()
                interaction_is_valid = False
            case "sleep":
                self.sleep()
                interaction_is_valid = False
            case "play":
                self.play()
                interaction_is_valid = False
            case _:
                print("Invalid input, try again!")

    def display_info(self):
        status = f"{self.name}'s stats are:\n" \
                 f"the battery is {self.battery_level},\n" \
                 f"overheat is {self.overheat_level},\n" \
                 f"skill level is {self.skill_level},\n" \
                 f"boredom is {self.boredom_level}, \n" \
                 f"rust is {self.rust_level}."
        print(status)

    def recharge(self):
        previous_overheat_level = self.overheat_level
        previous_battery_level = self.battery_level
        previous_boredom_level = self.boredom_level
        if self.battery_level == 100:
            print(f"{self.name} is charged!")
        else:
            self.battery_level += 10
        if self.overheat_level >= 5:
            self.overheat_level -= 5
        else:
            self.overheat_level = 0
        self.boredom_level += 5
        status = f"{self.name}'s level of overheat was {previous_overheat_level}. Now it is {self.overheat_level}.\n" \
                 f"{self.name}'s level of the battery was {previous_battery_level}. Now it is {self.battery_level}.\n" \
                 f"{self.name}'s level of boredom was {previous_boredom_level}. Now it is {self.boredom_level}." \
                 f"{self.name} is recharged!"
        print(status)

    def sleep(self):
        previous_overheat_level = self.overheat_level
        if self.overheat_level == 0:
            print(f"{self.name} is cool!")
        else:
            if self.overheat_level > 20:
                self.overheat_level -= 20
                status = f"{self.name} cooled off!\n" \
                         f"{self.name}'s level of overheat was {previous_overheat_level}. Now it is {self.overheat_level}."
                print(status)
            else:
                self.overheat_level = 0
                print(
                    f"{self.name}'s level of overheat was {previous_overheat_level}. Now it is {self.overheat_level}.")
                print(f"{self.name} is cool!")

    def play(self):
        global game_isValid, game, isExit, input_isValid, user_won, robot_won, draws
        previous_boredom_level = self.boredom_level
        previous_overheat_level = self.overheat_level
        game_isValid = False
        while not game_isValid:
            check_game_input()
        input_isValid = False
        isExit = False
        user_won = 0
        robot_won = 0
        draws = 0
        while not isExit and not input_isValid:
            initialize_game()
            check_user_input()
            while not isExit and input_isValid:
                if self.boredom_level >= 20:
                    self.boredom_level -= 20
                else:
                    self.boredom_level = 0
                if game == "numbers":
                    play_numbers()
                    determine_result()
                elif game == "rock-paper-scissors":
                    play_RPS()
                    determine_result()
                input_isValid = False

        print_result()
        self.overheat_level += 10

        status = f"{self.name}'s level of boredom was {previous_boredom_level}. Now it is {self.boredom_level}.\n" \
                 f"{self.name}'s level of overheat was {previous_overheat_level}. Now it is {self.overheat_level}."
        print(status)

        if self.battery_level < 10:
            self.fallIntoPool()
        if 10 < self.battery_level < 30:
            self.stepIntoPuddle()

        if self.boredom_level == 0:
            print(f"{self.name} is in a great mood!")
        if self.overheat_level >= 100:
            print(f"The level of overheat reached 100, "
                  f"{self.name} has blown up! Game over. Try again?")
            sys.exit()

    def work(self):
        if self.skill_level < 50:
            print(f"{self.name} has got to learn before working!")
        else:
            previous_battery_level = self.battery_level
            previous_boredom_level = self.boredom_level
            previous_overheat_level = self.overheat_level
            previous_rust_level = self.rust_level
            if self.battery_level <= 10:
                self.battery_level = 0
            else:
                self.battery_level -= 10
            self.boredom_level += 10
            self.overheat_level += 10

            print(f"{self.name} did well!")
            print(f"{self.name}'s level of boredom was {previous_boredom_level}. Now it is {self.boredom_level}.")
            print(f"{self.name}'s level of overheat was {previous_overheat_level}. Now it is {self.overheat_level}.")
            print(f"{self.name}'s level of the battery was {previous_battery_level}. Now it is {self.battery_level}.")

            if self.battery_level < 10:
                self.fallIntoPool()
            if 10 < self.battery_level < 30:
                self.stepIntoPuddle()


    def stepIntoPuddle(self):
        previous_rust_level = self.rust_level
        self.rust_level += 10
        print(f"Oh no, {self.name} stepped into a puddle!")
        print(f"{self.name}'s level of rust was {previous_rust_level}. Now it is {self.rust_level}.")

    def fallIntoPool(self):
        previous_rust_level = self.rust_level
        self.rust_level += 50
        print(f"Guess what! {self.name} fell into the pool!")
        print(f"{self.name}'s level of rust was {previous_rust_level}. Now it is {self.rust_level}.")

    def oil(self):
        if self.rust_level == 0:
            print(f"{self.name} is fine, no need to oil!")
        else:
            previous_rust_level = self.rust_level
            self.rust_level -= 20
            print(f"{self.name}'s level of rust was {previous_rust_level}. "
                  f"Now it is {self.rust_level}. {self.name} is less rusty!")

    def learn(self):
        if self.skill_level >= 100:
            print(f"There's nothing for {self.name} to learn!")
        else:
            previous_skill_level = self.skill_level
            previous_overheat_level = self.overheat_level
            previous_battery_level = self.battery_level
            previous_boredom_level = self.boredom_level
            self.skill_level += 10
            if self.battery_level <= 10:
                self.battery_level = 0
            else:
                self.battery_level -= 10
            self.overheat_level += 10
            self.boredom_level += 5

            status = f"{self.name}'s level of skill was {previous_skill_level}. Now it is {self.skill_level}.\n" \
                     f"{self.name}'s level of overheat was {previous_overheat_level}. Now it is {self.overheat_level}.\n" \
                     f"{self.name}'s level of the battery was {previous_battery_level}. Now it is {self.battery_level}.\n" \
                     f"{self.name}'s level of boredom was {previous_boredom_level}. Now it is {self.boredom_level}.\n" \
                     f"{self.name} has become smarter!"

            print(status)

        if self.battery_level < 10:
            self.fallIntoPool()
        if 10 <= self.battery_level < 30:
            self.stepIntoPuddle()


def check_game_input():
    global game_isValid, game
    game = input("Which game would you like to play?").lower()
    if game != "numbers" and game != "rock-paper-scissors":
        print("Please choose a valid option: Numbers or Rock-paper-scissors?")
        game_isValid = False
    else:
        game_isValid = True


def initialize_game():
    global game, user_input
    if game == "numbers":
        print("What is your number?")
    elif game == "rock-paper-scissors":
        print("What is your move?")
    user_input = input()


def display_available_interactions(robot):
    global interaction_chosen
    interaction_menu = f"""Available interactions with {robot.name}:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills"""

    print(interaction_menu)
    interaction_chosen = input("Choose:")


def check_interaction_valid(robot):
    global interaction_chosen, interaction_is_valid
    interaction_is_valid = False
    valid_interactions = ["exit", "info", "work", "play", "oil", "recharge", "sleep", "learn"]
    if interaction_chosen in valid_interactions:
        if robot.rust_level >= 100:
            print(f"{robot.name} is too rusty! Game over. Try again?")
            sys.exit()
        if interaction_chosen == "work":
            if robot.battery_level == 0:
                print(f"The level of the battery is 0, {robot.name} needs recharging!")
            elif robot.boredom_level >= 100:
                print(f"{robot.name} is too bored! {robot.name} needs to have fun!")
            else:
                interaction_is_valid = True
        else:
            interaction_is_valid = True


def check_user_input():
    global user_input, isExit, input_isValid, game
    # print("user_number:", user_number)
    if user_input == "exit game":
        input_isValid = True
        isExit = True
    else:
        if game == "numbers":
            try:
                user_input = int(user_input)
                if user_input < 0:
                    print("The number can't be negative!")
                elif user_input > 1000000:
                    print("Invalid input! The number can't be bigger than 1000000")
                else:
                    input_isValid = True
            except ValueError:
                print("A string is not a valid input!")
        elif game == "rock-paper-scissors":
            user_input = user_input.lower()
            if user_input == "rock" or user_input == "paper" or user_input == "scissors":
                input_isValid = True
            else:
                print("No such option! Try again!")
                input_isValid = False


def play_numbers():
    global robot_input
    global goal
    robot_input = random.randint(0, 1000000)
    goal = random.randint(0, 1000000)
    print(f"The robot entered the number {robot_input}.")
    print(f"The goal number is {goal}.")


def play_RPS():
    global user_input
    global robot_input
    move_list = ["rock", "paper", "scissors"]
    robot_input = random.choice(move_list)
    print(f"The robot chose {robot_input}")


def determine_result():
    global user_input, robot_input, goal, user_won, robot_won, draws, game

    if game == "numbers":
        if abs(goal - user_input) < abs(goal - robot_input):
            user_won += 1
            print("You won!")
        elif abs(goal - user_input) > abs(goal - robot_input):
            robot_won += 1
            print("The robot won!")
        else:
            draws += 1
            print("It's a draw!")
    elif game == "rock-paper-scissors":
        user_input = user_input.lower()
        robot_input = robot_input.lower()
        # print("user: ", user_input, "robot:", robot_input, "same:", user_input == robot_input)
        if user_input == robot_input:
            draws += 1
            print("It's a draw!")
        elif (user_input == "paper" and robot_input == "rock") \
                or (user_input == "rock" and robot_input == "scissors") \
                or (user_input == "scissors" and robot_input == "paper"):
            user_won += 1
            print("You won!")
        else:
            robot_won += 1
            print("The robot won!")


def print_result():
    global user_won, robot_won, draws
    print(f"You won: {user_won},")
    print(f"Robot won: {robot_won},")
    print(f"Draws: {draws}.")


def main():
    global interaction_chosen
    robot = Robot()
    while True:
        if robot.rust_level >= 100 or robot.overheat_level >= 100:
            if robot.rust_level >= 100:
                print(f"{robot.name} is too rusty! Game over. Try again?")
            if robot.overheat_level >= 100:
                print(f"The level of overheat reached 100, "
                      f"{robot.name} has blown up! Game over. Try again?")
            sys.exit()
        else:
            while interaction_is_valid is False:
                display_available_interactions(robot)
                check_interaction_valid(robot)
            robot.interact()


if __name__ == "__main__":
    main()

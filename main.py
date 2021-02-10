import random
from collections import Counter

class Dice:

    def __init__(self, dice_sides=6, target_roll_count=1):
        self.dice_sides = dice_sides
        self.target_roll_count = target_roll_count

    def generate_possible_rolls(self):
        dice_rolls = []
        for number in range(2, ((self.dice_sides * 2) + 1), 1):
            # append each number value to function input empty list
            dice_rolls.append(number)

        return dice_rolls

    def random_dice_game(self):

        def roll_dice (dice):

            """Function that replicates the random roll of a dice"""

            # assign a randomly generated number that occurs between 1 and a globally specified
            # variable that equates to the amount of sides the user wants the normal dice to have
            dice = random.randint(1, self.dice_sides)
            return dice

        def add_dice (first, second):

            """Function that calculates the sum of two function inputs that relate to the random roll
            of a dice"""

            total = first + second
            return total

        random_dice1 = 0
        random_dice2 = 0
        random_dice_rolled = 0

        if random_dice_rolled == 0:
            random_dice1 = roll_dice(random_dice1)
            random_dice2 = roll_dice(random_dice2)
            random_dice_rolled = add_dice(random_dice1, random_dice2)
        return random_dice_rolled

    def generate_random_rolls(self):

        random_rolls = []
        while len(random_rolls) != self.target_roll_count:
            random_rolls.append(self.random_dice_game())

        return random_rolls

    def generate_expected_rolls(self):

        def evaluateSides (dice_list):

            count = 0
            while count < self.dice_sides:
                for n in range(1, (self.dice_sides + 1), 1):
                    if count < self.dice_sides:
                        count += 1
                        dice_list.append(n)
            return dice_list

        def max_calculation (instance_one, instance_two):

            max_int = max(instance_one) * max(instance_two)

            return max_int

        dice_one = []
        dice_two = []

        expected_outcomes = []

        dice_one = evaluateSides(dice_one)
        dice_two = evaluateSides(dice_two)

        max_possible_outcomes = max_calculation(dice_one, dice_two)

        while len(expected_outcomes) != max_possible_outcomes:
            for n in range(len(dice_one)):
                for m in range(len(dice_two)):
                    expected_outcomes.append(dice_two[n] + dice_two[m])

        return expected_outcomes

class Frequency:

    def __init__ (self, instances=None, target_roll_count=1):
        self.target_roll_count = target_roll_count
        self.instances = instances

    def calculate_frequency (self):

        def generate_percentage (instances):

            for n in range(len(instances)):
                instances[n] = "{:.2f}".format(((instances[n]) / self.target_roll_count * 100))

            return instances

        def organise_frequency(list):

            return dict(Counter(list))

        def make_dict_list (dict):

            values = dict.values()

            frequency = list(values)

            return frequency

        def convert_list_int (list):

            for n in range(len(list)):
                list[n] = int(list[n])
            return list

        def convert_list_str (list):

            for n in range(len(list)):
                list[n] = str(list[n])
            return list

        instances = convert_list_str(sorted(self.instances))

        instances = organise_frequency(instances)

        instances = make_dict_list(instances)

        instances = convert_list_int(instances)

        instances = generate_percentage(instances)

        return instances

def main ():

    def segmentList (list, segment_size):

        """Function that segments the function input list into defined batch sizes to fit the parameters
        of the tabular column lable elements"""

        # for each string of the length of the list, in the defined size of segments
        for s in range(0, len(list), segment_size):
            # yield new segement lists in their defined segment batch size containing full lengthed
            # string items
            yield list[s:s + segment_size]

    def table_data (list1, list2, list3):

        table_headers = ["Total", "Simulated", "Expected", " ", "Percent", "Percent"]

        final_list = []

        for i in range(len(table_headers)):
            final_list.append(table_headers[i])

        for i in range(len(list1)):
            final_list.append(list1[i])
            final_list.append(list2[i])
            final_list.append(list3[i])

        return final_list

    def display_table (table):

        for t in range(len(table)):
            # first segment of table list == first 3 items of table_headers list
            if t == 0:
                print('{:>50s}{:>12s}{:>11s}'.format(table[t][0],table[t][1],table[t][2]))
            # second segment of table list == last 3 items of table_headers list
            elif t == 1:
                print('{:>50s}{:>12s}{:>11s}'.format(table[t][0],table[t][1],table[t][2]))
            # results of all dice rolling functions and (percentages)
            else:
                print('{:>50d}{:>12s}{:>11s}'.format(table[t][0],table[t][1],table[t][2]))

    table_values = []

    dice_sides = 6
    target_roll_count = 1000

    game = Dice(dice_sides, target_roll_count)
    random_game_rolls = game.generate_random_rolls()
    expected_game_rolls = game.generate_expected_rolls()
    random_game_frequency = Frequency(random_game_rolls, target_roll_count)
    expected_game_frequency = Frequency(expected_game_rolls, len(expected_game_rolls))

    table_values = table_data(
                            game.generate_possible_rolls(),
                            random_game_frequency.calculate_frequency(),
                            expected_game_frequency.calculate_frequency()
                            )

    table = list(segmentList(table_values, 3))

    display_table(table)

main()
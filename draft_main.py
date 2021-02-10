# import module
import random

def generate_possible_rolls (data_set):
    
    """Function to generate all possible rolls that are the sum of two dice, uses the multiplication
    of one global variable in its list parameter limitation"""
    
    # beginning from two, at a single increment, to the sum of the two dice used of 'x' sides
    for number in range(2, ((dice_sides * 2) + 1), 1):    
        # append each number value to function input empty list
        data_set.append(number)
        
    # return newly appended list
    return data_set
 
    
def verify_rolls (rolls):
    
    """Function that verifies the results of the dice roll calculations, checking
    that they occur as real two dice rolling possibilities, that would be found 
    and compared to the global variable containing all real possibilities pertained
    to a user specified dice sides"""
    
    # verify each item of function input list
    for roll in rolls:
        # qualify each item against the list containing all real possibilities
        if roll not in possible_rolls:
            # raise error if roll sum of the two dice is not true of the total
            # possibilities of their 'x' defined sides
            raise ValueError ("Error roll, result does not exist for two dice rolls")
        
        # else pass
        else:
            pass
        
    # return verified list
    return rolls


def generatePercentage (frequency, base_parameter):
            
    """Function that generate a frequency percentage and includes one global variable that determines
    the proportionate of each frequency."""
    
    # for each item of the function input list that is the incedent of a particular result, turn
    # into a percentage of the total
    for n in range(len(frequency)):
        frequency[n] = "{:.2f}".format(((frequency[n]) / base_parameter * 100))
        
    return frequency


def segmentList (list, segment_size):
    
    """Function that segments the function input list into defined batch sizes to fit the parameters
    of the tabular column lable elements"""
    
    # for each string of the length of the list, in the defined size of segments
    for s in range(0, len(list), segment_size):
        # yield new segement lists in their defined segment batch size containing full lengthed
        # string items
        yield list[s:s + segment_size]


def calculateFrequency (instances):
    
    """Function that takes count and organises the occurence of a specific value in accumulated list
    that can efficiently be converted to a percentage."""
    
    def organiseFrequency (list):
        
        """Function that takes the items of a list and allocates each instance to a categoric key - 
        the keys of the dictionary have not been calibrated to a change if the user decided to alter
        the global variable (dice sides) and therefore the dictionary keys are limited to that of 2
        six sided dice, unlike what is found in other functions of the program"""
        
        # frequency dictionary that holds all possible values for the sums of two 6-sided dice rolls
        Frequency = {"2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0
                        , "9": 0, "10": 0, "11": 0, "12": 0}
        
        # take the items of the function input list and when an instance matches the dictionary key:
        # add 1 to its associating matching dictionary key
        for instance in list:
            Frequency[instance] += 1
            
        # return the dictionary
        return Frequency
    
    def makeDictList (dict):
        
        """Function that extracts the values of the dictionary keys, and then restructure that data
        into a list format"""
        
        # take value of dictionary function input
        values = dict.values()
        
        # organise extracted values to a list
        Frequency = list(values)
        
        # return list, that is asegmented dictionary data as an organised list
        return Frequency
    
    def convertListStr (list):
        
        """Function that converts the items of a list into strings"""
        
        # At each index of the entrie list range, convert the item to a string
        for n in range(len(list)):
            list[n] = str(list[n])
         
        # return converted list
        return list
    
    def convertListInteger (list):
        
        """Function that converts the items of a list into integers"""
        
        # At each index of the entrie list range, convert the item to a integer
        for n in range(len(list)):
            list[n] = int(list[n])
        
        # return converted list
        return list
    
    # call to function
    instances = convertListStr(instances)
    
    # call to function
    instance_dict = organiseFrequency(instances)    
    
    # call to function
    instance_list = makeDictList(instance_dict)
    
    # call to function
    instance_list = convertListInteger(instance_list)
       
    return instance_list


def expected_dice_game ():
    
    """Function that generates expected accumulative of dice roles in accordance to probability theory."""
    
    def evaluateSides (list):
        
        """Function that generates a list of numbers that occur on each side of a normal dice"""
        
        # initiate loop mechanisms while the count is less than the specified global variable that equates
        # to the amount of sides the dice have
        count = 0
        while count < dice_sides:
            # from a single increment that occurs within the range of a specified dice, take the index
            for n in range(1, (dice_sides + 1), 1):
                # verify the count is still within the parameters of the possible dice values
                if count < dice_sides:
                    count += 1
                    # append the index, equating to an incrementing side of the dice, to the empty
                    # function input list
                    list.append(n)
        
        # return the updates list
        return list
    
    def max_calculation (input_one, input_two):
        
        """Function that returns the product of the two maximum values that occur from 2 lists of
        possibilities, the product value equates to the maximum amount of possible congruencies
        between each value, or instance, of the function input list - in terms of a 2 six sided dice,
        this will amount to 36 possible outcomes"""
        
        int = max(input_one) * max(input_two)
        
        return int
    
    # create empty list that will contain dice values
    dice_one = []
    dice_two = []
    
    # create empty list that will contain all expected possible outcomes
    possible_outcomes = []
    
    # call to function
    dice_one = evaluateSides(dice_one)
    dice_two = evaluateSides(dice_two)
    
    # call to function
    max_possible_outcomes = max_calculation(dice_one, dice_two)
    
    # loop mechanisms whilst the list of generated possible outcomes are not equal to the
    # caluculated maximum amount of possible outcomes relevant to the specified dice sides
    while len(possible_outcomes) != max_possible_outcomes: 
        # generate accumulative sum from an expected roll of two dice from the index
        for n in range(len(dice_one)):
            for m in range(len(dice_two)):
                # append the possible outcome of the sum of two dice, which value are specified
                # in the list, as the index increments
                possible_outcomes.append(dice_one[n] + dice_two[m])
                # call to function
                possible_outcomes = verify_rolls(possible_outcomes)
    
    return possible_outcomes
    

def random_dice_game ():
    
    """Function that generates a random accumulative of two dice roles."""
    
    def roll_dice (dice):
        
        """Function that replicates the random roll of a dice"""
        
        # assign a randomly generated number that occurs between 1 and a globally specified
        # variable that equates to the amount of sides the user wants the normal dice to have
        dice = random.randint(1, dice_sides)
        return dice
    
    def add_dice (first, second):
        
        """Function that calculates the sum of two function inputs that relate to the random roll
        of a dice"""
        
        total = first + second
        return total
    
    # create value assignment variables
    random_dice1 = 0
    random_dice2 = 0
    random_dice_rolled = 0
    
    # initiate function mechanisms if the variable does not contain the result of the two dice
    if random_dice_rolled == 0:  
        random_dice1 = roll_dice(random_dice1)
        random_dice2 = roll_dice(random_dice2)
        random_dice_rolled = add_dice(random_dice1, random_dice2)
    
    # return the sum value of the two random dice rolls
    return random_dice_rolled

# the amount of sides that the dice used in the function will have
dice_sides = 6
# the amount of rolls that will be generated for the random dice game
target_roll_count = 1000

# strings for the headers of the table
table_headers = ["Total", "Simulated", "Expected", " ", "Percent", "Percent"]

# create empty list that will contain the distinct sums of the possible rolls
possible_rolls = []
# call to function
possible_rolls = generate_possible_rolls(possible_rolls)

# create empty dictionary that will contain accumulated count of expected value instances
expected_roll_frequency = {}
# call to main expected dice game function
expected_rolls = expected_dice_game()
# in weight it is equivalent to the target roll count variable, however specific to the expected dice game
maximum_expected_outcomes = len(expected_rolls)
# call to functrion
expected_roll_frequency = calculateFrequency(expected_rolls)
# call to function
expected_roll_frequency = generatePercentage(expected_roll_frequency, maximum_expected_outcomes)

# create empty dictionary that will contain accumulated count of random value instances
random_roll_frequency = {}
# create empty list that will contain the sums of the randomly rolled dice
random_rolls = []

# call to function that generates a accumultaive of two random rolled dice until the list that such
# results are appended to, is equal in length to the amount specified for target of roll counts required
while len(random_rolls) != target_roll_count:
    random_rolls.append(random_dice_game())
    # call to functioin
    random_rolls = verify_rolls(random_rolls)

# call to function
random_roll_frequency =calculateFrequency(random_rolls)
# call to function
random_roll_frequency = generatePercentage(random_roll_frequency, target_roll_count)

# create empty list that will contain the values to be converted into a table display
table_values = []

# for the length of the specified list, append its items to the meta table list at each proper increment
for i in range(len(table_headers)):
    table_values.append(table_headers[i])

# the values of the table are limited by the sum of the possible rolls of the two dice
# append at the index of the limiting possible roll list to the new meta table value list, in a 
# specific order that will match the delimiter table columns of the final table list
for i in range(len(possible_rolls)):
    table_values.append(possible_rolls[i])
    table_values.append(random_roll_frequency[i])
    table_values.append(expected_roll_frequency[i])

# call to function
table = list(segmentList(table_values, 3))    

# display items of table in a format
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
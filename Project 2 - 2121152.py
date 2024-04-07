#####################################################################################################################

''' Υπολογιστική Νοημοσύνη και Μηχανική Μάθηση - Εργασία 2
# Βιολέντης Αντώνιος - 2121152 - aviolentis@uth.gr - Πέμπτο (5ο) εξάμηνο. ΑΜ που τελειώνει σε 2 (πρώτο θέμα).

Κάθε πακέτο έχει τις τιμές number (αριθμός ID), price (τιμή), length, width, height και weight (μήκος, πλάτος, ύψος, 
βάρος). Υποθέτουμε ότι το πρόγραμμα ασχολείται με τις παραγγελίες που λαμβάνονται σε ένα συγκεκριμένο σημείο της χώρας
για την συγκεκριμένη εταιρία. Υποθέτουμε επίσης ότι για height/length/width παίρνουμε ως μονάδα μέτρησης τα μέτρα 
(λχ. 2.6 μέτρα) και για weight παίρνουμε κιλά (πχ. 200 κιλά). Επιπλέον, τα δεδομένα μπορούν να δίνονται από τον χρήστη, 
ή να παράγονται τυχαία με χρήση της βιβλιοθήκης random για μία πιο αποδοτική και γρήγορη επίδειξη του αλγορίθμου. 
Θεωρώ ως βέλτιστη λύση εκείνη που μπορεί να εισάγει τα περισσότερα δέματα στα φορτηγά. Για παράδειγμα, εάν υπάρξει ένα
δέμα που ζυγίζει 400 κιλά και μόνο ένα φορτηγό με μέγιστο όριο 400, το μοντέλο θα προτιμίσει να επιλέξει άλλα δέματα
για να εισαχθούν στο φορτηγό με σκοπό τον μέγιστο δυνατό αριθμό συνολικών δεμάτων. Το μοντέλο επίσης έχει φτιαχτεί έτσι
ώστε στην fitness function να επιβραβέβεται μία δεκτή λύση όπου χρησιμοποείται ο ελάχιστος δυνατός αριθμός φορτηγών
για την τοποθέτηση πακέτων. Δηλαδή, εάν έχουμε 3 φορτηγά X, Y, Z και 3 δέματα τα οποία χωράνε ακόμα και σε ένα μόνο 
φπορτηγό, τότε το μοντέλο θα επιστρέψει μία λύση της μορφής [X, X, X] και όχι [X, Y, X] ή κάτι αντίστοιχο.
Κάθε chromosome είναι της μορφής ενός πίνακα μεγέθους όσο και το μήκος του συνολικού αριθμού των ημερίσιων δεμάτων, και
το κάθε index του αναπαριστάται από κάθε δέμα. Θεωρούμε ότι ένα δέμα έχει τιμή -1 αν δεν εισαχθεί σε κανένα φορτηγό, ή
τιμή Χ όπου Χ ο αριθμός του φορτηγού όπου εισάχθηκε το δέμα. Για παράδειγμα, εάν έχουμε 3 δέματα και 2 διαθέσιμα 
φορτηγά, μία λύση μπορεί να είναι η [-1, 0, 1] που σημαίνει ότι το δέμα 0 δεν μπήκε σε κάποιο φορτηγό και ότι τα 
δέματα 1 και 2 μπήκαν στα φορτηγά 0 και 1 αντίστοιχα. Η αρίθμηση ξεκινάει από το 0. 
Η τελική πολυπλοκότητα του αλγορίθμου είναι η μεγαλύτερη πολυπλοκότητα O(αριθμός γενιών x αριθμός λύσεων x αριθμός 
δεμάτων χ αριθμός φορτηγών), που προκύπτει από τo fitness function.
Ένα παράδειγμα λύσεων που θα μπορούσε να έχει ο κώδικας για 2 trucks και 5 parcels είναι [0, 0, 0, 1, -1].'''

#####################################################################################################################

# LIBRARY

import numpy # Used for arrays and lists.
import random # Used to generate random data.
import copy # Used to create a duplicate truck object.

#####################################################################################################################

# OBJECTS

trucks = []
class Truck:
    def __init__ (self, maxWeight, height, length, width): # Truck object constructor function.
        self.maxWeight = maxWeight        
        self.height = height
        self.length = length
        self.width = width
        self.area = width*length
        
parcels = []
class Parcel:
    def __init__ (self, weight, height, length, width, ID, price): # Parcel object constructor function.
        self.weight = weight
        self.height = height
        self.length = length
        self.width = width
        self.ID = ID
        self.price = price
        self.area = width*length
        self.rotated = False
        
#####################################################################################################################

# FUNCTIONS

def initializeValues(selection):
    
    if selection == 1:
        dailyOrderAmount = int(input("Enter the daily amount of orders: "))
        truckAmount = int(input("Enter the daily amount of trucks: "))
        
    elif selection == 2:    
        dailyOrderAmount = random.randint(5, 20) 
        truckAmount = random.randint(1, 3) 
        
    return dailyOrderAmount, truckAmount

def truckValues(selection, i):
    
    if selection == 1:
        print (f'DATA FOR TRUCK NUMBER {i}')
        maxWeight = int(input("Enter the maximum weight of the truck: "))
        height = float(input("Enter the height of the truck: "))
        length = float(input("Enter the length of the truck: "))
        width = float(input("Enter the width of the truck: "))
            
    elif selection == 2:
        maxWeight = random.randint(400, 600)        
        height = round(random.uniform(2.0, 2.20), 2) 
        length = round(random.uniform(3.0, 4.0), 2)
        width = round(random.uniform(2.0, 2.20), 2)
    
    return maxWeight, height, length, width

def parcelValues(selection, i):
    
    if selection == 1:
        print (f'DATA FOR PARCEL NUMBER {i}')
        weight = int(input("Enter the weight of the parcel: "))
        height = float(input("Enter the height of the parcel: "))
        length = float(input("Enter the length of the parcel: "))
        width = float(input("Enter the width of the parcel: "))
        price = float(input("Enter the price of the parcel: "))
        
    elif selection == 2:
        weight = round(random.uniform(0.10, 45), 2)
        height = round(random.uniform(0.05, 1), 2)
        length = round(random.uniform(0.10, 1), 2)
        width = round(random.uniform(0.10, 1), 2)
        price = round(random.uniform(7.00, 40), 2)
    
    return weight, height, length, width, price

def lines():
    print ("\n---------------------\n")
    
# 二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二　#
    
def initializePopulation(parcels, trucks):
    population_solutions = 14 # Number of solutions for each population.
    population_size = (population_solutions, len(parcels)) # Returns dimensions (10, amount of parcels).
    generation_amount = 800 # Amount of generations.
    
    # Creating the first set of (probably invalid) solutions.
    solutions = numpy.random.randint(-1, len(trucks), size=population_size)
            
    print (f'Initial solutions:\n{solutions}')

    return population_solutions, population_size, solutions, generation_amount

# 二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二　#

def truckValidity(parcels, trucks, solutions):
    updated_trucks = copy.deepcopy(trucks)
    
    # 3D array used to store tuples for each piece that was cut in a truck.
    # When a truck is cut, we take a right part and an upper part. Each tuple has an index of 0 until 3 (4 spots).
    # In indexes 0 and 1 we are referencing to the respective width and length of the right part, and in indexes
    # 2 and 3 we are referencing to the respecting width and length of the upper part.
    subtruck = [[] for i in range(len(trucks))]
    after_one = numpy.full(len(trucks), False, dtype = bool)

    # Iterating through every solution to check if it is valid. If an invalid solution is found, then the function returns False.
    for j in range(len(parcels)):

        # Examining if the parcel ended up getting in a truck. If not, the loop continues.
        if (solutions[j] != -1 ):
            
            # Examining if the weight is valid.
            if (parcels[j].weight <= updated_trucks[solutions[j]].maxWeight):
                
                # Checking if this is the first item added to truck solutions[j].
                if (after_one[solutions[j]] == False):
                    
                    # If it doesn't fit, we will try to rotate it and examine if that solution is valid.
                    if ((parcels[j].length > updated_trucks[solutions[j]].length)
                        or (parcels[j].width > updated_trucks[solutions[j]].width)):
                        
                        # Examining the same if statement with intverted width and length values.
                        if ((parcels[j].length <= updated_trucks[solutions[j]].width) 
                            and (parcels[j].width <= updated_trucks[solutions[j]].length)):
                            
                            # Adding tupples in the 3D array to make up for the space that we cut.
                            right_width = updated_trucks[solutions[j]].width - parcels[j].length
                            right_length = parcels[j].width
                            upper_width = updated_trucks[solutions[j]].width
                            upper_length = updated_trucks[solutions[j]].length - parcels[j].width
                            
                            # Updating the variables accordingly.
                            updated_trucks[solutions[j]].maxWeight -= parcels[j].weight
                            subtruck[solutions[j]].append([right_width, right_length, upper_width, upper_length])
                            parcels[j].rotated = True
                            after_one[solutions[j]] = True
                            
                            continue # Rotated to fit; continuing.
                            
                        else: 
                            return False # First package did not fit; leaving.

                    else: # It fits without needing a rotation! (still first parcel in the truck)
                                                                        
                        # Creating a tuple for our solution (truck).
                        right_width = updated_trucks[solutions[j]].width - parcels[j].width
                        right_length = parcels[j].length
                        upper_width = updated_trucks[solutions[j]].width
                        upper_length = updated_trucks[solutions[j]].length - parcels[j].length
                        
                        # Again, updating the variables accordingly.
                        updated_trucks[solutions[j]].maxWeight -= parcels[j].weight
                        subtruck[solutions[j]].append([right_width, right_length, upper_width, upper_length])
                        after_one[solutions[j]] = True
                        
                        continue # Length and width are valid; continuing.
                        
                else: # More than one item in truck solutions[j]. This means that after_one[solutions[j]] == True.
                    
                    yun = False # Flag to check if there was a new subtruck that needs to be created.
                    for w in range(len(subtruck[solutions[j]])): # Iterating through the amount of tuples caused by cut trucks.

                        if (parcels[j].width <= subtruck[solutions[j]][w][0] and parcels[j].length <= subtruck[solutions[j]][w][1]): 
                            right_width = subtruck[solutions[j]][w][0] - parcels[j].width
                            right_length = parcels[j].length
                            upper_width = subtruck[solutions[j]][w][0]
                            upper_length = subtruck[solutions[j]][w][1] - parcels[j].length
                            
                            subtruck[solutions[j]][w][0] = -1
                            subtruck[solutions[j]][w][1] = -1
                            
                            yun = True
                            break
                            
                        # Rotation check.
                        elif (parcels[j].length <= subtruck[solutions[j]][w][0] and parcels[j].width <= subtruck[solutions[j]][w][1]):                                    
                            right_width = subtruck[solutions[j]][w][0] - parcels[j].length
                            right_length = parcels[j].width
                            upper_width = subtruck[solutions[j]][w][0]
                            upper_length = subtruck[solutions[j]][w][1] - parcels[j].width
                            
                            subtruck[solutions[j]][w][0] = -1
                            subtruck[solutions[j]][w][1] = -1
                            parcels[j].rotated = True
                            
                            yun = True
                            break

                        elif (parcels[j].width <= subtruck[solutions[j]][w][2] and parcels[j].length <= subtruck[solutions[j]][w][3]):
                            right_width = subtruck[solutions[j]][w][2] - parcels[j].width
                            right_length = parcels[j].length
                            upper_width = subtruck[solutions[j]][w][2]
                            upper_length = subtruck[solutions[j]][w][3] - parcels[j].length
                            
                            subtruck[solutions[j]][w][2] = -1
                            subtruck[solutions[j]][w][3] = -1
                            
                            yun = True
                            break
                        
                        # Rotation check.
                        elif (parcels[j].length <= subtruck[solutions[j]][w][2] and parcels[j].width <= subtruck[solutions[j]][w][3]):
                            right_width = subtruck[solutions[j]][w][2] - parcels[j].length
                            right_length = parcels[j].width
                            upper_width = subtruck[solutions[j]][w][2]
                            upper_length = subtruck[solutions[j]][w][3] - parcels[j].width

                            subtruck[solutions[j]][w][2] = -1
                            subtruck[solutions[j]][w][3] = -1
                            parcels[j].rotated = True
                            
                            yun = True             
                            break
          
                    if (yun == True):
                        updated_trucks[solutions[j]].maxWeight -= parcels[j].weight
                        subtruck[solutions[j]].append([right_width, right_length, upper_width, upper_length])
                        
                        continue # Subtrucks created; continuing.
                        
                    else:
                        return False # Did not fit anywhere; leaving.
            else: 
                return False # Weight is invalid; leaving.
        else: 
            continue # The parcel did not get into a truck; continuing.

    return True # If the for loop ends, that means that there were no invalid solutions.

# 二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二　#

''' Mathematical equation used to calculate the fitness:
    Sum from 0 until len(trucks) of [
        ( Sum from 0 until len(parcels) of [ parcel that got in.area ] ) / truck[i].area ) times total number of parcels put in truck [i]
    ]'''
def fitnessCalculation(parcels, trucks, solutions): # O(solution amount x parcel amount)    
    fitness = numpy.empty(len(solutions))
    truckPut = numpy.zeros(len(trucks))
    
    # The score will increment each time it finds a value that is not -1.
    score = 0
    
    # Iterating through every solution of the array.
    for i in range(len(solutions)):
        
        # Checking if the solution is valid.
        if (truckValidity(parcels, trucks, solutions[i]) == True):
            
            # Updating the truckPut array.
            for j in range(len(parcels)):
                
                if (solutions[i][j] != -1):
                    
                    truckPut[solutions[i][j]] += 1
             
            solution_area_sum = 0
            
            # Iterating through each truck to calculate the fitness.
            for j in range(len(trucks)):
                
                for k in range(len(parcels)):
                    
                    if (solutions[i][k] == j): # If the placement is the same as the truck, proceed.
                        
                        solution_area_sum += parcels[k].area
                
                score += (solution_area_sum / trucks[j].area) * truckPut[j]
                    
        else:
            score = -10
        
        fitness[i] = score
        
        truckPut = numpy.zeros(len(trucks)) # Resetting the truckPut array.
        score = 0 # Resetting the score variable for its next use.
        
    return fitness.astype(float)

# 二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二　#
        
def chromosomeSelection(parcels, parent_amount, solutions, fitness): #O(parent_amount)
    # Copying the fitness and storing it in a new list variable because it will be altered in the following for loop.
    fitness = list(fitness)
    
    # Creating an array with its dimensions being (parent amount, amount of items)
    parents = numpy.empty((parent_amount, len(parcels)), dtype=int) 
    
    for i in range(parent_amount):
        # Retrieving the maximum fitness value. argmax will return a single value.
        max_fitness_index = numpy.argmax(fitness)
        parents[i] = solutions[max_fitness_index]
        
        # Ensuring that the current selected solution will not be selected again.
        fitness[max_fitness_index] = -1
        
    return parents

# 二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二　#
        
def exploration(parcels, selected_parents, offspring_amount): # Exploration meaning Crossover. O(offspring_amount).
    # Creating an empty array to store the offsprings.
    # .shape[1] returns the amount of columns. 
    offspring = numpy.empty((offspring_amount, len(parcels)), dtype=int)

    crossover_point = int(len(parcels)/2)
    crossover_rate = 0.85 # 85% chance for a crossover to occur.
    
    for i in range(offspring_amount):
        first_parent = i % len(selected_parents)         # i=0 - 0  i=1 - 1   i=2 - 2  [...]
        second_parent = (i + 1) % len(selected_parents)  # i=0 - 1  i=1 - 2   i=3 - 3  [...]
        
        random_value = random.uniform(0, 1) # Float in [0, 1).
        
        # If a crossover occurs, the offspring will have some values from both parents; starting
        # from 0 until the crossover point  (exclusive) for the data from the first parent, and from
        # the crossover point until the end for the second parent. If one doesn't occur, the array
        # will still be filled but with the values of the first parent.
        if (random_value <= crossover_rate):
            offspring[i, 0:crossover_point] = selected_parents[first_parent, 0:crossover_point]
            offspring[i, crossover_point:] = selected_parents[second_parent, crossover_point:]
        else:
            offspring[i, :] = selected_parents[first_parent, :]
        
    return offspring

# 二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二　#

def exploitation(parcels, trucks, offspring):
    # Creating an empty array to save mutated solutions. (dimensions same as the offspring array)
    mutations = numpy.empty((offspring.shape), dtype=int)
    mutation_rate = 0.4 # 40% chance of a solution to go through the mutation process.
    
    # Iterating through every solution from the mutations array. Then, a random number between
    # 0 and 1 is generated to see if there will be a mutation or not.
    for i in range(len(mutations)):
        random_number = random.uniform(0, 1)
        mutations[i,:] = offspring[i,:]
        
        # Checking if the mutation will occur.
        if (random_number <= mutation_rate):
            # Generating the position of the gene that will go through mutation.
            # -1 is used to confirm that the numbers will not go out of bounds.
            mutated_position = random.randint(0, len(parcels)-1)
            
            # Generating a random value in the form of a truck number or -1.
            random_mutated_value = random.randint(-1, len(trucks)-1)
            
            previous_value = mutations[i, mutated_position]
            mutations[i,mutated_position] = random_mutated_value
    
            # While loop to confirm that the new value is not the same as the previous one.
            # If it is, the number will be re-generated as many times needed.
            while (mutations[i,mutated_position] == previous_value):
                random_mutated_value = random.randint(-1, len(trucks)-1)
                mutations[i,mutated_position] = random_mutated_value
   
    return mutations

# 二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二二　#

def neuralNetwork(parcels, trucks, population_size, solutions, generation_amount):
    placement_solutions = []  # Array that stores solutions for parcels.
    
    # Counter that stops if a maximum solution has been found for too long (50 iterations), so as to save time in iterations.
    stop_counter = 0 
    previous_max_fitness = None 
    
    parent_amount = int(len(population_size)/2)
    offspring_amount = len(population_size)-parent_amount
    
    for i in range(generation_amount):
        
        if (stop_counter == 50): # Best solution has been found since 50 iterations ago; leaving the loop.
            break
        
        # Calculating the current fitness score. O(generation_amount x solution amount x parcel amount)
        fitness = fitnessCalculation(parcels, trucks, solutions)
        
        # Choosing the ideal parents (which have a high fitness score). O(generation_amount x parent_amount)
        selected_parents = chromosomeSelection(parcels, parent_amount, solutions, fitness)
        
        # Creating an offspring using the parents selected. O(generation_amount x offspring_amount)
        offspring = exploration(parcels, selected_parents, offspring_amount) 
        
        # Creating a mutation. O(generation_amount x mutation amount)
        mutations = exploitation(parcels, trucks, offspring)
        
        # Updating the initial_population array. First, the parent_amount rows of the population array will be 
        # updated with the selected_parents variable. Then, the rows remaining will be updated with the mutations.
        # 0:len(selected_parents) is used to select a portion of the rows starting from 0.
        solutions[0:len(selected_parents), :] = selected_parents 
        solutions[len(selected_parents):, :] = mutations.astype(int)
                
        current_max_fitness = numpy.argmax(fitness)
        
        # Checking to see if we have reached a maximum solution
        if (i>200):

            if (fitness[current_max_fitness] <= fitness[previous_max_fitness]):
                stop_counter += 1
            else:
                stop_counter = 0
        
        previous_max_fitness = numpy.argmax(fitness)

    last_generation_fitness = fitnessCalculation(parcels, trucks, solutions)
    
    print ("\nFinal solutions: ")
    print(solutions)
    
    # Selecting the best solution from the solutions array and storing it in a new variable.
    highest_fitness_index = numpy.argmax(last_generation_fitness)
    placement_solutions.append(solutions[highest_fitness_index, :])
        
    print("\nFinal placement solutions:")
    print (placement_solutions)
    
    return placement_solutions

#####################################################################################################################

print ("-------WELCOME-------\n")

# FOR DEBUGGING PURPOSES - WILL USE WHILE BEING EXAMINED.

# parcels = [Parcel(1, 1, 1, 1, 1, 1) for _ in range(4)]
# trucks = [Truck(4, 2, 2, 2) for _ in range(3)]
# solutions = [numpy.array([2, 2, 2, 2])]
# result = truckValidity(parcels, trucks, solutions[0])
# fitness = fitnessCalculation(parcels, trucks, solutions)

# print(result)
# print(fitness)

# Variable used as a parameter to determine whether or not all the values will be generated automatically.
selection = int(input("Press 1 to insert values manually, or 2 to have them inserted randomly: ")) 

# Generating the amount of daily orders and available trucks.
dailyOrderAmount, truckAmount = initializeValues(selection) 
print (f'\nAmount of Orders today: {dailyOrderAmount}')
print (f'Amount of Trucks: {truckAmount}')
lines()

# Creating as many truck and parcel objects as the number of trucks and parcels available.
for i in range(truckAmount):
    weight, height, length, width = truckValues(selection, i)
    trucks.append(Truck(weight, height, length, width))

for i in range(dailyOrderAmount): 
    weight, height, length, width, price = parcelValues(selection, i)
    parcels.append(Parcel(weight, height, length, width, i, price))

# Printing the data for each Truck and Parcel.
for i in range(truckAmount):
        print (f'Data for Truck number {i}:')
        print (f'Max weight: {trucks[i].maxWeight}, Height: {trucks[i].height}, Length: {trucks[i].length}, Width: {trucks[i].width}') 

lines()

for i in range(dailyOrderAmount): 
    print (f'Data for Parcel number {i}:')
    print (f'Weight: {parcels[i].weight}, Height: {parcels[i].height}, Length: {parcels[i].length}, Width: {parcels[i].width}, ID: {parcels[i].ID}, Price: {parcels[i].price}\n')

lines()

# Initializing the population values.
population_solutions, population_size, solutions, generation_amount = initializePopulation(parcels, trucks)

# Calling the neuralNetwork function to generate the final result for the ideal package placement.
placement_solutions = neuralNetwork(parcels, trucks, population_size, solutions, generation_amount)

# Updating the rotated values.
always_true = truckValidity(parcels, trucks, placement_solutions[0])

# Printing the final results.
daily_earnings = 0
lines()
for j in range(dailyOrderAmount):
    
    if (placement_solutions[0][j] == -1):
        print (f'Parcel numbered {j} was not placed in a truck.')
    else:
        if (parcels[j].rotated == True):
            print (f'Parcel numbered {j} was placed in truck {placement_solutions[0][j]} and was rotated.')
        else:
            print (f'Parcel numbered {j} was placed in truck {placement_solutions[0][j]}.')

        daily_earnings += parcels[j].price

lines()
print (f'Total earnings today: {round(daily_earnings, 2)}€')
print ("\n-------EXITING-------")
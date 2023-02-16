# Use python to read and return information from a CSV file.

print("Life-expectancy")
print()

choice = int(input("Hello, welcom to Ryker Swensen's data base. Please Enter the year of interest: "))

choice_2 = input("Thank you, Which country would you like to learn more about: ")
print()

# Set Min/Max variables
max_value = -1
min_value = 100
max_value_1 = -1
min_value_1 = 100
max_value_2 = -1
min_value_2 = 100
max_value = -1
min_value = 100
max_value_1 = -1
min_value_1 = 100
max_value_2 = -1
min_value_2 = 100
min_year = 0
max_year = 0
min_year_1 = 0
max_year_1 = 0
min_year_2 = 0
max_year_2 = 0
avg_life = 0
avg_life_2 = 0
avg_life_3 = 0
avg_life_4 = 0
avg_life_5 = 0
avg_life_6 = 0
min_country = ""
max_country = ""
min_country_1 = ""
max_country_1 = ""
min_country_2 = ""
max_country_2 = ""

# Open CSV file
with open("life_expectancy.csv") as data_base:
    header = next(data_base)
    for data in data_base:
        population = data.strip()
        data_list = population.split(",")
        country_name = data_list[0]
        country_code = data_list[1]
        year = int(data_list[2])
        life_expectancy = float(data_list[3])

        if life_expectancy < min_value:
            min_value = life_expectancy
            min_year = year
            min_country = country_name
        if life_expectancy > max_value:
            max_value = life_expectancy
            max_year = year
            max_country = country_name
        if choice == year:
            avg_life = avg_life + float(data_list[3])
            avg_life_2 = avg_life_2 + 1
            avg_life_3 = avg_life / avg_life_2
            if life_expectancy < min_value_1:
                min_value_1= life_expectancy
                min_year_1 = year
                min_country_1 = country_name
            if life_expectancy > max_value_1:
                max_value_1 = life_expectancy
                max_year_1 = year
                max_country_1 = country_name
        if choice_2 == country_name:
            avg_life_4= avg_life_4 + float(data_list[3])
            avg_life_5 = avg_life_5 + 1
            avg_life_6 = avg_life_4 / avg_life_5
            if life_expectancy < min_value_2:
                min_value_2= life_expectancy
                min_year_2 = year
                min_country_2 = country_name
            if life_expectancy > max_value_2:
                max_value_2 = life_expectancy
                max_year_2 = year
                max_country_2 = country_name

print(f"The overall max life expectancy is {max_value} from {max_country} in {max_year}")
print(f"The overall min life expectancy is {min_value} from {min_country} in {min_year}")
print()
print(f"For the year {choice}: ")
print(f"The average life expectancy across all countries was {avg_life_3:.2f}")
print(f'The max life expectancy was in {max_country_1} with {max_value_1}')
print(f'The min life expectancy was in {min_country_1} with {min_value_1}')
print()
print(f"For {choice_2}: ")
print(f"The average life expectancy across in {choice_2} is {avg_life_6:.2f}")
print(f'The max life expectancy was in {max_country_2} with {max_value_2}')
print(f'The min life expectancy was in {min_country_2} with {min_value_2}')
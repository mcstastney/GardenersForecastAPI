# >>>> READ ME: Before you run this programme, complete *ACTION REQUIRED* sections below <<<<
# Note: All references are commented at then bottom of this file

# *ACTION REQUIRED* Get API key from Slack chat, paste it in the empty 'api_key' string in 'get_weather_forecast()'
# *ACTION REQUIRED* Install 'requests' module by typing in your terminal cmd line: pip install requests
import requests # used to send HTTP requests to API
import time # used to get current time for timer delay
import math # used to round down floats to ints with math.floor
import datetime # used to get current date / time

# Emoji / unicode icons key:
seedling = "\U0001F331"
flower = "\U0001F33A"
star_eyes = "\U0001F929"
calendar_icon = "\U0001F4C5"
world_map = "\U0001F5FA"

# >>>> MAIN PROGRAMME <<<<

# Function to add typing style animation to the welcome text using a timer delay
def type_text_slowly(text, delay=0.06): # Two parameters = 1) welcome message and 2) set timer delay
    for char in text:
        print(char, end='', flush=True) # Print each character immediately and one after the other on the same line
        time.sleep(delay) # Add a delay to control the typing speed

welcome_message = ("\n\033[0;32m\033[1m{} \033[4mWelcome to the Gardener's Forecast app!\033[0m {} \033[0m\n"
                "{} Get daily seasonal gardening tips based on your personal goals and local weather forecast. {}\n"
                .format(flower, flower, seedling, seedling))
type_text_slowly(welcome_message)


# Function to get the weather forecast for the user's requested city
def get_weather_forecast():
    while True: # while True == True, get inputs from user and run the API request
        # use inbuilt .input() function to take input from the user
        city = input("\n\033[1mWhat city do you want the weather forecast for?\033[0m ")
        country_code = input("\033[1mWhat's the country code? e.g. GB\033[0m (look up country code https://www.iso.org/obp/ui/#search) ")
        api_key = "" # NOTE TO DEVELOPERS: add API key here before running the file
        # use inbuilt .format() function to insert the variables in to the api url
        url_weather = "https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}&units=metric".format(city, country_code, api_key)
        response = requests.get(url_weather) # Get data from the API via HTTP method

        if response.ok: # if request is successful (i.e. user entered valid city/country code), execute the function
            forecast = response.json() # Return data in more readable json format
            return forecast
        else:
            # if request unsuccessful, ask user to try again (using red font ANSI escape code)
            print("\u001b[31mYou've entered an incorrect city name or country code! Please try again. \u001b[0m \n")

forecast = get_weather_forecast()


# Variables to get specific data from API in readable format to use later
current_location = forecast['name'] # returns name of city
weather_overview = forecast['weather'][0]['main'] # use 0 index to retrieve this value as 'weather' is stored in a list []
weather_description = forecast['weather'][0]['description'] # use 0 index to retrieve this value as 'weather' is stored in a list []
temperature = math.floor(forecast['main']['temp']) # temp in degrees - use math.floor in math module to round float down to nearest int
wind_speed_mps = forecast['wind']['speed'] # API outputs wind speed as miles per second (MPS)
wind_speed_mph = math.floor(wind_speed_mps * 2.237) # convert MPS to miles per hour (MPH)
today_date = datetime.datetime.now().strftime("%d-%m-%Y") # use 'string format time' (strftime) in datetime modeule to convert to UK date format
readable_date = datetime.datetime.now().strftime("%d-%B-%Y") # use %B to convert month to the full word (e.g. 'September')


# Function to check if goal is valid number and use as an int in the first key for get_recommendation()
def get_user_goal():
    while True: # while True == True, get input from user
        user_goal = int(input("\n\033[1mWhat would you like to do today?\033[0m "
                          "\n1. Grow flowers and veg"
                          "\n2. Garden maintenance "
                          "\nType 1 or 2: "))
        if 1 <= user_goal <= 2: # if the user inputs number between correct range (1 - 2), proceed with the function
            return user_goal
        else:
            # if invalid number typed, ask user to try again (using red font ANSI escape code)
            print("\u001b[31mYou must type 1 or 2! Please try again.\u001b[0m\n")

chosen_task = get_user_goal()


# Function to get season from the current datetime
# test_date = '20-11-24' # *ACTION REQUIRED* add different dates to test other seasons. Replace 'today_date' in get_season with 'test_date'
def get_season():
    month = int(today_date[3:5]) # String slicing to return month from today_date i.e. slice from index 3 to 5 (excl 5)
    if month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Winter"

current_season = get_season()


# Function to get bespoke recommendations based on user input and weather report for chosen city
def get_recommendation():
    recommendations = {
        # Use a tuple within the dictionary to represent 3 conditions with a single key to make code more compact - see reference notes
        (1, "Spring", "Clear"): "Divide perennials and transplant shrubs. \nIf you move them while they are dormant, there will be less stress on the plants and they will spring back into action quickly.",
        (1, "Spring", "Clouds"): "Divide perennials and transplant shrubs. \nIf you move them while they are dormant, there will be less stress on the plants and they will spring back into action quickly.",
        (1, "Spring", "Rain"): "Cover the most delicate plants. \nUse a waterproof covering to protect young and fragile plants, including herbs and vegetables, if the rain is hard and persistent.",
        (1, "Spring", "Drizzle"): "Cover the most delicate plants. \nUse a waterproof covering to protect young and fragile plants, including herbs and vegetables, if the rain is hard and persistent.",
        (1, "Spring", "Snow"): "Keep plants warm. \nCover up plants that have tender emerging buds or foliage. If the buds haven’t begun to open yet, there’s no need to cover them.",
        (1, "Spring", "Thunderstorm"): "Start sowing indoors. \nIf you’ve got a shed, garage or greenhouse to shelter in, now is the time to start sowing vegetables and slow-germinating annuals.",
        (1, "Summer", "Clear"): "Divide perennials and transplant shrubs. \nIf you move them while they are dormant, there will be less stress on the plants and they will spring back into action quickly.",
        (1, "Summer", "Clouds"): "Divide perennials and transplant shrubs. \nIf you move them while they are dormant, there will be less stress on the plants and they will spring back into action quickly.",
        (1, "Summer", "Rain"): "Cover the most delicate plants. \nUse a waterproof covering to protect young and fragile plants, including herbs and vegetables, if the rain is hard and persistent.",
        (1, "Summer", "Drizzle"): "Cover the most delicate plants. \nUse a waterproof covering to protect young and fragile plants, including herbs and vegetables, if the rain is hard and persistent.",
        (1, "Summer", "Snow"): "Keep plants warm. \nCover up plants that have tender emerging buds or foliage. If the buds haven’t begun to open yet, there’s no need to cover them.",
        (1, "Summer", "Thunderstorm"): "Start sowing indoors. \nIf you’ve got a shed, garage or greenhouse to shelter in, now is the time to start sowing vegetables and slow-germinating annuals.",
        (1, "Autumn", "Clear"): "Keep sowing! \nSow batches of hardy broad beans and peas outdoors for early crops next year. Plant garlic cloves in a sunny well-drained spot.",
        (1, "Autumn", "Clouds"): "Keep sowing! \nSow batches of hardy broad beans and peas outdoors for early crops next year. Plant garlic cloves in a sunny well-drained spot.",
        (1, "Autumn", "Rain"): "Pot up and plant out \nLift and pot tender perennials to protect over winter. Plant evergreen shrubs and conifer hedges while the soil is warm.",
        (1, "Autumn", "Drizzle"): "Pot up and plant out \nLift and pot tender perennials to protect over winter. Plant evergreen shrubs and conifer hedges while the soil is warm.",
        (1, "Autumn", "Snow"): "Panic - this is freak weather!",
        (1, "Autumn", "Thunderstorm"): "Check your vegetable roots \nOnce the rain has stopped, recover exposed roots with soil before they dry out and risk harming the plant.",
        (1, "Winter", "Clear"): "Tidy up the borders \nWhen you cut back your borders, remove any dead and unsightly plants as these can harbour diseases.",
        (1, "Winter", "Clouds"): "Tidy up the borders \nWhen you cut back your borders, remove any dead and unsightly plants as these can harbour diseases.",
        (1, "Winter", "Rain"): "Plant your spring bulbs \nNow is a great time to plant tulips, daffodils and snowdrops – just remember to plant them deep.",
        (1, "Winter", "Drizzle"): "Plant your spring bulbs \nNow is a great time to plant tulips, daffodils and snowdrops – just remember to plant them deep.",
        (1, "Winter", "Snow"): "Have a rest with a cuppa tea – you deserve it!",
        (1, "Winter", "Thunderstorm"): "Plant and prune fruit trees and bushes \nBare root trees and bushes can be bought and planted between November and March. Prune apple and pear trees, gooseberries and currants.",
        (2, "Spring", "Clear"): "Test your garden soil \nTest every 3-5 years to see what nutrients or organic materials it needs and which it has too much of.",
        (2, "Spring", "Clouds"): "Test your garden soil \nTest every 3-5 years to see what nutrients or organic materials it needs and which it has too much of.",
        (2, "Spring", "Rain"): "Turn your compost \nEnsure the entirety of your compost is watered by mixing the damp with the dry under layers.",
        (2, "Spring", "Drizzle"): "Turn your compost \nEnsure the entirety of your compost is watered by mixing the damp with the dry under layers.",
        (2, "Spring", "Snow"): "Address hardscaping issues \nRepair damaged retaining walls, level out stepping stones, clean out gutters, and fix fences, benches, decks, sheds.",
        (2, "Spring", "Thunderstorm"): "Install a waterbutt \nRainwater is much better for plants than tap water. Make sure your waterbutt is securely sealed to avoid debris falling in!",
        (2, "Summer", "Clear"): "Mow the lawn!",
        (2, "Summer", "Clouds"): "Mow the lawn!",
        (2, "Summer", "Rain"): "Keep slugs and snails at bay \nCoffee grounds and egg shells are natural ways to deter slugs.",
        (2, "Summer", "Drizzle"): "Keep slugs and snails at bay \nCoffee grounds and egg shells are natural ways to deter slugs.",
        (2, "Summer", "Snow"): "Panic - this is freak weather!",
        (2, "Summer", "Thunderstorm"): "Pull up weeds by hand \nThe moist soil means you are much more likely to retrieve the whole root without it snapping and breaking.",
        (2, "Autumn", "Clear"): "Clean the greenhouse \nGet rid of debris, pests and diseases. Wash greenhouse glazing to let in as much of the weaker autumn daylight as possible.",
        (2, "Autumn", "Clouds"): "Clean the greenhouse \nGet rid of debris, pests and diseases. Wash greenhouse glazing to let in as much of the weaker autumn daylight as possible.",
        (2, "Autumn", "Rain"): "Sort your drainage \nMake sure there is a proper runoff that slopes away from that garden and, most importantly, make sure it is not blocked.",
        (2, "Autumn", "Drizzle"): "Sort your drainage \nMake sure there is a proper runoff that slopes away from that garden and, most importantly, make sure it is not blocked.",
        (2, "Autumn", "Snow"): "Panic - this is freak weather!",
        (2, "Autumn", "Thunderstorm"): "Weed and prune \nPut on your woolies and waterproofs and get out there!",
        (2, "Winter", "Clear"): "Tend to the pond \nClean up ponds, water features and bird baths. Add a ball to stop the surface freezing over.",
        (2, "Winter", "Clouds"): "Tend to the pond \nClean up ponds, water features and bird baths. Add a ball to stop the surface freezing over.",
        (2, "Winter", "Rain"): "Get organised \nTidy the shed, sort seeds and plan sowings, take an inventory of supplies and plan your garden for next year.",
        (2, "Winter", "Drizzle"): "Get organised \nTidy the shed, sort seeds and plan sowings, take an inventory of supplies and plan your garden for next year.",
        (2, "Winter", "Snow"): "Feed the birds \nBirds require high-energy foods right now as they build up reserves ready for nesting and breeding.",
        (2, "Winter", "Thunderstorm"): "Clean tools and pots \nCheck that your hand tools are in tip top condition for the gardening season ahead. Oil and sharpen secateurs and loppers.",
    }
    key = (chosen_task, current_season, weather_overview) # 3 variables make up the keys in the dictionary
    return recommendations.get(key, "Sorry, we don't have any specific recommendations for the given conditions.")
    # Get the value (recommendation) related to the specific key combination.
    # If no recommendation available for weather condition return a message

your_recommendation = get_recommendation()


# Print the results to the console with added formatting and emojis
def display_results():
    return("\n\u001b[44m\u001b[37;1m \033[1m--------------{} YOUR FORECAST & GARDENING TIPS {}-------------- \033[0m \n" 
           "\n\033[4m\033[0;32m\033[1m {} Your personalised gardening tips are ready! {} \033[0m\n"
          "\nThe forecast for {} \033[1m{}\033[0m on {} {} is \033[1m{}\033[0m. "
          "\nThe temperature \N{thermometer} is \033[1m{}\N{DEGREE SIGN}\033[0m, and the wind speed is \033[1m{} MPH\033[0m.\n"
           "\n\033[1mBased on today's forecast and tasks suitable for the {} season, you should\033[0m: \n"
           "{}\n"
           "\n\u001b[44m\u001b[37;1m \033[1m--------------{} GOOD LUCK & HAPPY GARDENING! {}---------------- \033[0m \n"
          .format(flower, flower, star_eyes, star_eyes, world_map, current_location, calendar_icon, readable_date,
                  weather_overview, temperature, wind_speed_mph, current_season, your_recommendation, seedling, seedling))

print_results = display_results()
print(print_results)


# Print plain text results to the text file (emojis and other unicodes throw an error in txt file)
def txt_results():
    return("\nThe forecast for {} on {} is {}."
          "\nThe temperature is {} degrees, and the wind speed is {} MPH.\n"
           "\nBased on today's forecast and recommended tasks for the {} season, you should:\n{}\n"
          .format(current_location, readable_date, weather_overview, temperature, wind_speed_mph, current_season, your_recommendation))

file_results = txt_results()

# Write results to txt file
file = open('gardeners_forecast_results_history.txt', 'w') # To append results to txt file, swap 'w' with 'a'
get_results = file_results
file.write(get_results)
file.close()

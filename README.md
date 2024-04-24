# ﻿Gardener's forecast API
I built this console app to get daily seasonal gardening tips based on the user's goals and real-time local weather forecast.

API used: [https://openweathermap.org/api](https://openweathermap.org/api)

## How to run the project
1. Before you run this programme, get your API key from [https://openweathermap.org/api](https://openweathermap.org/api).
2. Copy paste your API key into the empty 'api_key' string in 'get_weather_forecast()'
3. Install 'requests' module by typing in your terminal cmd line: **pip install requests**

## Future improvements
For the next version of this app, I would:
- Add to the 'if else' statement in my get_user_goal() function so that if the user enters any input that isn't an integer, it prints an error msg.
- Print the goal as a string in my display_results() function
- Use an API with an 8 day forecast and ask user to choose which day they want forecast / tips for

## Credits / references
### Typing style animation 
I asked Chat GPT: "How can I add a slow typewriter style animation to Python":
Code from Chat GPT:
        def slow_typewriter(text, delay=0.1):
             for char in text:
                 print(char, end='', flush=True)  # end='' to avoid newline, flush=True to ensure immediate printing
                 time.sleep(delay)  # introduce a delay between characters
        # Example usage
        slow_typewriter("Hello, World!")

I tweaked this and used for my type_text_slowly() function.

### flush() method
Further reading: [https://www.w3schools.com/python/ref_file_flush.asp](https://www.w3schools.com/python/ref_file_flush.asp)

### Solution for 'get_season()' function 
Fixed with help from Chat GPT. 

My prompt was: "How can I fix my Python function to return what the season is according to the current datetime month? This is my code:"

         def get_season():
         
           for %m in today_date(12):
           
              if %m == 3 or 4 or 5:
              
               return("Spring")
               
              elif %m == 6 or 7 or 8:
              
               return("Summer")
               
              elif %m == 9 or 10 or 11:
              
               return("Autumn")
               
              else:
              
               return("Winter")
               
        current_season = get_season()

### Solution for get_recommendation() 
Refined with help from Chat GPT. 

My prompt was: "How can I make my Python function more efficient? Here's my code:

        def get_recommendation():
        
             if goal == 1 and current_season == "Spring" and (weather_overview == "Clear" or weather_overview == "Clouds"):
             
                 print("It's a good time to Divide perennials and transplant shrubs. \nIf you move them while they are dormant, there will be less stress on the plants and they will spring back into action quickly.")
                 
             elif goal == 1 and current_season == "Spring" and (weather_overview == "Rain" or weather_overview == "Drizzle"):
             
                 print("It's a good time to Cover the most delicate plants. \nUse a waterproof covering to protect young and fragile plants, including herbs and vegetables, if the rain if hard and persistent.")
                 
             elif goal == 1 and current_season == "Spring" and weather_overview == "Snow":
             
                 print("It's a good time to Keep plants warm. \nCover up plants that have tender emerging buds or foliage. If the buds haven’t begun to open yet, there’s no need to cover them.")
                 
        # ...Plus 29 other elif statements using the same format which I wrote in its entirity!"

### Printing emojis in Python
[https://medium.com/@natashanewbold/print-emojis-using-python-53736bb32b9d#:~:text=Printing%20emojis%20using%20Python%20is,applications%20more%20expressive%20and%20engaging](https://medium.com/@natashanewbold/print-emojis-using-python-53736bb32b9d#:~:text=Printing%20emojis%20using%20Python%20is,applications%20more%20expressive%20and%20engaging)

### Unicode characters
- \N{DEGREE SIGN} - Degrees celsius sign: [https://stackoverflow.com/questions/3215168/how-to-get-character-in-a-string-in-python](https://stackoverflow.com/questions/3215168/how-to-get-character-in-a-string-in-python)
- \U0001F4C5 - Calendar icon [https://www.compart.com/en/unicode/U+1F4C5#:~:text=%E2%80%9C%F0%9F%93%85%E2%80%9D%20U%2B1F4C5%20Calendar%20Unicode%20Character](https://www.compart.com/en/unicode/U+1F4C5#:~:text=%E2%80%9C%F0%9F%93%85%E2%80%9D%20U%2B1F4C5%20Calendar%20Unicode%20Character)
- \U0001F5FA - World map icon [https://stackoverflow.com/questions/40061158/what-is-the-uni-code-of-map-icon#:~:text=Probably%20the%20closest%20to%20a,i.e.%20aren't%20red](https://stackoverflow.com/questions/40061158/what-is-the-uni-code-of-map-icon#:~:text=Probably%20the%20closest%20to%20a,i.e.%20aren't%20red)
- \N{thermometer} [https://en.wikipedia.org/wiki/List_of_emojis](https://en.wikipedia.org/wiki/List_of_emojis)

### ANSI escape codes
- \033[0;32m - green text colour [https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007](https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007)
- \u001b[42;1m - green background colour [https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html)

### Gardening tasks for different seasons
- [https://www.countryliving.com/uk/homes-interiors/gardens/a887/what-to-do-to-garden-heavy-rain/](https://www.countryliving.com/uk/homes-interiors/gardens/a887/what-to-do-to-garden-heavy-rain/)
- [https://15minutesofgreen.com/rainy-day-jobs/](https://15minutesofgreen.com/rainy-day-jobs/)
- [https://ngs.org.uk/your-winter-gardening-to-do-list/](https://ngs.org.uk/your-winter-gardening-to-do-list/)
- [https://www.provenwinners.com/learn/early-spring/10-essential-spring-gardening-tasks](https://www.provenwinners.com/learn/early-spring/10-essential-spring-gardening-tasks)
- [https://www.gardenersworld.com/what-to-do-now-october/](https://www.gardenersworld.com/what-to-do-now-october/)

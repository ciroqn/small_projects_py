gamers = []

def add_gamer(gamer, gamers_list):
    if gamer["name"] and gamer["availability"]:
        gamers_list.append(gamer)


def build_daily_frequency_table():
    return {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}


def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer["availability"]:
            available_frequency[day] += 1


def find_best_night(availability_table):
    highest = 0
    best_day = ''
    for key, value in availability_table.items():
        if value > highest:
            highest = value
            best_day = key
    return best_day


def available_on_night(gamers_list, day):
    attendees = []
    for gamer in gamers_list:
        if day in gamer["availability"]:
            attendees.append(gamer['name'])
    return attendees


def send_email(gamers_who_can_attend, day, game):
    for name in gamers_who_can_attend:
        print(form_email.format(name, day, game))


kimberly = {"name": "Kimberly Warner", "availability": ["Monday", "Tuesday", "Wednesday"]}
add_gamer(kimberly, gamers)

add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

# construct frequency table for each day (a dict)
count_availability = build_daily_frequency_table()

# best night for game (most gamers)
calculate_availability(gamers, count_availability)

# save best night to var
game_night = find_best_night(count_availability)

# gamers available on best night
attending_game_night = available_on_night(gamers, game_night)

# template for mail message
form_email = "Hi {}. Our games night is on {}. We will be playing {}"

send_email(attending_game_night, game_night, "Abruptly Goblins!")

# for those who can't attend best night, arrange second best night
unable_to_attend_best_night = []

for gamer in gamers:
    if game_night not in gamer["availability"]:
        unable_to_attend_best_night.append(gamer)
    
# create another frequency table for the second best night
second_night_availability = build_daily_frequency_table()

# find second best night
calculate_availability(unable_to_attend_best_night, second_night_availability)

# save second best night to var
second_night = find_best_night(second_night_availability)

# print(second_night)

# find attendees for second best night
available_second_game_night = available_on_night(gamers, second_night)

send_email(available_second_game_night, second_night, "Abruptly Goblins!")

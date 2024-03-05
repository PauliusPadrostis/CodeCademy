from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# Build your program below:
landmark_string = ""
for letter, landmark in landmark_choices.items():
    landmark_string += f'{letter} - {landmark}\n'

stations_under_construction = ['Granville']


def greet():
    print('Hi there! Welcome to SkyRoute!\n')
    print(f'We will help you find the shortest route between the following Vancouver landmarks:\n\n{landmark_string}')


def skyroute():
    greet()
    new_route()
    goodbye()


def get_active_stations():
    updated_metro = vc_metro
    for station_uc in stations_under_construction:
        for station, con_station in vc_metro.items():
            if station != station_uc:
                updated_metro[station] -= set(stations_under_construction)
            else:
                updated_metro[station] = set([])

    return updated_metro


def set_start_and_end(start_point, end_point):
    if start_point is not None:
        change_point = input(
            'What would you like to change? You can enter "o" for "origin", "d" for "destination", or "b" for "both"')
        if change_point == 'b':
            start_point = get_start()
            end_point = get_end()
        elif change_point == 'o':
            start_point = get_start()
        elif change_point == 'd':
            end_point = get_end()
        else:
            print('That is not one of the choices. Please try again!')
            set_start_and_end(start_point, end_point)
    else:
        start_point = get_start()
        end_point = get_end()

    return start_point, end_point


def get_start():
    start_point_letter = input('Where are you coming from? Type in the corresponding letter: ')
    if start_point_letter in landmark_choices:
        start_point = landmark_choices[start_point_letter]
        return start_point
    else:
        print('Sorry, that is not a landmark we have data on. Let us try this again...')
        get_start()


def get_end():
    end_point_letter = input('Where are you headed? Type in the corresponding letter: ')
    if end_point_letter in landmark_choices:
        end_point = landmark_choices[end_point_letter]
        return end_point
    else:
        print('Sorry, that is not a landmark we have data on. Let us try this again...')
        get_end()


def show_landmarks():
    see_landmarks = input(f'Would you like to see the list of landmarks again? Enter y/n:')
    if see_landmarks == 'y':
        print(landmark_string)


def new_route(start_point=None, end_point=None):
    start_point, end_point = set_start_and_end(start_point, end_point)

    shortest_route = get_route(start_point, end_point)

    if shortest_route:
        shortest_route_string = '\n'.join(shortest_route)
        print(f'\nThe shortest metro route from {start_point} to {end_point} is:\n\n{shortest_route_string}')
    else:
        print(f'Currently there are no routes between {start_point} and {end_point} due to maintenance.')

    again = input(f'Would you like to see another route? Enter y/n: ')
    if again == 'y':
        show_landmarks()
        new_route(start_point, end_point)


def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]
    routes = []

    for start_station in start_stations:
        for end_station in end_stations:
            metro_system = get_active_stations() if stations_under_construction else vc_metro
            if stations_under_construction:
                possible_route = dfs(metro_system, start_station, end_station)
                continue
            route = bfs(metro_system, start_station, end_station)

            if route is not None:
                routes.append(route)

                shortest_route = min(routes, key=len)
                return shortest_route


def goodbye():
    print('Thanks for using SkyRoute!')


print(get_route('Marine Building', 'Robson Square'))

skyroute()

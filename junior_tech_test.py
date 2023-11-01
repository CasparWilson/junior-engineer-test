import csv

def read_csv_file(file_path):
    """
    Read a CSV file and return its content as a list of dictionaries.
    """
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        list_of_dict = []
        for row in reader:
            list_of_dict.append(row)
    return list_of_dict

def get_unique_teams(data):
    """
    Return a set of unique team names from the provided data.

    I assumed the question was just trying to get unique team_names, and not possession_team_name values
    """
    return {dict['team_name'] for dict in data}

def get_most_common_event_type(data):
    """
    Return the most common event type name from the provided data.
    """
    event_tally = {}
    for dict in data:
        event_type_name = dict['event_type_name']
        if event_type_name in event_tally:
            event_tally[event_type_name] += 1
        else:
            event_tally[event_type_name] = 1
    num_of_most_common_event = (max(event_tally.values()))
    index_most_common_event = list(event_tally.values()).index(num_of_most_common_event)
    return list(event_tally.keys())[index_most_common_event]

def filter_by_team(data, team_name):
    """
    Filter the data by the provided team name and return the filtered data.
    """
    return[dict for dict in data if dict['team_name'] == team_name]

def filtered_by_team_and_event_type(data, team_name, event_type_name):
    return [dict for dict in data if dict['team_name'] == team_name and dict['event_type_name'] == event_type_name]

def count_event_type_by_team(data, team_name, event_type_name):
    """
    Count the number of events of a specific type for a given team.
    """
    return len(filtered_by_team_and_event_type(data, team_name, event_type_name))

def average_pass_length_by_team(data, team_name):
    """
    Calculate the average pass length for the provided team to 1 decimal place
    """
    team_pass_dicts = filtered_by_team_and_event_type(data, team_name, 'Pass')
    team_pass_lengths = [float(dict['pass_length']) for dict in team_pass_dicts]
    return(round((sum(team_pass_lengths))/(len(team_pass_lengths)), 1))

def filter_players_by_position(data, position_name):
    """
    Return a list of player names who play at the provided position.

    So there are columns for 'position_name', 'formation_position_name', 'player_position_name' and 'freeze_frame_position_name'.
    I initially tried 'position_name', but all the 'Center-Forwards' are stored under 'formation_position_name'.  I do not know if there is
    a technical difference here so I just stuck to using the formation variant, but could easily generate sets for each and then combine the results.
    """
    return {dict['formation_player_name'] for dict in data if dict['formation_position_name'] == position_name}


def count_successful_passes(data):
    """
    Count the number of successful passes (not considering pass outcome).
    
    I do not understand how else I am supposed to determine whether a pass is successful except by considering the outcome for passes.
    All the outcome_names are ways for a pass to be incomplete, so I will simply count the passes that lack a value for 'outcome_names'
    and assume the question does not want to know if pass lead to a goal etc.
    """
    return len([dict for dict in data if dict['event_type_name'] == 'Pass' and dict['outcome_name'] == ''])

def filter_by_period(data, period):
    """
    Return a list of events that occurred in the provided period (e.g., 1 or 2).

    Initially I returned a list just of the event_type_name that occurred in the period, but the test made it clear a list of dictionaries including
    the period property was expected so I just performed a filter.
    """
    return [dict for dict in data if dict['period'] == period] 

def count_shots_by_player(data, player_name):
    """
    Count the number of shots taken by the provided player.

    Was getting too many counts do made sure only one entry per ID
    """
    # print([dict for dict in data if dict['event_type_name'] == 'Shot'])
    return len({dict['id'] for dict in data if dict['event_type_name'] == 'Shot' and dict['player_name'] == player_name})

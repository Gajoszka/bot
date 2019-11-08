import copy

# empty list
listOfEvents = []

# empty dictionary
event = {
    'summary': None,
    'description': None,
    'start': None,
    'end' : None,
    'attendees': [
        {'email': None},
    ],

}
def get_promotions():
    return listOfEvents
def upload_promos_list(the_list):
    event = the_list

# to register a new promotion
def process_new_promotion(event_list, the_type, rate):
     data = []
     e = {}
     if len(event_list) != 0:
        new_list = copy.deepcopy(event_list) # #creates a deep copy to reference a completely new object
        e['promo_type'] = the_type
        e['discount'] = rate
        new_list.append(e)
        data = new_list
     else:
        event['promo_type'] = the_type
        event['discount'] = rate
        event_list.append(event)
        data = event_list
     return data
# to view all promotions
def process_view_promotion(event_list):
     for index in range(len(event_list)):
        ev = event_list[index]
        print(ev)
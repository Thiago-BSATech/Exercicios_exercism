"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue: list - names in the normal queue.
    :param ticket_type: int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """

    

    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    elif ticket_type == 0:
        normal_queue.append(person_name)
        return normal_queue
    pass


def find_my_friend(queue, friend_name):
    """Search the queue for a name and return their queue position (index).

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """

    return queue.index(friend_name)

    pass


def add_me_with_my_friends(queue, index, person_name):
    """Insert the late arrival's name at a specific index of the queue.

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue, person_name):
    """Remove the mean person from the queue by the provided name.

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return: list - queue update with the mean persons name removed.
    """
    queue.remove(person_name)
    return queue

    pass


def how_many_namefellows(queue, person_name):
    """Count how many times the provided name appears in the queue.

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return: int - the number of times the name appears in the queue.
    """
    i = 0
    
    for index in queue:
        
        if(index == person_name):
            i += 1
    return i

    pass


def remove_the_last_person(queue):
    """
    Removes the last person from the queue and returns their name.
    The queue list is updated in place.
    
    Parameters:
    queue (list): The list of people in the queue.
    
    Returns:
    str: The name of the person removed.
    """
    return queue.pop()
def sorted_names(queue):
    """
    Returns a sorted copy of the queue in alphabetical order.
    The original queue list is not modified.
    
    Parameters:
    queue (list): The list of people in the queue.
    
    Returns:
    list: A new list with the names sorted alphabetically.
    """
    return sorted(queue)
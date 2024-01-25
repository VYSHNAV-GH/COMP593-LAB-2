def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name':'vyshnav amruthraj R',
        'student_id':10327042,
        'pizza_toppings':['PINAPPLE','PEPPERONI','GARLIC'],
        'movie':[
            {
                'title':'Avatar',
                'genre':'fantasy'
            },
            {
                'title':'Endgame',
                'genre':'Superhero'
            }
        ]
    }   

    # TODO: Step 3 - Add another movie to the data structure
    Another_movie={
        'title':'Titanic',
        'genre':'Romantic'
    }
    about_me['movie'].append(Another_movie)
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me, toppings)
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me['movie'])
    


# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    print(f'My name is {about_me['full_name']}, but you can call me Sir{about_me['full_name'].split()[0]}')
    print(f'My student ID is {about_me['student_id']}')
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
toppings=('grounded beef','paneer')
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].extend(toppings)
    about_me['pizza_toppings'].sort()
    about_me['pizza_toppings']=[item.lower() for item in about_me['pizza_toppings']]
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("My favourite pizza toppings are:")
    for i in about_me['pizza_toppings']:
        print(f"-{i}")
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    Genres=[movie['genre'] for movie in about_me ['movie']]
    print('i like to watch',end='')
    for genre in range(len(Genres)-1):
        print(f'{Genres[genre]},',end='')
        print(f'and{Genres[-1]}movies.')

    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    all_titles = [movie['title'] for movie in movie_list]
    edited_titles = [word.capitalize() for word in all_titles]
    print("some of my favourite movies are",end='')
    for i in range(len(edited_titles)-1):
        print(f'{edited_titles[i]},', end = ' ')
    print(f'and {edited_titles[-1]}!')
        
    return
    
if __name__ == '__main__':
    main()
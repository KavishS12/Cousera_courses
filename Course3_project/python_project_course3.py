import json
import requests_with_caching

def get_movies_from_tastedive(movie_name):
    base_url='https://tastedive.com/api/similar'
    params_dict={}
    params_dict['q']=movie_name
    params_dict['type']='movies'
    params_dict['limit']=5
    result = requests_with_caching.get(base_url,params=params_dict)
    return json.loads(result.text)

def extract_movie_titles(result_dict):
    movies_list=[]
    for i in result_dict["Similar"]["Results"]:
        print(i["Name"])
        movies_list.append(i["Name"])
    return movies_list

def get_related_titles(movie_titles_lst):
    combined_lst=[]
    for movie in movie_titles_lst:
        related_movies=get_movies_from_tastedive(movie)
        extracted_titles=extract_movie_titles(related_movies)
        for title in extracted_titles:
            if title not in combined_lst:
                combined_lst.append(title)
    return combined_lst

def get_movie_data(movie):
    base_url="http://www.omdbapi.com/"
    param_dict={}
    param_dict["t"]=movie
    param_dict["r"]="json"
    result = requests_with_caching.get(base_url,params=param_dict)
    return (json.loads(result.text))
    
def get_movie_rating(result_dict):
    for lst_item in result_dict["Ratings"]:
        if lst_item["Source"] == "Rotten Tomatoes":
            ans=lst_item["Value"][:-1]
            return int(ans)
    return 0

def get_sorted_recommendations(movies_lst):
    related_titles = get_related_titles(movies_lst)
    new_dict = {}
    for movie in related_titles:
        rating = get_movie_rating(get_movie_data(movie))
        new_dict[movie] = rating
    return [i[0] for i in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]

    




import pickle
from .models import profile
movies = pickle.load(open('C:/Users/sagar/movieRS/movies/model/movie_list.pkl','rb'))
similarity = pickle.load(open('C:/Users/sagar/movieRS/movies/model/similarity.pkl','rb'))
movie_list = movies['title'].values
def rec(movie,pf):
    # movie=movie.lowercase()
    already_watched=[]
    for x in pf.title.all():
        already_watched.append(x.title)
    index = movies[movies['title'] == movie.title].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    y=1
    x=0
    while x<10:
        # fetch the movie poster
        i=distances[y]
        if(movies.iloc[i[0]].title in already_watched):
            y=y+1
        else:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_names.append(movies.iloc[i[0]].title)
            y=y+1
            x=x+1

    return recommended_movie_names

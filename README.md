# Project Luther


## Question:

* Can the rating of a movie (by critics and amateurs) be predicted from the release date?
* Secondary question: which features are relevant for the rating of a movie?

__Hypothesis:__  
Rotten Tomatoes has a limited database, presumably it is regularly cleaned out, getting rid of reviews of movies that are not relevant anymore. Older movies are more likley to be eliminated from the databse, or were never in there to begin with, __except__ if they are considered to be classics and are hence likley have a higher rating. 

## Description of my sample of movies and/or other data:

* 1484 movies from the [Rotten Tomatoes] (https://www.rottentomatoes.com/browse/dvd-streaming-all?minTomato=0&maxTomato=100&services=amazon;hbo_go;itunes;netflix_iw;vudu;amazon_prime;fandango_now&genres=14&sortBy=release) website, from the category 'Sci-Fi and Fantasy'. 
* No selection by date or rating, all movies from the category are taken into account.

__Note:__ other categories may be included time permitting, code is written to easily scrape data from other categories.


## Characteristics of each movie:

* Sci-Fi or Fantasy
* Following variables are collected:
> 1. Critics score
> 2. Critics rating
> 3. Number of critics reviews
> 4. Number of 'Fresh' classifications
> 5. Number of 'Rotten' classifications
> 6. Audience score
> 7. Audience rating
> 8. Number of audience reviews
> 9. Director
> 10. Box office
> 11. Runtime
> 12. Release date in theaters
> 13. Release date on disc
> 14. Rating
> 15. Studio  


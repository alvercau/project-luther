# Process and results


## 1. Questions, data and variables

See Readme.

## 2. Design

Steps:
* Formulation of the hypothesis: how to make a popular sci-fi/fantasy movie?
* Identification and scraping of the data: Rotten Tomatoes has movie ratings by critics and the audience. Several other variables are available:
> Title of the movie  
> Url to the details of the movie  
> Percentage of Approved Tomatometer critics who gave a positive review to the movie  
> Average rating according to the critics  
> Number of critics that have reviewed the movie  
> Number of positive reviews by critics  
> Number of negative reviews by critics  
> Percentage of the audience that gave positive review  
> Average rating according to audience  
> Director  
> Box office  
> Runtime  
> Release date in theaters  
> Release date on disc/streaming  
> MPAA rating and reason for rating  
> Studio  
* Data cleaning
* Selection of relevant variables: given the scenario, only variables that can be chosen before making a movie will be taken into acount.

| Dependent variables | Independent variables |
| --- | --- |
| Rating critics, rating audience | runtime, director, release month (extracted from release in theatres), MPAA rating, studio


* Building the model (iterative design)


## 3. Scraping

[notebook](../blob/master/Scraping_rotten_tomatoes.ipynb)
[Spider](../blob/master/rotten_spider2.py)


## 4. Data cleaning

[notebook](../blob/master/Project_Luther_data_cleaning.ipynb)

## 5. Regression analysis

[notebook](../blob/master/Regression_the_neat_way.ipynb)

Creating an overal rating variable: the mean difference between critics rating and audience rating is smaller than the standard deviation of the difference, so this option was not explored. Two models were built: one for predicting the critics ratings, and one for the audience ratings.

I wanted to include 'Studio' as an independent variable as well, but there were a lot of NaNs in that column, and regression analysis does not take into account NaNs. If I would have included that variable, I would have lost half of the data points. I could have scraped 'studio' from other sources, but not time.

Model was refined as follows:
* only runtime: bad R squared, bad scores for predictions: there was no correlation between ratings and runtime. Test several polynomials: degree 6 had the best results. This model was used as the base model.
* runtime + director: good R squared but overfitting: including the director introduces a lot of multicollinearity. Ridge regularization with alpha = 0.8 gave better results, but still massive overfitting.
* runtime + MPAA rating: bad R squared, bad scores for predictions: there was no correlation between ratings and runtime + MPAA rating.
* runtime + month of release: bad R squared, bad scores for predictions: there was no correlation between ratings and runtime + month of release

Since the inclusion of director had a dramatic impact on the fit of the model (at least fr the training data), refine the model based on this variable. 

* Select only those movies that were made by productive directors (directors that made more than 5 movies in the dataset, a total of 125 movies): 
	* runtime + productive directors + Ridge regularization: R squared for training data was not that good (0.46), score of predictions was similar (0.47). Best model that I could find.


## 6. Results

Predicting ratings is damn hard, but critics ratings are slightly more predictable than audience ratings. This is probably due to the fact that the audience is a more heterogeneous group than the critics. The most relevant factor is the director. I recommend working with the following directors:

1. Ridley Scott (Blade runner, Alien, The martian)
2. Sam Raimi (Evil Dead, The jungle book)
3. James Cameron (The terminator, Aliens)


## 7. Future considerations

* Include more numeric independent variables, such as budget. Categorical variables do not combine well with linear regression.
* Include rating data from other sources (IMDB, Fandango) in order to augment the dataset of productive directors and build a stronger model.
* Include the principal actors, the Studio, whether the movie was an adaptation to the screen. However, this means including more caegorical variables, and linear regression is not the best type of modelling for this type of variables.


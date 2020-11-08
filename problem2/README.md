# Problem 2 - Forex

## Question 3
In the following example determine the date where the Australian dollar had the best exchange rate for the previous month.  You will need to fetch data for each day in that month, extract the Australian dollar rate (AUD).  Write a function to return as a tuple the date and best rate.

The daily data (for example May 1st 2019) can be fetched from https://api.exchangeratesapi.io/2019-05-01, and the requests library is recommended. Return the latest date if there are multiple dates with the same highest exchange rate.

For example where May 5th had the highest AUD value the result would look something like:

### Output
```
>>>best_rate()
'2019-05-19', 1.6239
```

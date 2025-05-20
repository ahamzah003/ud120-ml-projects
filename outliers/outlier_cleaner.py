#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    # create a list of tuples (age, net_worth, error)
    error = [(age, net_worth, abs(prediction - net_worth)) for prediction, age, net_worth in zip(predictions, ages, net_worths)]
    # sort list in ascending order by absolute error
    error_sorted = sorted(error, key=lambda x: x[2])
    # remove the 10% of points with the largest errors
    limit = int(len(error_sorted) * 0.9)
    cleaned_data = error_sorted[:limit]
    return cleaned_data


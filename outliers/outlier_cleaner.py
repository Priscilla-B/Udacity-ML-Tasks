#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):

    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    

    zipped = zip(ages, net_worths, abs(predictions - net_worths))
    cleaned_data = list(zipped)

    cleaned_data.sort(key=lambda tup: tup[2])

    return cleaned_data[:round(len(cleaned_data) * 0.9)]
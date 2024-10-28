def ft_filter(function, sequence):
    if function:
        return (elem for elem in sequence if function(elem))
    return (elem for elem in sequence if elem)


ft_filter.__doc__ = "A function that filters words from the function provided"

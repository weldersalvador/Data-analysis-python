import numpy as np

def calculate(list):
    if (len(list) != 9):
        raise ValueError("List must contain nine numbers.")
    array = np.array(list)
    array = array.reshape((3,3))
    dict = {"Mean": [],
            "Variance": [],
            "Standart Deviation": [],
            "Max": [],
            "Min": [],
            "Sum": []
            }

    flattered = array.flatten()
    dict["Mean"].append(array.mean(axis = 0))
    dict["Mean"].append(array.mean(axis = 1))
    dict["Mean"].append(flattered.mean())

    dict["Variance"].append(array.var(axis = 0))
    dict["Variance"].append(array.var(axis = 1))
    dict["Variance"].append(flattered.std())

    dict["Standart Deviation"].append(array.std(axis = 0))
    dict["Standart Deviation"].append(array.std(axis = 1))
    dict["Standart Deviation"].append(flattered.std())

    dict["Max"].append(array.max(axis = 0))
    dict["Max"].append(array.max(axis = 1))
    dict["Max"].append(flattered.max())

    dict["Min"].append(array.min(axis = 0))
    dict["Min"].append(array.min(axis = 1))
    dict["Min"].append(flattered.min())

    dict["Sum"].append(array.sum(axis = 0))
    dict["Sum"].append(array.sum(axis = 1))
    dict["Sum"].append(flattered.sum())
    return dict
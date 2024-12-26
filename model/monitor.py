from time import time

def monitor_prediction_time():
    def wrapper(func):
        def inner(*args, **kwargs):
            start_time = time()
            result = func(*args, **kwargs)
            end_time = time()
            print(f"Prediction time: {end_time - start_time:.4f} seconds")
            return result
        return inner
    return wrapper
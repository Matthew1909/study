# Decorators are functions that enhance other functions by "adding more code" without actually changing
# the function.
# e.g.:
import time
from datetime import datetime, timedelta


# when a function with decorator is executed what basically happens is:
# - the execution ignores the base version;
# - goes to the decorator and then take the enhanced version;
# - makes the simple version name reference to the enhanced version;
# - execute the enhanced version through the name of the simple version.
def timer_dec(base_func):
    # if the function to be decorated has parameters then this enhanced version has also to receive them
    def enhanced_func(*args, **kwargs):
        start_time = time.time()
        # funny thing: here the * in *args, **kwargs is just unpacking syntax
        # if the decorated function has any return then here we should capture the return
        result = base_func(*args, **kwargs)
        end_time = time.time()
        print(f"Task time: {end_time - start_time} seconds.")
        return result
    return enhanced_func


@timer_dec
def brew_tea(tea_type, steep_time):
    print(f"Brewing {tea_type} tea...")
    time.sleep(steep_time)
    print("Tea is ready!")


@timer_dec
def make_matcha():
    print("Making matcha...")
    time.sleep(1)
    print("Matcha is ready!")
    return f"Drink match by {datetime.now() + timedelta(minutes=30)}"


brew_tea(tea_type="green", steep_time=1)
print(make_matcha())

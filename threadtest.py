import threading

def my_thread_function():
    # Code to be executed in the thread goes here
    print("This is running in a separate thread")

# Create a new thread
my_thread = threading.Thread(target=my_thread_function)

# Start the thread
my_thread.start()
# Create and start 5 threads
for _ in range(5):
    thread = threading.Thread(target=my_thread_function)
    thread.start()
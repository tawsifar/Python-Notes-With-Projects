import threading
import time

# multithreading = run multiple tasks concurrently instead of one after another
# best for I/O bound tasks: reading files, network calls, API requests
# while one task is waiting (like time.sleep simulating a network delay),
# another thread can run instead of the CPU just sitting idle

def walk_dog(first, last):
    time.sleep(8)  # simulates an 8 second task
    print(f"You finish walking {first} {last}")

def take_out_trash():
    time.sleep(2)  # simulates a 2 second task
    print("You take out the trash")

def get_mail():
    time.sleep(4)  # simulates a 4 second task
    print("You get the mail")


# without threading these three would run one after another
# total time = 8 + 2 + 4 = 14 seconds

# with threading, all three start almost instantly
# total time = the longest single task = 8 seconds

start_time = time.time()

# creating a Thread object
# target = which function to run
# args = arguments to pass into that function, must be a tuple (comma needed even for one arg)
chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore1.start()  # actually starts the thread, doesnt wait for it to finish

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

# .join() blocks the main program here until that specific thread finishes
# without join(), the program would move on immediately and print "All chores are complete!"
# even while the threads are still running in the background
chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")

end_time = time.time()
print(f"Total time: {end_time - start_time:.2f} seconds")
# expected output order (trash and mail can finish before the dog walk):
# You take out the trash
# You get the mail
# You finish walking Scooby Doo
# All chores are complete!
# Total time: 8.0X seconds   <- not 14, because tasks ran concurrently
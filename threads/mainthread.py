import threading

print("current thread is =",threading.currentThread().getName())

if threading.current_thread()==threading.main_thread():
    print("main thread ")
else:
    print("anpther thread ")
    
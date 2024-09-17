import time
current_time = int(time.strftime("%H"))

if current_time >= 0 and current_time < 12:
    print("Good Morning! Sir")
elif current_time >= 12 and current_time < 16:
    print("Good Afternoon! Sir")
elif current_time >= 16 and current_time < 21:
    print("Good Evening! Sir")
else:
    print("Good Night! Sir")


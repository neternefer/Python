import time
import webbrowser


def break_time():
    session  = int(input("How many sessions do you want for today? "))
    duration = input("How many hours should a session last?(Use hh.mm format)")
    minutes = duration.split(".")[1]
    hours = duration.split(".")[0]

    print("This program was started at", time.ctime())
    print("Number of learning sessions for today:", session, '\n')
          
    if hours == '0':
        print("Session duration: {}".format(minutes), "minutes")
    elif minutes == '0':
        print("Session duration: {}".format(hours), "hours")
    else:
        print("Session duration: {} hours {} minutes".format(hours, minutes))
        
    miliseconds = int(hours) * (3600 * 1000) + int(minutes) * (60 * 1000)

    for i in range(session):
        time.sleep(miliseconds)
        browser = webbrowser.get().open('https://www.youtube.com/watch?v=73NdmMYZsnM')

break_time()

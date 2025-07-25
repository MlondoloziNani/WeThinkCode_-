def main():
    time = convert(input("What time is it? "))

    if time >= 7.0 and time <= 8.0:
        print("breakfast time")
    elif time >= 12.0 and time <= 13.0:
        print("lunch time")
    elif time >= 18.0 and time <= 19.0:
        print("dinner time")
    else:
        return


def convert(time):
    time = time.split(":")
    minutes = float("0.".join(time[-1::]))/60
    return round(float(time[0]) + minutes, 2)


if __name__ == "__main__":
    main()

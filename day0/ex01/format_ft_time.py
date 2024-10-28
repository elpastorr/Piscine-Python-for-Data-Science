import time
import datetime


def main():
    print(f"Seconds since January 1, 1970: {time.time():,.4f} or \
{time.time():.2e} in scientific notation")
    print(datetime.date.today().strftime('%b %d %Y'))


if __name__ == "__main__":
    main()

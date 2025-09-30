from data_processing.file_reader import read_data
from data_processing.web_fetcher import fetch_user_data

def main():
    file_data = read_data("data.txt")
    print("Data from file:")
    for name, age in file_data:
        print(f"{name} is {age} years old.")

    print("\nFetching user data from web API...")
    user_data = fetch_user_data()
    print("Data from web:")
    for user in user_data:
        print(user)

if __name__ == "__main__":
    main()

import os
import json

def installRequirements():
    # FINISH ME:
    # This might not be needed if we pack into exe, but for those that use the github for this, here ya go
    os.system("pip install -r requirements.txt") # FIXME: the path issue might be annoying here

def main():
    # installRequirements()
    configPath = "Scripts/Config.json"
    config = {}
    with open(configPath, "r") as f:
        config = json.load(f)
        print("Config loaded from", configPath)

    settings = f"""    Location: {config["location-ZIP:"]}
    Username: {config["userName"]}
    WelcomeMessage: {config["displayWelcomeMessage"]}
    ScrapeFrequency: {config["scrapingFrequency"]}
    ListingsPerScrape: {config["listingsPerScrape"]}\n"""
    
    menu = """Settings:\n
- (Location) Edit your location, via ZIP or city, state.
- (Username) Edit your username.
- (WelcomeMessage) Set whether or not to display the welcome message at the start.
- (ScrapeFrequency) Set the frequency of data scraping in number of days between scrapes.
- (ListingsPerScrape) Set the number of listings to grab per scraper run.
- (Exit) To exit"""

    while True:
        os.system("clear" if os.name == "posix" else "cls")
        print(f"{'─'*50}")
        print(settings)
        print(f"{'─'*50}")
        print(menu, "\n\nEnter your choice")
        choice = input("> ").lower()
        if choice == "location" or choice == "1":
            # Edit location
            try:
                location = input("Enter your location: ")
                config["location-ZIP:"] = location
            except:
                print("Error: Invalid location input")
                config["location-ZIP:"] = "Las Cruses, NM"
        elif choice == "username" or choice == "2":
            # Edit username
            try:
                username = input("Enter your username: ")
                config["userName"] = username
            except:
                print("Error: Invalid username input")
                config["userName"] = "your_username_here"
        elif choice == "welcome message" or choice == "3" or choice == "welcome":
            # Toggle welcome message
            try:
                welcomeMessage = str(input("Would you like to display the welcome message (T/F): ")).lower()
                if welcomeMessage == "true" or welcomeMessage == "t":
                    welcomeMessage = True
                elif welcomeMessage == "false" or welcomeMessage == "f":
                    welcomeMessage = False
                config["displayWelcomeMessage"] = welcomeMessage
            except:
                print("Error: Invalid welcome message input")
                config["displayWelcomeMessage"] = False
        elif choice == "scrape frequency" or choice == "4":
            # Edit scraping frequency
            try:
                frequency = input("Enter the amount of days you would like between scheduled scrapes: ")
                config["scrapingFrequency"] = frequency
            except:
                print("Error: Invalid scrape frequency input")
                config["scrapingFrequency"] = 7
        elif choice == "listings per scrape" or choice == "5":
            # Edit listings per scrape
            try:
                listingsPerScrape = input("Enter how many listings you would like grabbed per scrape: ")
                config["listingsPerScrape"] = listingsPerScrape
            except:
                print("Error: Invalid listings per scrape input")
                config["listingsPerScrape"] = 10
        elif choice == "exit" or choice == "0":
            # Exit
            break
        else:
            print("Invalid choice. Please try again.")

    with open(configPath, "w") as f:
        json.dump(config, f, indent=4)
    return

if __name__ == "__main__":
    main()
import requests
import random
import string
import threading

url = 'https://www.vivoshoeuk.com/login.html?action=process'  # Scam Website
max_attempts = 5 # Max attempts
num_requests = 1000  # Number of requests to send
num_threads = 50 # Number of thread

counter_lock = threading.Lock()
counter = 0

def generate_random_name():
    boy_names = [
        "Liam", "Noah", "Oliver", "Elijah", "William", "James", "Benjamin", "Lucas", "Henry", "Alexander",
        "Mason", "Michael", "Ethan", "Daniel", "Jacob", "Logan", "Jackson", "Sebastian", "Jack", "Aiden",
        "Owen", "Samuel", "Matthew", "Joseph", "Levi", "Mateo", "David", "John", "Wyatt", "Carter",
        "Julian", "Luke", "Grayson", "Isaac", "Jayden", "Theodore", "Gabriel", "Anthony", "Dylan", "Leo",
        "Lincoln", "Jaxon", "Asher", "Christopher", "Josiah", "Andrew", "Thomas", "Joshua", "Ezra", "Hudson",
        "Charles", "Caleb", "Isaiah", "Ryan", "Nathan", "Adrian", "Christian", "Maverick", "Colton", "Elias",
        "Aaron", "Eli", "Landon", "Jonathan", "Nolan", "Hunter", "Cameron", "Connor", "Santiago", "Jeremiah",
        "Ezekiel", "Angel", "Roman", "Easton", "Miles", "Robert", "Jameson", "Nicholas", "Greyson", "Cooper",
        "Ian", "Carson", "Axel", "Jaxson", "Dominic", "Leonardo", "Luca", "Austin", "Jordan", "Adam",
        "Xavier", "Jose", "Jace", "Everett", "Declan", "Evan", "Kayden", "Parker", "Wesley", "Kai",
        "Brayden", "Bryson", "Weston", "Jason", "Emmett", "Sawyer", "Silas", "Bennett", "Brooks", "Micah",
        "Damian", "Harrison", "Waylon", "Ayden", "Vincent", "Ryder", "Kingston", "Rowan", "George", "Luis",
        "Chase", "Cole", "Nathaniel", "Zachary", "Ashton", "Braxton", "Gavin", "Tyler", "Diego", "Bentley",
        "Amir", "Beau", "Gael", "Carlos", "Ryker", "Jasper", "Max", "Juan", "Ivan", "Brandon", "Jonah",
        "Giovanni", "Kaiden", "Myles", "Calvin", "Lorenzo", "Maxwell", "Jayce", "Kevin", "Legend", "Tristan",
        "Jesus", "Jude", "Zion", "Justin", "Maddox", "Abel", "King", "Camden", "Elliott", "Malachi",
        "Milo", "Emmanuel", "Karter", "Rhett", "Alex", "August", "River", "Xander", "Antonio", "Brody",
        "Finn", "Elliot", "Dean", "Emiliano", "Eric", "Miguel", "Arthur", "Matteo", "Graham", "Alan",
        "Nicolas", "Blake", "Thiago", "Stephen", "Zayden", "Theo", "Judah", "Caden", "Royce", "Jake",
        "Asher", "Emilio", "Brooks", "Derrick", "Hugo", "Ronin", "Orlando", "Frank", "Johan", "Louis",
        "Avery", "Xzavier", "Curtis", "Alec", "Danny", "Scott", "Colby", "Conor", "Ellis", "Lukas",
        "Eugene", "Nelson", "Randy", "Keaton", "Reginald", "Gideon", "Zachariah", "Khalil", "Nikolai", "Hendrix",
        "Drew", "Terrance", "Sergio", "Marvin", "Ralph", "Quentin", "Eddie", "Ramon", "Frederick", "Maximus",
        "Jaxon", "Fernando", "Kristopher", "Dexter", "Dustin", "Brendan", "Bryce", "Terrence", "Brock", "Dallas",
        "Vance", "Colton", "Alijah", "Fletcher", "Cassius", "Ibrahim", "Dax", "Moises", "Ellis", "Raymond",
        "Darren", "Santino", "Carmelo", "Harold", "Keanu", "Kody", "Lawrence", "Mathias", "Zaiden", "Javion",
        "Harry", "Hakeem", "Osvaldo", "Konnor", "Alvaro", "Lewis", "Gustavo", "Darien", "Romeo", "Kamari",
        "Kamden", "Lucca", "Kohen", "Leonidas", "Jasiah", "Niko", "Gerald", "Reece", "Rodney", "Ronald",
        "Zachary", "Malcolm", "Brycen", "Tony", "Boston", "Edison", "Camron", "Terrell", "Allan", "Matias",
        "Yahir", "Dwayne", "Anakin", "Kellan", "Sheldon", "Harley", "Chris", "Lance", "Amos", "Alonso",
        "Jeffery", "Gunnar", "Gary", "Memphis", "Rudy", "Darian", "Giancarlo", "Roy", "Giovani", "Dominique",
        "Reynaldo", "Stanley", "Yosef", "Rex", "Ismael", "Beckham", "Jair", "Dayton", "Mathew", "Willie",
        "Isaias", "Justice", "Joziah", "Marlon", "Orion", "Jamarion", "Braeden", "Tate", "Armando", "Jon",
        "Sullivan", "Elisha", "Kolton", "Jax", "Tatum", "Maximilian", "Jimmy", "Ramon", "Kyler", "Dennis",
        "Nathanael", "Desmond", "Keegan", "Ezequiel", "Branson", "Kash", "Titan", "Camren", "Armani", "Asa",
        "Uriel", "Noel", "Daxton", "Talon", "Alfred", "Kieran", "Baylor", "Adrien", "Deandre", "Kingsley",
        "Valentino", "Jerry", "Izaiah", "Quinton", "Jeff"
    ]
    return random.choice(boy_names)

def generate_random_numbers():
    return ''.join(random.choices(string.digits, k=random.randint(3, 5)))

def generate_random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(8, 12)))

def generate_random_email():
    name = generate_random_name().lower()
    numbers = generate_random_numbers()
    return f"{name}{numbers}@gmail.com"

def make_request(email, password):
    global counter
    payload = {
        'email_address': email,
        'password': password
    }

    attempts = 0
    success = False

    while attempts < max_attempts:
        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()
            success = True
            break
        except requests.RequestException as e:
            print(f"Attempt {attempts+1} failed:", e)
            attempts += 1

    with counter_lock:
        counter += 1
        current_counter = counter

    if success:
        print(f"{email} and {password} sent. {current_counter}")
    else:
        print("Max attempts reached. Unable to complete the request.")

def make_requests_threaded():
    for _ in range(num_requests):
        email = generate_random_email()
        password = generate_random_password()
        make_request(email, password)

threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=make_requests_threaded)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All requests completed.")
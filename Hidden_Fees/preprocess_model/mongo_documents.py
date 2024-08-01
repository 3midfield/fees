from pymongo import MongoClient
import subprocess

def start_mongodb():
    try:
        # Command to start MongoDB (adjust as needed for your system)
        command = "brew services start mongodb/brew/mongodb-community"
        
        # Run the command as a background process
        subprocess.Popen(command, shell=True)
        
        print("MongoDB started successfully.")
    except Exception as e:
        print(f"An error occurred while starting MongoDB: {e}")
        
def stop_mongodb():
    try:
        # Command to stop MongoDB (this might vary depending on your system)
        command = "brew services stop mongodb/brew/mongodb-community"

        # Run the command
        subprocess.run(command, shell=True, check=True)

        print("MongoDB stopped successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while stopping MongoDB: {e}")


def add_to_mongo(recordkeeper, company_name, text):
    # Start MongoDB
    start_mongodb()

    client = MongoClient('localhost', 27017)

    db = client['***']
    collection = db['adp']
    document = {'Company': company_name, 'DocumentText': text}
    collection.insert_one(document)

    # List databases
    print(client.list_database_names())

    # List collections in the 'mydatabase' database
    print(db.list_collection_names())
    client.close()
    # Stop MongoDB
    stop_mongodb()
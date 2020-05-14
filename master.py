from helpers import valid_boolean_input
from config_controller import new_controller
from config_model import new_model
from config_model import build_attribute
from config_routes import new_routes
from mongoose_config import mongoose_db_config
from config_server import server_js


def backend_config():
    """ 
    docS -> The singular name of a MongoDb document (example: "user")
    docP -> The plural name of a MongoDb document (example: "users")
    """
    
    server_routes = []

    number_of_documents = int(input("How many documents would you like to add to your database? "))

    documents = []
    print("For each of your documents, please enter its singular and plural spellings, separated by a comma: (for example: user, users)")
    
    for i in range(1, number_of_documents + 1):
        while True:
            docNames = input(f"Document: {i} - singular and plural spellings: ")
            docNames = docNames.split(",")
            try:
                docS, docP = docNames[0].strip(), docNames[1].strip()
                if docS == "" or docP == "":
                    raise IndexError
                documents.append( (docS, docP) )            
            except IndexError:
                print("Oops, please try that again.")
                continue
            break


    for document in documents:
        docS, docP = document[0], document[1]

        attributes = []
        while True:
            if len(attributes) == 0:
                ans = input(f"Y/n - Would you like to add attributes to {docS.capitalize()} model? " )
                if valid_boolean_input(ans) == "error":
                    print("Oops, please enter a valid response. ")
                    continue
                elif not valid_boolean_input(ans):
                    break
                attributes.append(build_attribute())
                continue
            
            add = input("Y/n - Add another attribute? ")
            if valid_boolean_input(add) == "error":
                print("Oops, please enter a valid response. ")
                continue
            elif not valid_boolean_input(add):
                break
            attributes.append(build_attribute())

        # print(attributes)

        # Create new docS.model.js file:
        f = open(f"./server/models/{docS}.model.js", "x")
        f.writelines(new_model(docS, docP, attributes))
        f.close()

        # Create new docS.controller.js file:
        f = open(f"./server/controllers/{docS}.controller.js", "x")
        f.writelines([line + "\n" for line in new_controller(docS, docP, attributes)])
        f.close()

        # Create a new docS.routes.js file:
        f = open(f"./server/routes/{docS}.routes.js", "x")
        f.writelines([line + "\n" for line in new_routes(docS, docP)])
        f.close()

        server_routes.append(f"require(\"./server/routes/{docS}.routes\")(app);")

    # build server.js
    port = int(input("Which port are you using? "))
    mongoose_db_config()
    f = open(f"./server.js", "x")
    f.writelines([line + "\n" for line in server_js(server_routes, port)])
    f.close()

    print()
    print("Express and Mongoose are configured. Hack away!")
    print()

backend_config()

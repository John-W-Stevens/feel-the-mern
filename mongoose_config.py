

def mongoose_config_js(db_name, update_validations):
    lines = [
       "const mongoose = require(\"mongoose\")",
       "",
       "// this line enables validators to run on update",
       f"mongoose.set(\"runValidators\", {update_validations});",
       "",
       f"mongoose.connect(\"mongodb://localhost/{db_name}\", "+"{",
       "    useNewUrlParser: true,",
       "    useUnifiedTopology: true,",
       "})",
       "    .then(() => console.log(\"Database connection established\"))",
       "    .catch(err => console.log(\"There was an error\", err))",
    ]
    return lines


def mongoose_db_config():
    db_name = input("What database are you using? ")
    update_validations = input("Y/n - Do you want to run validations on update? ")

    if update_validations == "Y" or update_validations == "y":
        update_validations = "true"
    else:
        update_validations = "false"

    f = open(f"./server/config/mongoose.config.js", "x")
    f.writelines([line + "\n" for line in mongoose_config_js(db_name, update_validations)])
    f.close()

    print("Your database is rip-roaring and ready to go.")


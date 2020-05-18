def build_attribute():
    """
    Input:
        docS -> Singular spelling of document name (ex: "user" )
        docP -> Plural spelling of coudment name (ex: "users" )
    """

    def valid_boolean_input(response):
        x = response.lower().strip()
        if x in ["true", "yes", "y"]: 
            return True
        if x in ["false", "no", "n"]: 
            return False
        else: 
            return "error"

    def configure_string_validator(validator):

        is_boolean = validator in ["lowercase", "uppercase", "trim",]

        if is_boolean:
            error = ""
            while True:
                if validator == "lowercase":
                    arg = input("Y/n - Always call .toLowerCase() on the value? ")
                
                elif validator == "uppercase":
                    arg = input("Y/n - Always call .toUpperCase() on the value? ")

                elif validator == "trim":
                    arg = input("Y/n - Always call .trim() on the value? ")
                
                arg = valid_boolean_input(arg)
                if arg == "error":
                    print("Oops, please input a valid response.")
                    continue
                else:
                    return arg, error
                
        while True:

            if validator == "enum":
                arg = input("Please enter all values separated by commas. (ex: dog, cat, fish)")
                arg = arg.split(",").strip()

            elif validator == "match":
                arg = input("Please enter your regex: ")
            
            elif validator == "minLength":
                arg = input("Please enter minimum length: ")

            elif validator == "maxLength":
                arg = input("Please enter maximum length: ")

            approval = input(f"Y/n - you entered {arg} as an argument for the {validator} validator. Save this? ")
            if valid_boolean_input(approval):
                break
        
        while True:
            error = input("Please enter the error message you want displayed if this validator returns false: ")
            approved = input(f"Y/n - You entered {error} as your error message. Save this? ")
            if valid_boolean_input(approved):
                break
            
        return arg, error

    def configure_number_validator(validator):

        while True:

            if validator == "enum":
                arg = input("Please enter all values separated by commas. (ex: 45, 83, 109)")
                arg = arg.split(",").strip()
                arg1 = [int(n) for n in arg]
                arg = arg1
            
            elif validator == "min":
                arg = input("Please enter minimum value: ")

            elif validator == "max":
                arg = input("Please enter maximum value: ")

            approval = input(f"Y/n - you entered {arg} as an argument for the {validator} validator. Save this? ")
            if valid_boolean_input(approval):
                break
        
        if validator == "min" or validator == "max":
            arg = int(arg)

        while True:
            error = input("Please enter the error message you want displayed if this validator returns false: ")
            approved = input(f"Y/n - You entered {error} as your error message. Save this? ")
            if valid_boolean_input(approved):
                break
            
        return arg, error

    # These are all the valid mongoose schema types:
    schema_types = {
        "String": "string",
        "Number": "number",
        "Date": "date",
        "Buffer": "buffer",
        "Boolean": "boolean",
        "Mixed": "mixed",
        "ObjectId": "ObjectId",
        "Array": "array",
        "Decimal128": "decimal128",
        "Map": "map"
    }

    string_validators = ["lowercase", "uppercase", "trim", "enum", "match", "minlength", "maxlength"]
    number_validators = ["min", "max"]

    attribute = {
        "label": "",
        "type": "",
        "required": "", # True/False
        "required_error_message": "",
        "use_validations": "", # True/False
        "validations": []
    }

    while True:
        label = input("What is this attribute called? (ex: name) ")
        app = input(f"Y/n - You selected '{label}' for this attribute's label. Is this correct? ")
        if valid_boolean_input(app):
            attribute["label"] = label
            break

    print(f"Choose one of the following mongoose schema types: {[k for k in schema_types.keys()]} ")
    schema_type = ""
    schema_approved = False

    while schema_type not in schema_types and not schema_approved:
        schema_type = input(f"What is the SchemaType? ")
        if schema_type not in schema_types:
            print("Oops, please enter a valid schema.")
            continue
        approved = input(f"Y/n - You selected the {schema_type} schema. Is this correct? ")
        if valid_boolean_input(approved):
            schema_approved = True
            attribute["type"] = schema_type

    required = "unset"
    while required == "unset":
        response = input("Y/n - Is this a required field? ")
        if valid_boolean_input(response) == "error":
            continue
        else: 
            required = valid_boolean_input(response)
            attribute["required"] = required
            if required:
                attribute["required_error_message"] = f"{attribute['label']} is required."
                ans = input(f"Y/n - The error message for 'required' property is {attribute['required_error_message']} Would you like to change it? ")
                if valid_boolean_input(ans):
                    approved = False
                    while not approved:
                        error_msg = input("Please enter your error message. ")
                        x = input(f"Y/n - Your error message is: {error_msg} Save this? ")
                        if valid_boolean_input(x):
                            approved = True
                            attribute["required_error_message"] = error_msg
    
    if attribute["type"] == "String" or attribute["type"] == "Number":


        while True:
            validations = input("Y/n - Would you like to add validations? ")
            if valid_boolean_input(validations) == "error":
                continue
            else:
                attribute["use_validations"] = valid_boolean_input(validations)
                break

        if attribute["use_validations"]:
            schema_type = attribute["type"]
            if schema_type == "String":
                available_validators = string_validators
            else:
                available_validators = number_validators

            print(f"Mongoose's {schema_type} SchemaType has the following available built-in validations: {available_validators}")
            adding_validators = True
            while adding_validators:
                validator = ""
                while True:
                    v = input("Please select a validator: ")
                    if v in available_validators:
                        ans = input(f"Y/n - You selected the {v} validator. Is this correct? ")
                        if valid_boolean_input(ans):
                            validator = v
                            break
                    else:
                        print("Oops, please select a valid validator.")
                
                if attribute["type"] == "String":
                    arg, error = configure_string_validator(validator)
                elif attribute["type"] == "Number":
                    arg, error = configure_number_validator(validator)

                attribute["validations"].append( [validator, arg, error] )
                add_another = input("Y/n - would you like to add another validator? ")
                
                if not valid_boolean_input(add_another):
                    break    

    return attribute






def new_model(docS, docP, attributes):
    lines = [
        f"const mongoose = require(\"mongoose\");\n",
        "\n",
        f"const {docS.capitalize()}Schema = new mongoose.Schema("+"{\n",]

    for a in attributes:
        lines.append(f"    {a['label']}: " +"{\n")
        lines.append(f"        type: {a['type']},\n")
        if a['required'] == True:
            lines.append("        required: [\n")
            lines.append(f"            true,\n")
            lines.append(f"            \"{a['required_error_message']}\"\n")
            lines.append("        ],\n")
        if a["use_validations"]:
            for v in a["validations"]:
                lines.append(f"        {v[0]}: [\n")
                if v[1] == True:
                    lines.append(f"            true,\n")
                    lines.append("         ],\n")
                # elif v[1] == False:
                #     lines.append(f"            false,\n")
                #     lines.append("         ],\n")
                else:             
                    lines.append(f"            {v[1]},\n")
                    lines.append(f"            \"{v[2]}\",\n")
                    lines.append("         ],\n")
        lines.append("    },\n")

    lines.append("}, {timestamps: true});\n")
    lines.append(f"module.exports.{docS.capitalize()} = mongoose.model(\"{docS.capitalize()}\", {docS.capitalize()}Schema)\n")

    return lines
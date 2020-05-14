
def new_controller(docS, docP, attributes):

    attr = ",".join([a['label'] for a in attributes])

    lines = [
       "const {"+f" {docS.capitalize() }"+"}"+f" = require(\"../models/{docS}.model\")",
       "",
       f"// CRUD Operations for {docS} Document",
       "",
       f"// Get All {docP}: READ",
       f"module.exports.findAll{docP.capitalize()} = (request, response) => "+"{",
       f"    {docS.capitalize()}.find()",
       f"        .then(all{docP.capitalize()} => response.json("+"{"+f"{docP.capitalize()}: all{docP.capitalize()}"+"}"+"))",
       "        .catch(err => response.json("+"{ message: \"Something went wrong\", error: err}))",
       "};",
       "",
       f"// Get a Single {docS.capitalize()}: READ",
       f"module.exports.findOneSingle{docS.capitalize()} = (request, response) => "+"{",
       f"    {docS.capitalize()}.find("+"{"+"_id: request.params.id})",
       f"        .then(oneSingle{docS.capitalize()} => response.json("+"{"+f" {docS.capitalize()}: oneSingle{docS.capitalize()}"+"}))",
       "        .catch(err => response.json({ message: \"Something went wrong\", error: err}));",
       "};",
       "",
       f"// Create a {docS.capitalize()}: CREATE",
       f"module.exports.create{docS.capitalize()} = (request, response) => "+"{",
       f"    // CHANGE THIS TO REFLECT THE PROPERTIES BELONGING TO {docS}",
       "    const {"+ f"{ attr }" +"} = request.body;",
       f"    {docS.capitalize()}.create("+"{",]


    for a in attributes:
       lines.append(f"        {a['label']},")
       
    lines1 = [
       "    })",
       f"        .then({docS.capitalize()} => response.json({docS.capitalize()}))",
       "        .catch(err => response.status(400).json(err))",
       "};",
       "",
       f"// Update a {docS.capitalize()}: UPDATE",
       f"module.exports.update{docS.capitalize()} = (request, response) => "+"{",
       f"    {docS.capitalize()}.findOneAndUpdate("+"{"+"_id: request.params.id}, request.body, "+"{"+"new:true})",
       f"        .then(updated{docS.capitalize()} => response.json(updated{docS.capitalize()}))",
       "        .catch(error => response.status(400).json(error))",
       "}",
       "",
       f"// Delete a {docS.capitalize()}: DELETE",
       f"module.exports.delete{docS.capitalize()} = (request, response) => "+"{",
       f"    {docS.capitalize()}.deleteOne("+"{"+"_id: request.params.id})",
       "        .then(deleteConfirmation => response.json(deleteConfirmation))",
       "        .catch(error => response.json(error))",
       "}",
    ]
    return lines + lines1
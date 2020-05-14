
def new_routes(docS, docP):
    lines = [
       f"const {docS.capitalize()}Controller = require(\"../controllers/{docS}.controller\");",
       "",
       "module.exports = function(app){",
       f"    app.get(\"/api/{docP}\", {docS.capitalize()}Controller.findAll{docP.capitalize()});",
       f"    app.post(\"/api/{docS}\", {docS.capitalize()}Controller.create{docS.capitalize()});",
       f"    app.get(\"/api/{docS}/:id\", {docS.capitalize()}Controller.findOneSingle{docS.capitalize()});",
       f"    app.put(\"/api/{docS}/:id\", {docS.capitalize()}Controller.update{docS.capitalize()});",
       f"    app.delete(\"/api/{docS}/:id\", {docS.capitalize()}Controller.delete{docS.capitalize()});",
       "}",
    ]
    return lines

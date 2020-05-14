
def server_js(routes, port):
    lines = [
       "const express = require(\"express\")",
       "const cors = require(\"cors\");",
       "const app = express()",
       f"const port = {port}",
       "",
       "require(\"./server/config/mongoose.config\");",
       "",
       "app.use(cors())",
       "app.use(express.json())",
       "app.use(express.urlencoded("+"{"+"extended: true}))",
       "",
       "// Routes must come afer the lines above:"]

    for route in routes:
        lines.append(route)

    lines.append("")
    lines.append(f"app.listen({port}, ()=>console.log(\"The server is all fired up and listening on port {port}\"))")

    return lines
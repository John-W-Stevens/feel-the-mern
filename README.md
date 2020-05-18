Feel the MERN (FTM) - A CLI for quickly launching a MERN project

Quickstart:
<<<<<<< HEAD
- FTM requires Python3, ttab, and Mongodb to be installed
=======
- FTM requires Python3, ttab, node, nodemon, and Mongodb to be installed
>>>>>>> b7022c74039a4d377d42f1e1b635ab92cce09198
- clone the repo into your root folder (git@github.com:John-W-Stevens/feel-the-mern.git) (Read below if you want to put it somewhere else)
- Add all three zsh functions below to your ~/.zshrc file (assuming you are using zsh, otherwise add them to your bash profile)
- Create an empty project directory and navigate into it
- Run: feel-the-mern

What is it? FTM is bascially a collection of zsh commands wrapped in a single function
that, when invoked, walks the user through the intial setup of a MERN application. From the
command line a user can create an instance of Mongodb, and customize it by adding documents 
with full CRUD functionality. Users can create as many documents as they wish and customize them 
<<<<<<< HEAD
by adding attributes and validations. Currently, only the mongoose 'String' and 'Number' SchemaTypes
support the use of built-in validations.
=======
by adding attributes and validations. Currently, FTM only supports the use of built-in validations for 
the mongoose 'String' and 'Number' SchemaTypes.
>>>>>>> b7022c74039a4d377d42f1e1b635ab92cce09198

After server-side configuration is completed the following file structure is the result:

project_directory:

    server
        config
            - mongoose.config.js
        controllers
            - doc_name.controller.js (for each doc specified)
        models
            - doc_name.model.js (for each doc specified)
        routes
            - doc_name.routes.js (for each doc specified)
    server.js

After configuring the server FTM moves on to the client.

An initial React app is created inside a folder called 'client' 
FTM pulls in axios, @reach/router, and bootstrap.css and then removes the following files
from client/src ( App.css, the logo, App.test.js,logo.svg ). It also adds two empty directories to src: /views and /components

At this point, FTM launches the server by running: { nodemon server.js } in a new terminal tab (using ttab) and the client by running: { npm run start }

Requirments for running this program:
- Python3: (all the underlying scripts are written in Python3 and FTM will call Python3 to run them)
- ttab: (necessary to launch server and client at the end, install with { npm install -g ttab } )
<<<<<<< HEAD
=======
- nodemon: (necessary to launch server at the end, install with { npm install -g nodemon } )
>>>>>>> b7022c74039a4d377d42f1e1b635ab92cce09198
- zsh: I use macOS and, after switching to Catalina 10.15.4, have zsh as my default shell. I think all the commands can be run with bash as well
  so you should be able to added them to your bash profile. The following functions are saved in my ~/.zshrc file:

##### THE FUNCTIONS BELOW NEED TO BE ADDED TO ./zshrc

<<<<<<< HEAD
setup-server(){
	git init
	npm init -y
	npm install mongoose express cors
	mkdir server
	mkdir server/config
	mkdir server/controllers
	mkdir server/models
	mkdir server/routes
	cp ~/feel-the-mern/config_controller.py ./
	cp ~/feel-the-mern/config_model.py ./
	cp ~/feel-the-mern/config_routes.py ./
	cp ~/feel-the-mern/config_server.py ./
	cp ~/feel-the-mern/helpers.py ./
	cp ~/feel-the-mern/master.py ./
	cp ~/feel-the-mern/mongoose_config.py ./
	python3 master.py
	rm -rf config_controller.py
	rm -rf config_model.py
	rm -rf config_routes.py
	rm -rf config_server.py
	rm -rf helpers.py
	rm -rf master.py
	rm -rf mongoose_config.py
}
setup-client(){
	npx create-react-app client
	npm --prefix ./client install axios @reach/router
	mkdir client/src/components
	mkdir client/src/views
	cp ~/feel-the-mern/bootstrap.css client/src
	rm client/src/App.css
	rm client/src/logo.svg
	rm client/src/App.test.js
	rm client/src/App.js
	cp ~/feel-the-mern/App.js client/src
	code .
}

feel-the-mern(){
	setup-server
	setup-client
	ttab nodemon server.js
	cd client
	npm run start
}

##### THE FUNCTIONS ABOVE NEED TO BE ADDED TO ./zshrc
=======
	setup-server(){
		git init
		npm init -y
		npm install mongoose express cors
		mkdir server
		mkdir server/config
		mkdir server/controllers
		mkdir server/models
		mkdir server/routes
		cp ~/feel-the-mern/config_controller.py ./
		cp ~/feel-the-mern/config_model.py ./
		cp ~/feel-the-mern/config_routes.py ./
		cp ~/feel-the-mern/config_server.py ./
		cp ~/feel-the-mern/helpers.py ./
		cp ~/feel-the-mern/master.py ./
		cp ~/feel-the-mern/mongoose_config.py ./
		python3 master.py
		rm -rf config_controller.py
		rm -rf config_model.py
		rm -rf config_routes.py
		rm -rf config_server.py
		rm -rf helpers.py
		rm -rf master.py
		rm -rf mongoose_config.py
	}
	
	setup-client(){
		npx create-react-app client
		npm --prefix ./client install axios @reach/router
		mkdir client/src/components
		mkdir client/src/views
		cp ~/feel-the-mern/bootstrap.css client/src
		rm client/src/App.css
		rm client/src/logo.svg
		rm client/src/App.test.js
		rm client/src/App.js
		cp ~/feel-the-mern/App.js client/src
		code .
	}

	feel-the-mern(){
		setup-server
		setup-client
		ttab nodemon server.js
		cd client
		npm run start
	}
>>>>>>> b7022c74039a4d377d42f1e1b635ab92cce09198

After adding these functions, run: { source ~/.zshrc } (or the equivilent for bash)

As you can see from the zsh functions, FTM will look for scripts in ~/feel-the-mern
I put them there so I can use them every time I start a project. You can of course put these files wherever you want
<<<<<<< HEAD
provided you change the paths in the zsh functions.
=======
provided you change the paths in the zsh functions. 

This is a work in progress!
>>>>>>> b7022c74039a4d377d42f1e1b635ab92cce09198


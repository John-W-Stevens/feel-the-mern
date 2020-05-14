
What is it? A CLI that offer a quick and convenient way to launch a MERN project.

This is a work in progress, though it functions well for simple projects.

Create an 


How to use it:
- clone the repo into your root folder (git@github.com:John-W-Stevens/feel-the-mern.git)
- add the lines below to your .zshrc file (make sure to save and the run: source ~/.zshrc)
	- You need ttab for this to launch (npm install -g ttab)
	- This will not work properly unless you have python3 and mongodb installed
- create an empty project directory and cd into it
- once inside your project directory run: feel-the-mern

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
	code .
	nodemon server.js
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
};








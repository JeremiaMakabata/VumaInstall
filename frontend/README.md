
# Local Setup

Python 3 and [pip3](mornally pre installed on a UNIX OS) need to already be installed. 

Clone the repo to your computer. It is advisable to have git and clone using  git clone <repo url>

```
$ cd ~/PATH_ON_LOCAL
$ git clone https://github.com/JeremiaMakabata/VumaInstall.git
$ cd VumaInstall
```

## Backend
For this part you will need to activate your virtual environment:  
Install the `python package: Recommended pip and conda` (https://docs.anaconda.com/anaconda/install/, https://pip.pypa.io/en/stable/installing/) to run the project, then create an empty `Virtual evnvironment`. Then `cd` into the `backend` directory and run migrations.

```
$ cd backend
install  requirements.txt: 
$ pip install -r requirements.txt or conda install --yes --file requirements.txt
activate the visrtial enviromnet
$ python manage.py makemigrations && python manage.py migrate
(venv) $python manage.py runserver
```

You can see the API now at [http://127.0.0.1:8000/api/request](http://127.0.0.1:8000/api/request).

## Frontend

Open up a new command line console so there are now **two** open. Navigate to the `frontend` directory.

```
$ cd ~/PATH_ON_LOCAL
$ 
$ cd VumaInstall/frontend
```

Make sure React is already installed globally. If not `$ npm install -g create-react-app`.

Then install necessary packages and start the React server:

```
$ npm install
$ npm start
```
NB: it is recommended to create a super user for the django app, you can do this by navigating to the frontend directory: 
```
(venv) $ cd ~/PATH_ON_LOCAL/VumaInstall/frontend
(venv) $ python manage.py createsuperuser
(venv) $ python manage.py runserver
```

Navigate to [http://localhost:3000/](http://localhost:3000/) to see a list of our DRF backend content outputted using React.


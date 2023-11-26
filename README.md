# chess-trainer-application

## How to start development
The Application is structured into a VueJS Frontend and a FastAPI (Python) Backend.
### Starting the Backend
1. Create a virtual environment (https://docs.python.org/3/tutorial/venv.html)
2. Use the virtual environment with "source virtualenvName/bin/activate"
3. Navigate into /chess-trainer-application-backend and run "pip install -r requirements.txt". This will install all the backend dependencies inside your virtual environment.
4. Run "uvicorn main:app" to start the Server.
### Starting the Frontend
1. Navigate into /chess-trainer-application-frontend and run "npm install".
2. To start the development server run "npm run dev".
3. The Frontend currently makes it's API calls to 'http://127.0.0.1:8000'. E.g. in ChessboardView.vue. If your uvicorn Server is running on a different port than 8000, you need to adjust this code.

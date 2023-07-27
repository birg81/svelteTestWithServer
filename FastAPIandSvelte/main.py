import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Abilita Richieste CORS
app.add_middleware(
	CORSMiddleware,
	allow_credentials = True,
	allow_methods = ['GET', 'POST', 'PUT', 'DELETE'],
	allow_headers = ['*'],
	allow_origins = [
		'http://localhost:3000',
		'http://localhost:4000',
		'http://localhost:5000',
	],
)

# Base di dati
people = [
	{
		'firstname': 'Anna',
		'lastname': 'Cuomo',
		'gender': 'female'
	},	{
		'firstname': 'Barbara',
		'lastname': 'De Riao',
		'gender': 'female'
	},	{
		'firstname': 'Chiara',
		'lastname': 'Di Maio',
		'gender': 'female'
	},	{
		'firstname': 'Daniela',
		'lastname': 'Simeone',
		'gender': 'female'
	},	{
		'firstname': 'Eleonora',
		'lastname': 'Cimmino',
		'gender': 'female'
	}
]

@app.get('/api/people')
async def getPeople():
	return people

@app.get('/api/people/{id}')
async def getPerson(id: int):
	return people[id]

# Codice di avvio dell'app FastAPI con Uvicorn
if __name__ == '__main__':
	uvicorn.run(
		'main:app',
		host = '0.0.0.0',
		port = 4000,
		use_colors = True,
		http = 'httptools',
		reload = True,
	)
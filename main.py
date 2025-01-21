from fastapi import FastAPI

app = FastAPI()

# Sample data for demonstration purposes
data = {
    "USA": {"New York": {}, "Los Angeles": {}},
    "France": {"Paris": {}, "Lyon": {}},
    "Spain": {"Madrid": {}, "Barcelona": {}}
}

# Create a new route that exposes the cities of a country:
@app.get('/countries/{country}')
def cities(country: str):
    return list(data[country].keys())


<p align="center">
  <a href="https://bhagavadgita.io">
    <img src="gita.png" alt="Logo" width="300">
  </a>

  <h3 align="center">Bhagavad Gita API v2</h3>

  <p align="center">
    Code for the BhagavadGita.io v2 API, which is an app built for Gita readers by Gita readers.
    <br />
    <br />
    <a href="https://bhagavadgita.io">View Demo</a>
    ·
    <a href="https://github.com/gita/bhagavadgita-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/gita/bhagavadgita-api/issues">Request Feature</a>
  </p>
</p>

<p align="center">
  <a href="https://github.com/gita/bhagavad-gita-api/blob/master/LICENSE">
    <img alt="LICENSE" src="https://img.shields.io/badge/License-MIT-yellow.svg?maxAge=43200">
  </a>
  <a href="https://starcharts.herokuapp.com/gita/bhagavad-gita-api"><img alt="Stars" src="https://img.shields.io/github/stars/gita/bhagavad-gita-api.svg?style=social"></a>
</p>


## Project Structure
```
.
├── LICENSE
├── README.md
├── app
│   ├── __init__.py
│   ├── config.env
│   ├── config.py
│   ├── main.py
│   ├── models.py
│   └── utils.py
├── docker
│   └── Dockerfile
├── docker-compose-dev.yml
├── docker-compose.yml
├── letsencrypt
│   └── bhagavadgita.json
├── requirements.txt
└── run.py
```

## Developing Locally

1. Fork this repository and clone the forked repository.
2. Create and activate a Python 3 virtualenv.
3. Use `pip install -r requirements.txt` to install the requirements.
4. `python manage.py runserver` to start the server.
5. API can be accessed at `http://127.0.0.1:5000`.

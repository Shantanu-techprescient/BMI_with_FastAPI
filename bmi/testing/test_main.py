from fastapi.testclient import TestClient
import main
import requests
import sqlite3
import pytest
from router import user
from models import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from router.user import get_db, router

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

models.Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


#main.app.router.dependency_overrides[get_db] = override_get_db

client = TestClient(main.app)


@pytest.fixture
def setup_database():
    """ Fixture to set up the in-memory database with test data """
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE test_bmi_data (
        name VARCHAR(20) NOT NULL,
        age_yr INTEGER NOT NULL CHECK (age_yr>12),
        height_cm NUMERIC(4, 2) NOT NULL CHECK (age_yr>=152.40),
        weight_kg NUMERIC(4, 2) NOT NULL CHECK (age_yr>=45.50),
        bmi NUMERIC(3, 2) NOT NULL,
        PRIMARY KEY (name)
        )''')
    yield conn


session = setup_database

test_height_weight = {
    "age_yr": 15,
    "weight_kg": 40,
    "height_cm": 100,
    "name": "shan"
}

response_height_weight = {
    "detail": [
        {
            "loc": [
                "body",
                "weight_kg"
            ],
            "msg": "Weight should be greater than 45.50 kg",
            "type": "value_error"
        },
        {
            "loc": [
                "body",
                "height_cm"
            ],
            "msg": "Height should be greater than 152.40 cms",
            "type": "value_error"
        }
    ]
}
already_registered = {
    "age_yr": 22,
    "weight_kg": 60,
    "height_cm": 170,
    "name": "aadish"
}

response_already_registred = {'detail': 'User Already Registered'}

header = {'Authorization': 'bearer shantanu'}


def test_calculate_bmi():
    response = client.post("/bmi/", data=test_height_weight)  # without authentication
    assert response.json() == {"detail": "Not authenticated"}
    response = client.post("/bmi/", data=test_height_weight, headers=header)  # invalid height & weight
    assert response.json() == response_height_weight
    response = client.post("/bmi/", data=already_registered, headers=header)  # already registered
    assert response.json() == {"name": "akon"}


'''
def test_connection(session):
    # Test to make sure that there are 2 items in the database
    assert len(list(session.execute('SELECT * FROM test_bmi_data'))) == 0

'''

# Crypto Exchange API
### This API was developed to be used as a cryptocurrency exchange
### You can get the exchange rate of two currencies and buy cryptocurrencies with a debit/credit card
Note: This API is only for educational purpose, not real money is being traded.

## Setup
### This API was developed with the followin stack:
* FastAPI
* PonyORM
* PostgreSQL
```
virtualenv venv
source venv/bin/activate
python -m scripts.migrator
uvicorn main:app --reload
```

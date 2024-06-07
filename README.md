# freshgrade-ml-service
## Create new virtual environment
```
python3 -m venv env
```
## Activate virtual environment
```
// windows
.\env\Scripts\activate

// linux
source env/bin/activate
```
## Install dependencies
```
pip install -r requirements.txt
```
## Create environment variable
```
cp .env.dev.example .env
```
> adjust the value based on your saved machine learning model directory
## Run application
```
python3 app.py
```
> Note: for better supports and services please run in linux/ubuntu etc environment

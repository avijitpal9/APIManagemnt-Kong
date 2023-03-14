# APIManagemnt-Kong
API Management Using Kong

#### Install Kong on MAC
- brew tap kong/kong
- brew install kong
 - Kong Install Path on MAC 
    * /usr/local/Cellar/kong/3.1.1/
    * /usr/local/opt/kong

#### Kong Basic Commands
- kong health : To check Kong status
- kong start -c kong.conf : To start Kong API Gateway
- kong restart -c kong.conf : To restart Kong
- kong stop : To stop kong
- kong config init : Generate a default kong.yml with declarative configuration
- kong config parse kong.yml : Parse Kong declarative configuration
- kong check kong.conf : Check Kong configuration

#### Setup Applications
- Setup python3 virtual environment
  * python3 -m venv .venv
  * source .venv/bin/activate
  * pip install --upgrade pip wheel setuptools
  * pip install -r requirements.txt

- Start Applications  
  * flask --app calc_api/src/sumV1/app.py run --port=5001  
  * flask --app calc_api/src/sumV2/app.py run --port=5002  
  * flask --app calc_api/src/divV1/app.py run --port=6001


#### Ordering
- load-balancing
- key-authentication
- ip-restriction
- acl
- rate-limiting
- response-transformer


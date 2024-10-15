## Install Deps
```sh
npm install
```

## Start Server
```sh
npm start
```

## Run Postgres Server
```sh
docker compose up
```

## Connect to client
```sh
psql postgresql://postgres:password@localhost:5432/study-sync
```

## Create PSQL Schema
```sh
psql study-sync < sql/schema.sql -h localhost -U postgres
```

## Import Data
```sh
psql study-sync < sql/seed.sql -h localhost -U postgres
```

### Manual Install if you don't have to do the virtual enviroment (optional)
```sh
pip install virtualenv
virtualenv -p python3.11 ~/myenv
source ~/myenv/bin/activate

git clone https://github.com/aws/aws-elastic-beanstalk-cli-setup.git
python ./aws-elastic-beanstalk-cli-setup/scripts/ebcli_installer.py
echo 'export PATH="/home/gitpod/.ebcli-virtual-env/executables:$PATH"' >> ~/.bash_profile && source ~/.bash_profile
```

## EB initialization
```sh
eb init
```

## Set CodeSource
```sh
eb codesource
```
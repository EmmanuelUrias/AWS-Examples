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
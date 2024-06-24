## Create bucket
```sh
aws s3api create-bucket --bucket cse-practice1
```
## Run the SDK Ruby script
```sh
bundle exec ruby encrypt.rb
```
## Clean up
```sh
aws s3 rm s3://cse-practice1 --recursive
aws s3 rb s3://cse-practice1
```

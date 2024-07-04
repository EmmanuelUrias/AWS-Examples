# Get caller identity
```sh
aws sts get-caller-identity
```

# Get caller identity with a endpoint url to override default url with endpoint url
```sh
aws sts get-caller-identity --endpoint-url https://sts.us-west-1.amazonaws.com
```
This should throw an error

# Get caller identity with a endpoint url with region
```sh
aws sts get-caller-identity --region us-west-1 --endpoint-url https://sts.us-west-1.amazonaws.com
```
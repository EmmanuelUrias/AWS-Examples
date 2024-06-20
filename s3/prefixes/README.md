# Create a bucket
```sh
aws s3 mb s3://prefixes-are-fun-eu
```

# Create a folder
```
aws s3api put-object --bucket prefixes-are-fun-eu --key folder/
```

# Create many folders
```
aws s3api put-object --bucket prefixes-are-fun-eu --key folder/anotherfolder/athirdfolder/morefolders/file.txt --body file.txt
```

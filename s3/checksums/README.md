## Create an s3 bucket

```
aws s3 mb s3://checksum-demo-bucket223
```

## Create a file that we will do a checksum on

```
echo "Hello world" > myChecksumfile.txt
```

## Get a checksum of a file for md5


```
md5sum myChecksumfile.txt
```
#### f0ef7081e1539ac00ef5b761b4fb01b3 myChecksumfile.txt

## Upload our file to bucket and look at etag

```
aws s3api put-object --bucket checksum-demo-bucket223 --key myChecksumfile.txt
```

##  Upload file with a different checksum

```sh
sudo apt install rhash -y
rhash --crc32 --simple myChecksumfile.txt
```

```sh
aws s3api put-object \
--bucket checksum-demo-bucket223 \
--key myChecksumfilecrc32.txt \
--body myChecksumfile.txt \
--checksum-algorithm="CRC32" \
--checksum-crc32="b739e0d5"
```
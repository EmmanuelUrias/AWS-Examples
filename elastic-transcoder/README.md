# Make content bucket
```sh
aws s3api create-bucket --bucket videos-example-bucket-223
aws s3api create-bucket --bucket src-videos-example-bucket-223

aws s3api put-object --bucket videos-example-bucket-223 --key App2Container.mp4 --body App2Container.mp4
```

# Create a pipeline
```sh
aws elastictranscoder create-pipeline \
--name my-pipeline \
--input-bucket src-videos-example-bucket-223 \
--role arn:aws:iam::099001967703:role/Elastic_Transcoder_Default_Role \
--content-config file://content-config.json \
--thumbnail-config file://thumbnail-config.json
```

# Create a job
```sh
aws elastictranscoder create-job \
--pipeline-id 1721156962570-6fgnro \
--inputs file://inputs.json \
--outputs file://outputs.json \
--output-key-prefix "videos/" \
--user-metadata file://user-metadata.json
```

# Job details
```sh
aws elastictranscoder read-job --id 1721157778405-mcm4kb
```
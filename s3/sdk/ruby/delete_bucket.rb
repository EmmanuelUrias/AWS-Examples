require 'aws-sdk-s3'
require 'pry'
require 'securerandom'

# Retrieve the bucket name from the environment variable 'BUCKET_NAME'
bucket_name = ENV['BUCKET_NAME']

# Initialize an S3 client
client = Aws::S3::Client.new

# Function to delete all objects in the bucket
def empty_bucket(client, bucket_name)
  # List and delete all objects
  client.list_objects_v2(bucket: bucket_name).contents.each do |object|
    client.delete_object(bucket: bucket_name, key: object.key)
    puts "Deleted object: #{object.key}"

  rescue Aws::S3::Errors::NoSuchBucket
    puts "Bucket not found: #{bucket_name}"
  end

end

# Empty the bucket
empty_bucket(client, bucket_name)

# Delete the bucket
begin
  client.delete_bucket(bucket: bucket_name)
  puts "Bucket deleted: #{bucket_name}"
rescue Aws::S3::Errors::NoSuchBucket
  puts "Bucket not found or already deleted: #{bucket_name}"
end

require 'aws-sdk-s3'
require 'pry'
require 'securerandom'

# Retrieve the bucket name from the environment variable 'BUCKET_NAME'
bucket_name = ENV['BUCKET_NAME']

# Initialize an S3 client
client = Aws::S3::Client.new

# Create a new bucket with the specified name
resp = client.create_bucket({
  bucket: bucket_name, 
})

# Generate a random number of files to create, between 1 and 6
number_of_files = 1 + rand(6)
puts "number_of_files: #{number_of_files}"

# Create the specified number of files
number_of_files.times.each do |i|
  puts "i: #{i}"
  filename = "file_#{i}.txt"
  output_path = "/tmp/#{filename}"

  # Write a random UUID to each file
  File.open(output_path, "w") do |f|
    f.write SecureRandom.uuid
  end

  # Upload each file to the S3 bucket
  File.open(output_path, 'rb') do |file|
    client.put_object(
      bucket: bucket_name,
      key: filename,
      body: file
    )
  end
end

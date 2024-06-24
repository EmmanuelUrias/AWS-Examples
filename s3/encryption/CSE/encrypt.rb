require 'aws-sdk-s3'
require 'openssl'
key = OpenSSL::PKey::RSA.new(1024)

bucket_name= 'cse-practice1'
object_key= 'hello.txt'

# encryption client
s3 = Aws::S3::EncryptionV2::Client.new(
  encryption_key: key,
  key_wrap_schema: :rsa_oaep_sha1, # the key_wrap_schema must be rsa_oaep_sha1 for asymmetric keys
  content_encryption_schema: :aes_gcm_no_padding,
  security_profile: :v2 # use :v2_and_legacy to allow reading/decrypting objects encrypted by the V1 encryption client
)

# round-trip an object, encrypted/decrypted locally
# Uploads a object
resp = s3.put_object(bucket: bucket_name, key: object_key, body:'Hello World')
puts "PUT"
puts resp
# Gets the object with the key
resp = s3.get_object(bucket: bucket_name, key: object_key).body.read
puts 'GET'
puts resp
#=> 'Hello World'

# reading encrypted object without the encryption client
# results in the getting the cipher text
# Gets object without the key
resp = Aws::S3::Client.new.get_object(bucket:bucket_name, key: object_key).body.read
puts 'get without key'
puts resp
#=> "... cipher text ..."
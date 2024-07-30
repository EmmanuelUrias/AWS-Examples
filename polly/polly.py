import boto3

client = boto3.client('polly')

response = client.synthesize_speech(
    Engine='standard',
    LanguageCode='en-AU',
    OutputFormat='mp3',
    SampleRate='8000',
    Text='I love hot dogs',
    TextType='text',
    VoiceId='Salli'
)

print(response)

# Check if the response contains audio data
if 'AudioStream' in response:
    with open('sample.mp3', 'wb') as file:
        file.write(response['AudioStream'].read())
else:
    print("Could not stream audio")

print("MP3 file saved successfully.")
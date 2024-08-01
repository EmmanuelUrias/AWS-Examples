import boto3

client = boto3.client('translate')

def translate(text, source_lang, target_lang):
    resp = client.translate_text(
        Text=text,
        SourceLanguageCode=source_lang,
        TargetLanguageCode=target_lang
    )

    print(resp)

if __name__ == '__main__':
    demo_text = 'I love donuts and hamburgers'
    source = 'auto'
    target = 'pt'
    translate(demo_text, source, target)
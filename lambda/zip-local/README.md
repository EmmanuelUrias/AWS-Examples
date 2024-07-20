## To build
```sh
sam build \
--template-file "${template_path}"
```
## To deploy
```sh
sam deploy \
--template-file "./.aws-sam/build/template.yaml" \
--stack-name "zip-local-lamba-py" \
--capabilities "CAPABILITY_IAM"
```
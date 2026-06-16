#!/bin/bash

# Script para desplegar la función Lambda
zip -r deployment.zip src/
aws lambda update-function-code --function-name $lambda_function_name --zip-file fileb://deployment.zip
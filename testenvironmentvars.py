import os

# Access a secret stored as an environment variable

# OpenAI secrets stored as environment variables

openai_secrets = {
  'openai_api_key': os.environ['OPENAI_API_KEY'],
  'openai_api_org_id': os.environ['OPENAI_ORG_ID'],
  'openai_deployment_id': os.environ['OPENAI_PROJECT_ID'],
}

# print('\n'.join(f"{key}: {value}" for key, value in openai_secrets.items()))

# Anthropic AI  secrets stored as environment variables

anthropic_secrets = {
  'anthropic_api_key': os.environ['ANTHROPIC_API_KEY'],
}

# print('\n'.join(f"{key}: {value}" for key, value in anthropic_secrets.items()))

# Cohere AI  secrets stored as environment variables

cohere_secrets = {
  'cohere_api_key': os.environ['COHERE_API_KEY'],
}

# print('\n'.join(f"{key}: {value}" for key, value in cohere_secrets.items()))


# AI21 secrets stored as environment variables

ai21_secrets = {
  'ai21_api_key': os.environ['AI21_API_KEY'],
}

# print('\n'.join(f"{key}: {value}" for key, value in ai21_secrets.items()))


googleaistudio_secrets = {
  'googleaistudio_api_key': os.environ['GOOGLEAISTUDIO_API'],
}

# print('\n'.join(f"{key}: {value}" for key, value in googleaistudio_secrets.items()))


hf_secrets = {
  'hf_api_key': os.environ['HF_TOKEN'],
}

print('\n'.join(f"{key}: {value}" for key, value in hf_secrets.items()))


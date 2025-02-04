import os
from datasets import load_dataset
import torch
from transformers import (
  DistilBertTokenizerFast,
  DistilBertForQuestionAnswering,
  TrainingArguments,
  Trainer,
  DataCollatorWithPadding
)

# Access a secret stored as an environment variable
HF_TOKEN=os.environ['HF_TOKEN']

from datasets import load_dataset
from transformers import (
    DistilBertTokenizerFast,
    DistilBertForQuestionAnswering,
    TrainingArguments,
    Trainer,
    DataCollatorWithPadding
)

# Load a tiny dataset subset
dataset = load_dataset("squad", split="train[:100]")  # Only 100 examples
eval_dataset = load_dataset("squad", split="validation[:20]")  # 20 validation examples


ds = load_dataset("rajpurkar/squad")
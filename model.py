import torch
from torch.utils.data import DataLoader
from sklearn.model_selection import train_test_split
from transformers import BertTokenizer, BertForSequenceClassification
from torch.optim import AdamW
from datasets import load_dataset

# Load the 'toxic-comments' dataset from Hugging Face's Hub
dataset = load_dataset("airespucrs/toxic-comments")

df = dataset['train'].to_pandas()

# Split dataset into training, validation, and test sets
train_indices, test_indices = train_test_split(df.index, test_size=0.2, random_state=42)
train_data = df.loc[train_indices]
test_data = df.loc[test_indices]

train_indices, val_indices = train_test_split(train_data.index, test_size=0.2, random_state=42)
train_data = df.loc[train_indices]
val_data = df.loc[val_indices]

# Define a custom PyTorch dataset class
class ToxicDataset(torch.utils.data.Dataset):
    def __init__(self, dataframe, tokenizer, max_length):
        self.dataframe = dataframe
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, idx):
        text = self.dataframe['comment_text'].iloc[idx]
        label = self.dataframe['toxic'].iloc[idx]
        encoding = self.tokenizer(text, padding='max_length', truncation=True, max_length=self.max_length, return_tensors='pt')
        return {'input_ids': encoding['input_ids'].flatten(),
                'attention_mask': encoding['attention_mask'].flatten(),
                'labels': torch.tensor(label, dtype=torch.long)}
    
# Tokenize and prepare the datasets
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
max_length = 128  # Set your desired maximum sequence length
train_dataset = ToxicDataset(train_data, tokenizer, max_length)
val_dataset = ToxicDataset(val_data, tokenizer, max_length)
test_dataset = ToxicDataset(test_data, tokenizer, max_length)

# Create data loaders for training, validation, and testing
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32)
test_loader = DataLoader(test_dataset, batch_size=32)

# Load pre-trained BERT model for sequence classification
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

# Define optimizer and loss function
optimizer = AdamW(model.parameters(), lr=2e-5)
loss_function = torch.nn.CrossEntropyLoss()

# Training loop
num_epochs = 3  # Adjust as needed
for epoch in range(num_epochs):
    model.train()  # Set model to training mode
    for batch in train_loader:
        inputs = batch['input_ids']
        attention_mask = batch['attention_mask']
        labels = batch['labels']
        outputs = model(inputs, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

# Evaluation loop
model.eval()  # Set model to evaluation mode
total_correct = 0
total_samples = 0
with torch.no_grad():
    for batch in test_loader:
        inputs = batch['input_ids']
        attention_mask = batch['attention_mask']
        labels = batch['labels']
        outputs = model(inputs, attention_mask=attention_mask)
        predictions = torch.argmax(outputs.logits, dim=1)
        total_correct += (predictions == labels).sum().item()
        total_samples += labels.size(0)

# Calculate accuracy
accuracy = total_correct / total_samples
print("Accuracy on test set:", accuracy)

# Save the trained model
model.save_pretrained('saved_model')





"""PyTorch demo: tiny synthetic skill-gap classifier, not an HR decision engine."""
import torch
from torch import nn

torch.manual_seed(21)
x = torch.rand(240, 3)
y = (x[:, 0] * 0.6 + x[:, 1] * 0.3 + x[:, 2] * 0.1 < 0.45).long()
train_x, test_x = x[:180], x[180:]
train_y, test_y = y[:180], y[180:]
model = nn.Sequential(nn.Linear(3, 12), nn.ReLU(), nn.Linear(12, 2))
optimizer = torch.optim.Adam(model.parameters(), lr=0.035)
loss_fn = nn.CrossEntropyLoss()
for _ in range(120):
    optimizer.zero_grad()
    loss = loss_fn(model(train_x), train_y)
    loss.backward()
    optimizer.step()
with torch.no_grad():
    accuracy = (model(test_x).argmax(1) == test_y).float().mean().item()
print({"held_out_accuracy": round(accuracy, 3), "test_examples": len(test_y)})
print("Synthetic experiment: never use predictions to determine real employee outcomes.")

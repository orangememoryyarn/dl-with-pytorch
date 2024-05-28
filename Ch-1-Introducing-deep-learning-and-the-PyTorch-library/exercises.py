import sys
import torch

print(f"Python version {sys.version}")
print(f"Torch version {torch.__version__}")

device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
device = torch.device(device)
print(device)

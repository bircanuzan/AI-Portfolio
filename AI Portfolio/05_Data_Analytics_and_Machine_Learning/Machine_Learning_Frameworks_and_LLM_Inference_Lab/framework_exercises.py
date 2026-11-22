"""Toy automatic-differentiation regression exercises.

Run 'python framework_exercises.py pytorch' or '... jax'.
Only imports the optional framework selected on the command line.
"""
import argparse


def torch_exercise():
    import torch

    torch.manual_seed(42)
    x = torch.linspace(-1.0, 1.0, 80).reshape(-1, 1)
    y = 2.0 * x + 0.5
    model = torch.nn.Linear(1, 1)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.12)
    for _ in range(200):
        optimizer.zero_grad()
        loss = torch.mean((model(x) - y) ** 2)
        loss.backward()
        optimizer.step()
    print({"framework": "PyTorch", "mse": float(loss.detach()), "weight": float(model.weight.detach().squeeze()), "bias": float(model.bias.detach().squeeze())})


def jax_exercise():
    import jax
    import jax.numpy as jnp

    x = jnp.linspace(-1.0, 1.0, 80)
    y = 2.0 * x + 0.5

    @jax.jit
    def step(params):
        def loss_fn(p):
            return jnp.mean((p[0] * x + p[1] - y) ** 2)
        grads = jax.grad(loss_fn)(params)
        return params - 0.12 * grads

    params = jnp.array([0.0, 0.0])
    for _ in range(200):
        params = step(params)
    mse = jnp.mean((params[0] * x + params[1] - y) ** 2)
    print({"framework": "JAX", "mse": float(mse), "weight": float(params[0]), "bias": float(params[1])})


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("framework", choices=("pytorch", "jax"))
    args = parser.parse_args()
    (torch_exercise if args.framework == "pytorch" else jax_exercise)()

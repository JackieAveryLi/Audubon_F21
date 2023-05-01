import torch


def get_sgd_optim(model, lr, momentum=0.9, weight_decay=0.0005):
    """
    Returns a stochastic gradient descent (SGD) optimizer associated with the input model, with the specified learning rate, momentum, and weight decay.

    Args:
        model (nn.Module): The PyTorch model for which the optimizer will be created.
        lr (float): The learning rate for the optimizer.
        momentum (float, optional): The momentum factor for SGD. Default is 0.9.
        weight_decay (float, optional): The weight decay (L2 penalty) factor for SGD. Default is 0.0005.

    Returns:
        The created SGD optimizer.
    """
    # Filter model parameters that need to have gradients computed
    params = [param for param in model.parameters() if param.requires_grad]
    optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum, weight_decay=weight_decay)
    return optimizer

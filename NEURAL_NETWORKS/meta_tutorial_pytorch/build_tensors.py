import torch

def activation(x):

    """
       Sigmoid activation function

       Arguments
       -------------
       x : torch.Tensor
    """

    return (1/(1+torch.exp(-x)))

torch.manual_seed(7) # set random seed

# Features are 5 random normal variables
features = torch.randn((1,5))
print(features)

weights = torch.randn_like(features)
print(weights)

bias = torch.randn((1,1))
print(bias)

y = activation(torch.mm(features, weights.view(5,1)) + bias)
print(y)

"""
y = activation((features * weights).sum() + bias))

feature * weight .sum() is doing summation of feature_i * weight_i


# torch.mm()  --> matrix multiplication


y = activation(torch.sum(features * weights.view(5,1) + bias)
"""


# matrix multiplication in pytorch

# torch.mm()
# tochmatmul()  -- supports broadcasting and complication ( may not do what is expected all the time )

# tensor.shape  to look at shape of the tensor
# for eg : weights.shape()


# weights.reshape()

"""

weights.reshape(a,b)

will reutrn a new tensor with same data shape as a,b

use weights.resize_(a,b) --> memory efficient, we not copying data, just the shape

weights.view(a,b) returns a new tensor with same data as weights with same memory with size(a,b)

view will return the same number of elements when you reshape weights.

weights.view(5,1)


"""












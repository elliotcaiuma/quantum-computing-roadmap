"""
Level 23: Compute Schmidt Decomposition

For any bipartite pure state |psi>, find orthonormal bases such that:
|psi> = sum lambda_i |i_A> tensor |i_B>
where lambda_i are Schmidt coefficients.
"""

import numpy as np


def schmidt_decomposition(psi, dim_a=2, dim_b=2):
    """Compute Schmidt decomposition of bipartite state.
    
    Args:
        psi: State vector of composite system
        dim_a: Dimension of subsystem A
        dim_b: Dimension of subsystem B
        
    Returns:
        Tuple (schmidt_coefficients, basis_a, basis_b)
    """
    # Reshape to matrix form
    psi_matrix = psi.reshape(dim_a, dim_b)
    
    # SVD gives Schmidt decomposition
    U, s, Vh = np.linalg.svd(psi_matrix)
    
    # Schmidt coefficients
    lambdas = s
    
    # Schmidt bases
    basis_a = U
    basis_b = Vh.conj().T
    
    return lambdas, basis_a, basis_b


if __name__ == "__main__":
    # Bell state |Phi+>
    bell_phi_plus = np.array([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])
    
    lambdas, ba, bb = schmidt_decomposition(bell_phi_plus)
    
    print("Schmidt decomposition of |Phi+>:")
    print("Schmidt coefficients:", lambdas)
    print("Schmidt rank:", np.sum(lambdas > 1e-10))
    print()
    
    # Product state |00>
    product = np.array([1, 0, 0, 0])
    
    lambdas, ba, bb = schmidt_decomposition(product)
    
    print("Schmidt decomposition of |00>:")
    print("Schmidt coefficients:", lambdas)
    print("Schmidt rank:", np.sum(lambdas > 1e-10))
    print()
    
    print("Interpretation:")
    print("- Schmidt rank = 1: Product state (not entangled)")
    print("- Schmidt rank > 1: Entangled state")

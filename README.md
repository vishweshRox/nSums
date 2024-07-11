Uses perturbation theory to generate the coefficients of the polynomial that will compute the sum of the first n terms of k-powers. 

For example, perturb(2) will produce the polynomial coefficients that compute the sum of the first n terms of all powers of 2. perturb(2).compute(5) will produce the sum of the first 5 terms (55).

This code uses a custom polynomial class. Accuracy is maintained until perturb(6), after which the values are inaccurate due to the use of floating point integers. Future version will include a Fraction class to maintain accuracy.

UPDATE:
Fraction class was implemented to allow for accurate arithmetic operations with no loss in accuracy. Correct coefficients can now be for powers up until 15.

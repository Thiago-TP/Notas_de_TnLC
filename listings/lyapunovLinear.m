	clc;
	A = [0  1   0;
	     0  0   1;
	     -8 -12 -6];
	I = [1 0 0; 
	     0 1 0; 
	     0 0 1];
	P = lyap(A',I);             % P: A'P + PA + I = 0 
	%teste = A'*P + P*A + I;

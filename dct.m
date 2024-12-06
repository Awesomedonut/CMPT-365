% warning: using matlab's default funcs gives diff nums than assign solu

% Define the matrix
input_matrix = [60, 47, 28, 0, 11, 0, 0, 0;
                0, 0, 0, 12, 0, 0, 0, 0;
                0, 0, 0, 0, 0, 0, 0, 0;
                0, 0, 0, 7, 0, 0, 0, 0;
                0, 0, 0, 0, 0, 0, 0, 0;
                0, 0, 0, 0, 0, 0, 0, 0;
                0, 0, 0, 0, 0, 0, 0, 0;
                0, 0, 0, 0, 0, 0, 0, 0];

% Perform 2D Discrete Cosine Transform
dct_matrix = dct2(input_matrix);

% Perform 2D Inverse Discrete Cosine Transform
reconstructed_matrix = idct2(dct_matrix);

% Display the results
disp('Original Matrix:');
disp(input_matrix);

disp('DCT of the matrix:');
disp(dct_matrix);

disp('Reconstructed Matrix (after inverse DCT):');
disp(reconstructed_matrix);

% Compare the matrices
difference = input_matrix - reconstructed_matrix;
disp('Difference between Original and Reconstructed Matrices:');
disp(difference);

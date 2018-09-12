import numpy as np
from scipy.interpolate import interp1d

# Code: cgiSensePlot.c v4.0 (sll - 13 February 2009 Build)
# from WWW Sensitivity Curve Generator located at:
#   http://www.srl.caltech.edu/~shane/sensitivity/MakeCurve.html
# EQUAL ARM Space Based Observatory Sensitivity Curve
# Polarization and All Sky Averaged
#
# For this data file:
# SNR = 1.000000
# Armlength = 5.000000e+09 	meters
# Optics diameter = 0.300000 	meters
# Wavelength = 1064.000000 	nanometers
# Laser power = 1.000000 Watts
# Optical train efficiency = 0.300000
# Accleration noise = 3.000000e-15 m/(s^2 root Hz)
# Position noise = 2.000000e-11 m/(root Hz)
# Sensitivity Floor Set by Position Noise Budget
# Output Curve type is Root Spectral Density, per root Hz
# Astrophysical Noise is Merged Instrumental + White Dwarf Noise

# f [Hz] 	 hf [Hz^(-1/2)]
_LISA_DATA = map(float, """
9.765035e-08 8.230539e-12
9.992561e-08 7.859994e-12
1.022538e-07 7.506140e-12
1.046364e-07 7.168208e-12
1.070744e-07 6.845487e-12
1.095693e-07 6.537299e-12
1.121222e-07 6.242988e-12
1.147346e-07 5.961930e-12
1.174080e-07 5.693514e-12
1.201436e-07 5.437190e-12
1.229430e-07 5.192405e-12
1.258075e-07 4.958644e-12
1.287388e-07 4.735402e-12
1.317385e-07 4.522210e-12
1.348080e-07 4.318618e-12
1.379489e-07 4.124195e-12
1.411632e-07 3.938518e-12
1.444523e-07 3.761205e-12
1.478180e-07 3.591876e-12
1.512621e-07 3.430168e-12
1.547865e-07 3.275741e-12
1.583931e-07 3.128264e-12
1.620836e-07 2.987428e-12
1.658602e-07 2.852934e-12
1.697248e-07 2.724491e-12
1.736793e-07 2.601834e-12
1.777260e-07 2.484699e-12
1.818671e-07 2.372836e-12
1.861046e-07 2.266009e-12
1.904408e-07 2.163993e-12
1.948781e-07 2.066569e-12
1.994188e-07 1.973531e-12
2.040652e-07 1.884682e-12
2.088199e-07 1.799832e-12
2.136855e-07 1.718802e-12
2.186644e-07 1.641421e-12
2.237592e-07 1.567524e-12
2.289728e-07 1.496953e-12
2.343079e-07 1.429559e-12
2.397673e-07 1.365200e-12
2.453538e-07 1.303738e-12
2.510706e-07 1.245043e-12
2.569205e-07 1.188990e-12
2.629067e-07 1.135461e-12
2.690325e-07 1.084342e-12
2.753009e-07 1.035525e-12
2.817154e-07 9.889054e-13
2.882794e-07 9.443839e-13
2.949963e-07 9.018673e-13
3.018697e-07 8.612648e-13
3.089033e-07 8.224904e-13
3.161008e-07 7.854613e-13
3.234659e-07 7.500995e-13
3.310026e-07 7.163298e-13
3.387150e-07 6.840801e-13
3.466070e-07 6.532827e-13
3.546830e-07 6.238715e-13
3.629471e-07 5.957846e-13
3.714038e-07 5.689619e-13
3.800575e-07 5.433470e-13
3.889128e-07 5.188853e-13
3.979745e-07 4.955249e-13
4.072473e-07 4.732161e-13
4.167362e-07 4.519116e-13
4.264461e-07 4.315663e-13
4.363823e-07 4.121371e-13
4.465500e-07 3.935824e-13
4.569546e-07 3.758632e-13
4.676017e-07 3.589416e-13
4.784967e-07 3.427819e-13
4.896457e-07 3.273497e-13
5.010545e-07 3.126122e-13
5.127290e-07 2.985383e-13
5.246756e-07 2.850980e-13
5.369006e-07 2.722627e-13
5.494104e-07 2.600053e-13
5.622116e-07 2.482997e-13
5.753111e-07 2.371212e-13
5.887160e-07 2.264458e-13
6.024330e-07 2.162511e-13
6.164697e-07 2.065154e-13
6.308335e-07 1.972179e-13
6.455319e-07 1.883391e-13
6.605728e-07 1.798600e-13
6.759641e-07 1.717626e-13
6.917140e-07 1.640298e-13
7.078310e-07 1.566451e-13
7.243235e-07 1.495928e-13
7.412002e-07 1.428581e-13
7.584702e-07 1.364265e-13
7.761425e-07 1.302846e-13
7.942267e-07 1.244191e-13
8.127321e-07 1.188177e-13
8.316687e-07 1.134684e-13
8.510467e-07 1.083600e-13
8.708760e-07 1.034816e-13
8.911674e-07 9.882283e-14
9.119316e-07 9.437377e-14
9.331797e-07 9.012501e-14
9.549227e-07 8.606755e-14
9.771724e-07 8.219274e-14
9.999403e-07 7.849242e-14
1.023239e-06 7.495867e-14
1.047080e-06 7.158399e-14
1.071478e-06 6.836114e-14
1.096443e-06 6.528358e-14
1.121990e-06 6.234442e-14
1.148133e-06 5.953766e-14
1.174884e-06 5.685729e-14
1.202259e-06 5.429752e-14
1.230271e-06 5.185302e-14
1.258937e-06 4.951858e-14
1.288270e-06 4.728922e-14
1.318286e-06 4.516025e-14
1.349002e-06 4.312712e-14
1.380434e-06 4.118551e-14
1.412599e-06 3.933130e-14
1.445512e-06 3.756057e-14
1.479192e-06 3.586960e-14
1.513658e-06 3.425473e-14
1.548927e-06 3.271254e-14
1.585016e-06 3.123982e-14
1.621947e-06 2.983338e-14
1.659738e-06 2.849028e-14
1.698410e-06 2.720764e-14
1.737983e-06 2.598272e-14
1.778478e-06 2.481298e-14
1.819917e-06 2.369587e-14
1.862321e-06 2.262908e-14
1.905712e-06 2.161032e-14
1.950116e-06 2.063741e-14
1.995554e-06 1.970829e-14
2.042050e-06 1.882102e-14
2.089630e-06 1.797369e-14
2.138318e-06 1.716450e-14
2.188141e-06 1.639175e-14
2.239125e-06 1.565379e-14
2.291296e-06 1.494904e-14
2.344684e-06 1.427602e-14
2.399315e-06 1.363331e-14
2.455219e-06 1.301954e-14
2.512425e-06 1.243339e-14
2.570965e-06 1.187363e-14
2.630868e-06 1.133908e-14
2.692168e-06 1.082858e-14
2.754895e-06 1.034108e-14
2.819084e-06 9.875514e-15
2.884769e-06 9.430916e-15
2.951984e-06 9.006333e-15
3.020765e-06 8.600860e-15
3.091149e-06 8.213644e-15
3.163173e-06 7.843864e-15
3.236875e-06 7.490728e-15
3.312294e-06 7.153494e-15
3.389470e-06 6.831440e-15
3.468444e-06 6.523886e-15
3.549260e-06 6.230176e-15
3.631957e-06 5.949690e-15
3.716582e-06 5.681832e-15
3.803178e-06 5.426034e-15
3.891793e-06 5.181751e-15
3.982471e-06 4.948466e-15
4.075263e-06 4.725683e-15
4.170217e-06 4.512930e-15
4.267382e-06 4.309757e-15
4.366812e-06 4.115729e-15
4.468559e-06 3.930436e-15
4.572677e-06 3.753486e-15
4.679220e-06 3.584503e-15
4.788246e-06 3.423126e-15
4.899812e-06 3.269016e-15
5.013978e-06 3.121843e-15
5.130803e-06 2.981296e-15
5.250351e-06 2.847077e-15
5.372684e-06 2.718900e-15
5.497867e-06 2.596494e-15
5.625968e-06 2.479599e-15
5.757053e-06 2.367966e-15
5.891192e-06 2.261359e-15
6.028457e-06 2.159551e-15
6.168920e-06 2.062327e-15
6.312656e-06 1.969480e-15
6.459741e-06 1.880813e-15
6.610253e-06 1.796138e-15
6.764272e-06 1.715275e-15
6.921879e-06 1.638052e-15
7.083159e-06 1.564306e-15
7.248196e-06 1.493881e-15
7.417080e-06 1.426625e-15
7.589898e-06 1.362398e-15
7.766742e-06 1.301062e-15
7.947707e-06 1.242488e-15
8.132889e-06 1.186550e-15
8.322385e-06 1.133131e-15
8.516297e-06 1.082117e-15
8.714726e-06 1.033400e-15
8.917780e-06 9.868754e-16
9.125564e-06 9.424457e-16
9.338190e-06 9.000164e-16
9.555773e-06 8.596516e-16
9.778423e-06 8.203796e-16
1.000626e-05 7.842100e-16
1.023940e-05 7.487290e-16
1.047798e-05 7.150519e-16
1.072212e-05 6.826616e-16
1.097194e-05 6.519610e-16
1.122759e-05 6.228491e-16
1.148919e-05 5.944378e-16
1.175689e-05 5.677198e-16
1.203082e-05 5.424234e-16
1.231114e-05 5.178527e-16
1.259799e-05 4.945224e-16
1.289153e-05 4.722685e-16
1.319190e-05 4.509176e-16
1.349927e-05 4.307189e-16
1.381380e-05 4.112541e-16
1.413566e-05 3.927505e-16
1.446503e-05 3.750364e-16
1.480206e-05 3.582161e-16
1.514695e-05 3.420310e-16
1.549987e-05 3.266847e-16
1.586102e-05 3.119744e-16
1.623058e-05 2.978757e-16
1.660876e-05 2.845108e-16
1.699574e-05 2.716874e-16
1.739173e-05 2.594650e-16
1.779696e-05 2.477797e-16
1.821163e-05 2.366199e-16
1.863597e-05 2.259827e-16
1.907018e-05 2.158126e-16
1.951452e-05 2.060941e-16
1.996921e-05 1.968119e-16
2.043449e-05 1.879505e-16
2.091061e-05 1.794902e-16
2.139783e-05 1.714096e-16
2.189640e-05 1.636955e-16
2.240659e-05 1.563260e-16
2.292866e-05 1.492898e-16
2.346290e-05 1.425682e-16
2.400958e-05 1.361489e-16
2.456900e-05 1.300159e-16
2.514147e-05 1.241636e-16
2.572726e-05 1.185755e-16
2.632671e-05 1.132354e-16
2.694012e-05 1.081372e-16
2.756782e-05 1.032693e-16
2.821015e-05 9.861999e-17
2.886745e-05 9.417898e-17
2.954006e-05 8.994035e-17
3.022834e-05 8.589040e-17
3.093267e-05 8.202404e-17
3.165340e-05 7.833080e-17
3.239092e-05 7.480423e-17
3.314563e-05 7.143698e-17
3.391792e-05 6.822040e-17
3.470821e-05 6.514956e-17
3.551691e-05 6.221652e-17
3.634445e-05 5.941521e-17
3.719128e-05 5.674042e-17
3.805783e-05 5.418604e-17
3.894459e-05 5.174658e-17
3.985199e-05 4.941688e-17
4.078054e-05 4.719209e-17
4.173073e-05 4.506742e-17
4.270306e-05 4.303854e-17
4.369804e-05 4.110085e-17
4.471621e-05 3.925047e-17
4.575809e-05 3.748345e-17
4.682425e-05 3.579589e-17
4.791526e-05 3.418436e-17
4.903169e-05 3.264534e-17
5.017412e-05 3.117569e-17
5.134318e-05 2.977207e-17
5.253948e-05 2.843176e-17
5.376365e-05 2.715171e-17
5.501634e-05 2.592932e-17
5.629822e-05 2.476199e-17
5.760997e-05 2.364719e-17
5.895228e-05 2.258256e-17
6.032587e-05 2.156589e-17
6.173146e-05 2.059497e-17
6.316980e-05 1.966777e-17
6.464166e-05 1.878232e-17
6.614781e-05 1.793673e-17
6.768906e-05 1.712920e-17
6.926621e-05 1.635804e-17
7.088012e-05 1.562159e-17
7.253162e-05 1.491829e-17
7.422160e-05 1.424666e-17
7.595097e-05 1.360527e-17
7.772063e-05 1.299274e-17
7.953152e-05 1.240781e-17
8.138461e-05 1.184920e-17
8.328086e-05 1.131574e-17
8.522131e-05 1.080630e-17
8.720696e-05 1.031979e-17
8.923889e-05 9.855182e-18
9.131815e-05 9.411496e-18
9.344587e-05 8.987782e-18
9.562320e-05 8.583139e-18
9.785113e-05 8.196733e-18
1.001311e-04 8.482534e-18
1.024642e-04 8.143535e-18
1.048516e-04 7.820224e-18
1.072946e-04 7.506294e-18
1.097946e-04 7.203762e-18
1.123528e-04 6.911949e-18
1.149706e-04 6.630576e-18
1.176494e-04 6.364943e-18
1.203907e-04 6.116981e-18
1.231958e-04 5.880652e-18
1.260662e-04 5.658161e-18
1.290035e-04 5.446143e-18
1.320094e-04 5.244110e-18
1.350852e-04 5.051610e-18
1.382326e-04 4.868195e-18
1.414535e-04 4.693638e-18
1.447493e-04 4.530233e-18
1.481220e-04 4.371627e-18
1.515732e-04 4.220725e-18
1.551049e-04 4.080137e-18
1.587189e-04 3.946401e-18
1.624170e-04 3.819194e-18
1.662013e-04 3.698410e-18
1.700738e-04 3.586611e-18
1.740365e-04 3.477376e-18
1.780916e-04 3.376836e-18
1.822411e-04 3.281419e-18
1.864874e-04 3.190860e-18
1.908325e-04 3.104908e-18
1.952788e-04 3.023322e-18
1.998289e-04 2.945618e-18
2.044849e-04 2.868288e-18
2.092493e-04 2.794621e-18
2.141249e-04 2.724420e-18
2.191140e-04 2.657497e-18
2.242193e-04 2.593418e-18
2.294437e-04 2.528461e-18
2.347897e-04 2.462757e-18
2.402603e-04 2.399716e-18
2.458584e-04 2.338949e-18
2.515869e-04 2.277140e-18
2.574488e-04 2.217420e-18
2.634474e-04 2.156573e-18
2.695858e-04 2.097933e-18
2.758671e-04 2.040908e-18
2.822948e-04 1.979747e-18
2.888722e-04 1.923626e-18
2.956030e-04 1.866376e-18
3.024905e-04 1.811338e-18
3.095385e-04 1.761139e-18
3.167508e-04 1.712639e-18
3.241311e-04 1.665766e-18
3.316833e-04 1.619801e-18
3.394115e-04 1.567175e-18
3.473199e-04 1.516380e-18
3.554124e-04 1.467346e-18
3.636935e-04 1.420205e-18
3.721676e-04 1.377316e-18
3.808391e-04 1.338237e-18
3.897126e-04 1.300421e-18
3.987929e-04 1.264002e-18
4.080848e-04 1.230977e-18
4.175932e-04 1.198975e-18
4.273231e-04 1.167955e-18
4.372798e-04 1.138052e-18
4.474684e-04 1.110947e-18
4.578944e-04 1.082775e-18
4.685633e-04 1.057427e-18
4.794809e-04 1.032643e-18
4.906528e-04 1.006808e-18
5.020849e-04 9.835970e-19
5.137835e-04 9.611885e-19
5.257547e-04 9.410567e-19
5.380048e-04 9.196772e-19
5.505403e-04 8.988750e-19
5.633679e-04 8.786294e-19
5.764943e-04 8.587750e-19
5.899266e-04 8.379372e-19
6.036719e-04 8.192788e-19
6.177375e-04 8.009636e-19
6.321308e-04 7.817026e-19
6.468595e-04 7.643390e-19
6.619313e-04 7.459254e-19
6.773543e-04 7.278684e-19
6.931367e-04 7.089927e-19
7.092867e-04 6.919001e-19
7.258131e-04 6.740192e-19
7.427246e-04 6.578315e-19
7.600301e-04 6.407687e-19
7.777387e-04 6.241717e-19
7.958600e-04 6.080265e-19
8.144035e-04 5.923193e-19
8.333792e-04 5.770371e-19
8.527969e-04 5.622727e-19
8.726671e-04 5.489152e-19
8.930002e-04 5.348044e-19
9.138071e-04 5.210712e-19
9.350988e-04 5.078016e-19
9.568866e-04 4.958951e-19
9.791821e-04 4.842827e-19
1.001997e-03 4.729567e-19
1.025344e-03 4.619984e-19
1.049234e-03 4.522331e-19
1.073681e-03 4.426879e-19
1.098698e-03 4.333576e-19
1.124298e-03 4.242357e-19
1.150493e-03 4.154004e-19
1.177300e-03 4.075977e-19
1.204731e-03 3.999532e-19
1.232802e-03 3.924629e-19
1.261526e-03 3.850454e-19
1.290920e-03 3.770754e-19
1.320997e-03 3.699655e-19
1.351777e-03 3.621745e-19
1.383273e-03 3.537501e-19
1.415504e-03 3.446710e-19
1.448485e-03 3.341667e-19
1.482235e-03 3.209185e-19
1.516771e-03 3.037686e-19
1.552112e-03 2.811405e-19
1.588276e-03 2.549015e-19
1.625282e-03 2.261138e-19
1.663152e-03 1.975323e-19
1.701904e-03 1.704067e-19
1.741557e-03 1.459603e-19
1.782136e-03 1.254489e-19
1.823660e-03 1.084437e-19
1.866150e-03 9.449930e-20
1.909632e-03 8.312050e-20
1.954126e-03 7.337509e-20
1.999657e-03 6.502911e-20
2.046250e-03 5.796329e-20
2.093928e-03 5.187256e-20
2.142716e-03 4.661558e-20
2.192641e-03 4.207976e-20
2.243730e-03 3.822759e-20
2.296009e-03 3.499884e-20
2.349506e-03 3.228159e-20
2.404249e-03 2.999061e-20
2.460268e-03 2.807779e-20
2.517593e-03 2.638119e-20
2.576253e-03 2.493279e-20
2.636279e-03 2.366533e-20
2.697704e-03 2.255710e-20
2.760561e-03 2.160835e-20
2.824882e-03 2.076929e-20
2.890701e-03 1.998964e-20
2.958055e-03 1.930275e-20
3.026978e-03 1.868164e-20
3.097506e-03 1.813752e-20
3.169678e-03 1.766589e-20
3.243532e-03 1.728039e-20
3.319106e-03 1.686363e-20
3.396441e-03 1.627769e-20
3.475578e-03 1.556124e-20
3.556559e-03 1.496017e-20
3.639427e-03 1.456191e-20
3.724226e-03 1.429565e-20
3.811000e-03 1.406496e-20
3.899796e-03 1.385833e-20
3.990661e-03 1.367199e-20
4.083644e-03 1.349165e-20
4.178793e-03 1.332975e-20
4.276159e-03 1.317334e-20
4.375793e-03 1.303368e-20
4.477749e-03 1.289907e-20
4.582080e-03 1.278031e-20
4.688843e-03 1.267079e-20
4.798093e-03 1.257071e-20
4.909889e-03 1.248321e-20
5.024289e-03 1.239878e-20
5.141355e-03 1.232262e-20
5.261149e-03 1.225741e-20
5.383733e-03 1.219552e-20
5.509175e-03 1.214367e-20
5.637538e-03 1.209459e-20
5.768893e-03 1.205230e-20
5.903308e-03 1.201888e-20
6.040855e-03 1.198818e-20
6.181607e-03 1.196366e-20
6.325639e-03 1.194709e-20
6.473025e-03 1.193331e-20
6.623848e-03 1.192499e-20
6.778182e-03 1.192231e-20
6.936115e-03 1.192645e-20
7.097726e-03 1.193199e-20
7.263103e-03 1.194480e-20
7.432333e-03 1.196262e-20
7.605507e-03 1.198427e-20
7.782715e-03 1.201288e-20
7.964053e-03 1.204661e-20
8.149615e-03 1.208442e-20
8.339501e-03 1.212788e-20
8.533811e-03 1.217711e-20
8.732649e-03 1.223224e-20
8.936120e-03 1.229343e-20
9.144331e-03 1.236085e-20
9.357394e-03 1.243473e-20
9.575422e-03 1.251574e-20
9.798530e-03 1.241597e-20
1.002684e-02 1.252391e-20
1.026046e-02 1.263868e-20
1.049953e-02 1.276072e-20
1.074416e-02 1.289051e-20
1.099451e-02 1.302859e-20
1.125068e-02 1.317555e-20
1.151282e-02 1.333204e-20
1.178107e-02 1.349877e-20
1.205557e-02 1.367651e-20
1.233647e-02 1.386613e-20
1.262390e-02 1.406855e-20
1.291804e-02 1.428483e-20
1.321903e-02 1.451612e-20
1.352703e-02 1.476369e-20
1.384222e-02 1.502894e-20
1.416473e-02 1.531344e-20
1.449477e-02 1.561892e-20
1.483250e-02 1.594732e-20
1.517810e-02 1.630079e-20
1.553175e-02 1.668172e-20
1.589364e-02 1.709280e-20
1.626396e-02 1.753702e-20
1.664291e-02 1.801773e-20
1.703069e-02 1.853865e-20
1.742751e-02 1.910398e-20
1.783357e-02 1.971836e-20
1.824909e-02 2.038697e-20
1.867429e-02 2.111554e-20
1.910940e-02 2.191033e-20
1.955465e-02 2.277816e-20
2.001028e-02 2.372632e-20
2.047651e-02 2.476238e-20
2.095362e-02 2.589385e-20
2.144183e-02 2.712775e-20
2.194143e-02 2.846967e-20
2.245267e-02 2.992251e-20
2.297581e-02 3.148461e-20
2.351115e-02 3.314706e-20
2.405896e-02 3.489032e-20
2.461953e-02 3.668027e-20
2.519317e-02 3.846438e-20
2.578017e-02 4.016973e-20
2.638084e-02 4.170497e-20
2.699553e-02 4.296874e-20
2.762451e-02 4.386525e-20
2.826817e-02 4.432434e-20
2.892681e-02 4.431893e-20
2.960081e-02 4.387232e-20
3.029051e-02 4.305180e-20
3.099628e-02 4.195185e-20
3.171849e-02 4.067445e-20
3.245753e-02 3.931354e-20
3.321379e-02 3.794625e-20
3.398768e-02 3.663059e-20
3.477958e-02 3.540704e-20
3.558995e-02 3.430210e-20
3.641920e-02 3.333209e-20
3.726777e-02 3.250659e-20
3.813610e-02 3.183111e-20
3.902468e-02 3.130923e-20
3.993395e-02 3.094408e-20
4.086441e-02 3.073947e-20
4.181656e-02 3.070084e-20
4.279088e-02 3.083586e-20
4.378790e-02 3.115513e-20
4.480816e-02 3.167271e-20
4.585220e-02 3.240658e-20
4.692055e-02 3.337896e-20
4.801380e-02 3.461622e-20
4.913253e-02 3.614794e-20
5.027731e-02 3.800435e-20
5.144878e-02 4.021065e-20
5.264753e-02 4.277583e-20
5.387421e-02 4.567345e-20
5.512949e-02 4.881244e-20
5.641400e-02 5.200311e-20
5.772845e-02 5.493886e-20
5.907352e-02 5.723287e-20
6.044994e-02 5.853857e-20
6.185842e-02 5.871059e-20
6.329972e-02 5.788569e-20
6.477460e-02 5.641188e-20
6.628385e-02 5.469512e-20
6.782826e-02 5.308133e-20
6.940866e-02 5.181788e-20
7.102588e-02 5.106953e-20
7.268078e-02 5.095236e-20
7.437425e-02 5.156580e-20
7.610717e-02 5.301658e-20
7.788046e-02 5.543316e-20
7.969508e-02 5.896588e-20
8.155197e-02 6.375584e-20
8.345213e-02 6.983106e-20
8.539657e-02 7.686288e-20
8.738631e-02 8.378357e-20
8.942241e-02 8.867067e-20
9.150595e-02 8.975036e-20
9.363804e-02 8.706563e-20
9.581978e-02 8.244549e-20
9.803368e-02 7.790364e-20
1.002987e-01 7.458568e-20
1.026162e-01 7.304369e-20
1.049872e-01 7.356351e-20
1.074128e-01 7.640322e-20
1.098946e-01 8.186921e-20
1.124337e-01 9.016525e-20
1.150315e-01 1.007434e-19
1.176892e-01 1.109429e-19
1.204084e-01 1.157387e-19
1.231905e-01 1.124714e-19
1.260368e-01 1.046877e-19
1.289488e-01 9.741535e-20
1.319282e-01 9.331344e-20
1.349764e-01 9.337619e-20
1.380950e-01 9.823575e-20
1.412856e-01 1.086059e-19
1.445501e-01 1.243467e-19
1.478898e-01 1.406546e-19
1.513069e-01 1.457502e-19
1.548028e-01 1.361177e-19
1.583796e-01 1.232325e-19
1.620389e-01 1.156700e-19
1.657828e-01 1.159843e-19
1.696131e-01 1.253079e-19
1.735320e-01 1.442396e-19
1.775415e-01 1.666450e-19
1.816436e-01 1.717616e-19
1.858404e-01 1.553223e-19
1.901342e-01 1.392739e-19
1.927040e-01 1.349667e-19
1.953085e-01 1.352582e-19
1.979482e-01 1.405307e-19
2.006235e-01 1.512176e-19
2.033351e-01 1.672670e-19
2.060833e-01 1.862641e-19
2.088686e-01 2.007268e-19
2.116915e-01 2.014193e-19
2.145527e-01 1.891064e-19
2.174524e-01 1.734964e-19
2.203914e-01 1.618073e-19
2.233701e-01 1.566473e-19
2.263891e-01 1.587866e-19
2.294488e-01 1.688097e-19
2.325499e-01 1.870020e-19
2.356930e-01 2.106606e-19
2.388785e-01 2.287123e-19
2.421070e-01 2.266695e-19
2.453793e-01 2.082242e-19
2.486957e-01 1.891387e-19
2.520569e-01 1.780135e-19
2.554636e-01 1.771053e-19
2.589163e-01 1.873123e-19
2.624157e-01 2.093111e-19
2.659624e-01 2.394324e-19
2.695570e-01 2.597596e-19
2.732002e-01 2.502243e-19
2.768926e-01 2.243969e-19
2.806350e-01 2.044989e-19
2.844279e-01 1.981854e-19
2.871554e-01 2.028793e-19
2.899090e-01 2.157027e-19
2.926891e-01 2.366111e-19
2.954958e-01 2.626558e-19
2.983294e-01 2.838988e-19
3.011902e-01 2.864464e-19
3.040785e-01 2.693423e-19
3.069945e-01 2.461381e-19
3.099383e-01 2.279172e-19
3.129104e-01 2.187374e-19
3.159110e-01 2.195981e-19
3.189405e-01 2.310950e-19
3.219989e-01 2.536414e-19
3.250867e-01 2.846836e-19
3.282040e-01 3.119963e-19
3.313513e-01 3.153843e-19
3.345288e-01 2.932859e-19
3.377367e-01 2.655784e-19
3.409754e-01 2.463717e-19
3.442452e-01 2.398022e-19
3.475463e-01 2.468226e-19
3.508791e-01 2.681625e-19
3.542438e-01 3.023187e-19
3.576408e-01 3.366303e-19
3.610703e-01 3.437650e-19
3.645328e-01 3.177297e-19
3.680285e-01 2.850803e-19
3.715576e-01 2.642993e-19
3.751206e-01 2.600452e-19
3.787178e-01 2.734317e-19
3.815347e-01 2.965190e-19
3.843726e-01 3.288839e-19
3.872317e-01 3.613118e-19
3.901120e-01 3.751818e-19
3.930136e-01 3.602581e-19
3.959369e-01 3.300604e-19
3.988820e-01 3.024997e-19
4.018489e-01 2.857103e-19
4.048379e-01 2.816991e-19
4.078490e-01 2.910580e-19
4.108828e-01 3.143217e-19
4.139389e-01 3.499689e-19
4.170179e-01 3.875606e-19
4.201197e-01 4.032480e-19
4.232446e-01 3.838074e-19
4.263927e-01 3.481432e-19
4.295643e-01 3.183514e-19
4.327594e-01 3.028965e-19
4.359783e-01 3.034970e-19
4.392212e-01 3.208901e-19
4.424882e-01 3.552278e-19
4.457794e-01 4.001224e-19
4.490952e-01 4.311168e-19
4.524356e-01 4.202971e-19
4.558009e-01 3.810293e-19
4.591912e-01 3.447766e-19
4.626067e-01 3.254418e-19
4.660476e-01 3.257658e-19
4.695142e-01 3.466388e-19
4.730064e-01 3.877366e-19
4.758811e-01 4.293208e-19
4.787732e-01 4.582915e-19
4.816829e-01 4.534575e-19
4.846103e-01 4.202534e-19
4.875554e-01 3.825038e-19
4.905185e-01 3.553448e-19
4.934996e-01 3.433077e-19
4.964987e-01 3.472786e-19
4.995162e-01 3.678689e-19
5.025519e-01 4.048978e-19
5.056062e-01 4.519207e-19
5.086789e-01 4.867085e-19
5.117704e-01 4.817833e-19
5.148805e-01 4.435050e-19
5.180097e-01 4.017686e-19
5.211578e-01 3.740106e-19
5.243251e-01 3.647346e-19
5.275116e-01 3.747983e-19
5.307176e-01 4.048441e-19
5.339429e-01 4.525963e-19
5.371879e-01 5.019893e-19
5.404526e-01 5.173336e-19
5.437372e-01 4.846248e-19
5.470416e-01 4.358934e-19
5.503662e-01 3.996982e-19
5.537110e-01 3.847298e-19
5.570761e-01 3.924130e-19
5.604617e-01 4.235725e-19
5.638678e-01 4.761001e-19
5.672946e-01 5.312341e-19
5.702096e-01 5.472881e-19
5.731395e-01 5.210935e-19
5.760846e-01 4.752400e-19
5.790447e-01 4.352840e-19
5.820200e-01 4.117658e-19
5.850106e-01 4.069499e-19
5.880167e-01 4.214159e-19
5.910381e-01 4.556089e-19
5.940750e-01 5.065132e-19
5.971276e-01 5.577213e-19
6.001959e-01 5.754405e-19
6.032799e-01 5.446470e-19
6.063798e-01 4.934345e-19
6.094955e-01 4.512923e-19
6.126274e-01 4.290290e-19
6.157752e-01 4.286221e-19
6.189394e-01 4.507539e-19
6.221197e-01 4.954574e-19
6.253164e-01 5.552284e-19
6.285294e-01 6.008028e-19
6.317590e-01 5.936326e-19
6.350053e-01 5.428504e-19
6.382681e-01 4.897784e-19
6.415477e-01 4.566351e-19
6.448442e-01 4.484049e-19
6.481578e-01 4.659749e-19
6.514882e-01 5.097900e-19
6.548357e-01 5.736018e-19
6.582006e-01 6.269192e-19
6.615826e-01 6.225949e-19
6.645274e-01 5.756418e-19
6.674851e-01 5.229619e-19
6.704562e-01 4.852676e-19
6.734404e-01 4.684861e-19
6.764379e-01 4.735947e-19
6.794488e-01 5.012064e-19
6.824731e-01 5.507799e-19
6.855108e-01 6.132274e-19
6.885620e-01 6.586223e-19
6.916268e-01 6.509583e-19
6.947053e-01 5.990619e-19
6.977975e-01 5.423665e-19
7.009034e-01 5.039386e-19
7.040231e-01 4.897026e-19
7.071568e-01 5.005844e-19
7.103043e-01 5.372214e-19
7.134659e-01 5.972436e-19
7.166416e-01 6.629501e-19
7.198315e-01 6.910981e-19
7.230354e-01 6.559482e-19
7.262537e-01 5.919587e-19
7.294863e-01 5.392589e-19
7.327333e-01 5.123080e-19
7.359947e-01 5.134947e-19
7.392707e-01 5.435846e-19
7.425612e-01 6.019381e-19
7.458663e-01 6.752993e-19
7.491862e-01 7.196567e-19
7.525209e-01 6.931896e-19
7.558704e-01 6.251797e-19
7.588381e-01 5.714579e-19
7.618173e-01 5.393279e-19
7.648083e-01 5.317497e-19
7.678110e-01 5.493118e-19
7.708255e-01 5.924475e-19
7.738519e-01 6.573684e-19
7.768901e-01 7.236454e-19
7.799402e-01 7.483253e-19
7.830024e-01 7.102102e-19
7.860764e-01 6.437527e-19
7.891626e-01 5.875887e-19
7.922611e-01 5.564244e-19
7.953715e-01 5.529138e-19
7.984943e-01 5.777074e-19
8.016292e-01 6.309248e-19
8.047765e-01 7.049564e-19
8.079361e-01 7.675960e-19
8.111082e-01 7.691469e-19
8.142927e-01 7.098715e-19
8.174896e-01 6.397253e-19
8.206991e-01 5.912867e-19
8.239213e-01 5.730225e-19
8.271561e-01 5.860952e-19
8.304037e-01 6.311718e-19
8.336638e-01 7.045623e-19
8.369369e-01 7.811033e-19
8.402228e-01 8.044436e-19
8.435216e-01 7.522426e-19
8.468334e-01 6.750944e-19
8.501581e-01 6.177240e-19
8.531439e-01 5.942652e-19
8.561401e-01 5.985528e-19
8.591469e-01 6.311930e-19
8.621642e-01 6.915780e-19
8.651922e-01 7.692496e-19
8.682308e-01 8.285191e-19
8.712800e-01 8.232002e-19
8.743399e-01 7.598835e-19
8.774107e-01 6.873689e-19
8.804921e-01 6.363496e-19
8.835844e-01 6.150977e-19
8.866876e-01 6.247573e-19
8.898017e-01 6.659788e-19
8.929267e-01 7.366951e-19
8.960626e-01 8.189685e-19
8.992096e-01 8.637348e-19
9.023677e-01 8.310812e-19
9.055368e-01 7.534540e-19
9.087171e-01 6.832341e-19
9.119085e-01 6.426188e-19
9.151112e-01 6.357348e-19
9.183251e-01 6.633162e-19
9.215502e-01 7.254589e-19
9.247867e-01 8.126022e-19
9.280346e-01 8.838721e-19
9.312939e-01 8.789773e-19
9.345645e-01 8.048793e-19
9.378467e-01 7.238894e-19
9.411405e-01 6.716957e-19
9.444458e-01 6.563247e-19
9.474463e-01 6.750062e-19
9.504563e-01 7.251460e-19
9.534759e-01 8.028170e-19
9.565049e-01 8.853373e-19
9.595442e-01 9.215530e-19
9.625922e-01 8.802743e-19
9.656506e-01 7.991996e-19
9.687186e-01 7.275361e-19
9.717961e-01 6.854834e-19
9.748832e-01 6.768616e-19
9.779807e-01 7.023164e-19
9.810878e-01 7.621378e-19
9.842045e-01 8.492870e-19
9.873316e-01 9.304448e-19
9.904683e-01 9.456252e-19
9.936155e-01 8.818264e-19
9.967722e-01 7.949173e-19
9.999384e-01 7.296956e-19
1.003115e+00 6.996330e-19
1.006302e+00 7.065691e-19
1.009499e+00 7.512085e-19
1.012707e+00 8.315052e-19
1.015923e+00 9.270120e-19
1.019152e+00 9.789658e-19
1.022390e+00 9.390827e-19
1.025637e+00 8.480522e-19
1.028896e+00 7.682728e-19
1.032165e+00 7.245126e-19
1.035444e+00 7.208922e-19
1.038733e+00 7.581927e-19
""".split())

def lisa_sensitivity():
    '''Computes LISA sensitivity curve according to `Larson, Hiscock, and Hellings (2000) <http://adsabs.harvard.edu/abs/2000PhRvD..62f2001L>`_
    '''

    ldata = np.asarray(_LISA_DATA).reshape(-1, 2).T
    return interp1d(ldata[0], ldata[1])

def lisa_root_psd():
    '''Computes LISA sensitivity curve according to `Cornish and Robson 2018 <https://arxiv.org/pdf/1803.01944.pdf>`_
    ''' 
    freq = np.logspace(-9,1,10000)
    # note: freq [Hz], L_arm [m], S_n [Hz^-0.5]
    L_arm = 2.5e9
    f_star = 19.09*1e-3
    
    P_oms = (1.5e-11)**2*(1. + (2.0e-3/freq)**4) 
    P_acc = (3.0e-15)**2*(1. + (0.4e-3/freq)**2)*(1. + (freq/(8.0e-3))**4)
    
    P_n = (P_oms + 2.*(1. + np.cos(freq/f_star)**2)*P_acc/(2.*np.pi*freq)**4)/L_arm**2
    R = 3./20./(1. + 6./10.*(freq/f_star)**2)
    S_n = (P_n/R)**0.5
    
    return interp1d(freq, S_n)


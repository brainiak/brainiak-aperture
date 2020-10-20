# Introduction and framing
_Shvartsman et al. 2018_ framed a number of common fMRI analysis methods available in `BrainIAK` as matrix-normal models, and showed some benefits of this formulation. _Cai et al. 2020_ provided an alternate framing of the work focusing on the modeling of structured residuals. 

Shvartsman, M., Sundaram, N., Aoi, M., Charles, A., Willke, T. L., & Cohen, J. D. (2018). Matrix-normal models for fMRI analysis. International Conference on Artificial Intelligence and Statistics, AISTATS 2018, 1914–1923.

Cai, M. B., Shvartsman, M., Wu, A., Zhang, H., & Zhu, X. (2020). Incorporating structured assumptions with probabilistic graphical models in fMRI data analysis. Neuropsychologia, 144, 1–23. https://doi.org/10.1016/j.neuropsychologia.2020.107500


# Mathematical tools

_Magnus & Neudecker 1988_ is the standard reference for matrix calculus, and has recently been updated to its third edition. However, the identities needed to understand the derivations within the matrix-normal paper are all available in a compact table on Wikipedia at https://en.wikipedia.org/wiki/Matrix_calculus#Identities_in_differential_form. Heavy use is made of the expectation of the quadratic form, which is explained here https://en.wikipedia.org/wiki/Quadratic_form_(statistics)#Expectation. The _matrix cookbook_ contains a number of useful identities used for simplifying the expressions in the matrix-normal paper. For the remainder, a useful reference would be a standard textbook focused on Baysian statistics and/or machine learning such as _Bishop 2006_. 

Magnus, J. R., & Neudecker, H. (1988). Matrix differential calculus with applications in statistics and econometrics.

Petersen, K. B., & Petersen, M. S. (2012). The Matrix Cookbook. https://doi.org/10.1.1.113.6244

Petersen, K. B., & Petersen, M. S. (2012). The Matrix Cookbook. No longer available on its original website but can be found in many course materials, including here: https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf. 

# Inference for seprable covariance models
The _Saatçi 2011_ thesis chapter 5 gives the kronecker solve / multiplication algorithms used for efficient inference in separable models. _Stegle et al. 2011_ and _Rakitsch et al. 2013_ give an alternate inference scheme for models marginalizing over separable covariances exploiting the compatibility between the kronecker product and the singular value decomposition. _Manceur et al. 2013_ give a maximum likelihood algorithm for higher-order normal distributions that inspires the ECM/ECME algorithms in the _Shvartsman et al._ contribution. 

Saatçi, Y. (2011). Scalable inference for structured Gaussian process models. Doctoral thesis, University of Cambridge (available from e.g. http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.222.579&rep=rep1&type=pdf). 

Stegle, O., Lippert, C., Mooij, J., Lawrence, N. D., & Borgwardt, K. (2011). Efficient inference in matrix-variate Gaussian models with iid observation noise. Advances in Neural Information Processing Systems 24 (NIPS 2011), 630–638. Retrieved from http://papers.nips.cc/paper/4281-efficient-inference-in-matrix-variate-gaussian-models-with-iid-observation-noise

Rakitsch, B., Lippert, C., Borgwardt, K., & Stegle, O. (2013). It is all in the noise: Efficient multi-task Gaussian process inference with structured residuals. Advances in Neural Information Processing Systems, 1466–1474. Retrieved from http://papers.nips.cc/paper/5089-it-is-all-in-the-noise-efficient-multi-task-gaussian-process-inference-with-structured-residuals

Manceur, A. M., & Dutilleul, P. (2013). Maximum likelihood estimation for the tensor normal distribution: Algorithm, minimum sample size, and empirical bias and dispersion. Journal of Computational and Applied Mathematics, 239(1), 37–49. https://doi.org/10.1016/j.cam.2012.09.017

# Related Applications

The framework of matrix-normal models for fMRI operates in a broader context of separable covariance models for neuroimaging. In particular, _Katanoda et al. 2002_ introduce a regression model for fMRI with separable residuals, i.e. a "Matrix-normal GLM". _Hartvig 2002_ adds a separable residual covariance to a spatial activation model for fMRI. _Bijma et al. 2005_ and _Roś et al. 2014_ use separable covariance models for spatiotemporal MEG data, as well as MEG data including task covariance. _Kia et al. 2018_ use tensor regression models for analyzing fMRI data. 

Katanoda, K., Matsuda, Y., & Sugishita, M. (2002). A spatio-temporal regression model for the analysis of functional MRI data. NeuroImage, 17(3), 1415–1428. https://doi.org/10.1006/nimg.2002.1209

Hartvig, N. V. (2002). A Stochastic Geometry Model for Functional Magnetic Resonance Images. Scandinavian Journal of Statistics, 29(3), 333–353. https://doi.org/10.1111/1467-9469.00294

Bijma, F., De Munck, J. C., & Heethaar, R. M. (2005). The spatiotemporal MEG covariance matrix modeled as a sum of Kronecker products. NeuroImage, 27(2), 402–415. https://doi.org/10.1016/j.neuroimage.2005.04.015

Roś, B., Bijma, F., de Gunst, M., & de Munck, J. (2014). A three domain covariance framework for EEG/MEG data. NeuroImage, 119, 305–315. https://doi.org/10.1016/j.neuroimage.2015.06.020

Kia, S. M., Beckmann, C. F., & Marquand, A. F. (2018). Scalable Multi-Task Gaussian Process Tensor Regression for Normative Modeling of Structured Variation in Neuroimaging Data. Retrieved from http://arxiv.org/abs/1808.00036
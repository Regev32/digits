# digits

This repository provides two simple Python scripts to generate random samples from:

- A Uniform distribution U(0,1)
- An Exponential distribution Exp(λ)

## Requirements

- Python 3.x  
- NumPy (specified in `requirements.txt`)

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Uniform samples

1. Open `uniform.py` and set the following parameters at the top of the file:

   ```python
   size = 1000   # number of samples to generate
   seed = 42     # random seed for reproducibility
   ```

2. Run the script:

   ```bash
   python uniform.py
   ```

3. The script will plot the distribution `size` independent samples drawn uniformly from the interval [0, 1], and will print the first 10 values.

### 2. Exponential samples

1. Open `exponential.py` and set the following parameters at the top of the file:

   ```python
   size = 1000    # number of samples to generate
   seed = 42      # random seed for reproducibility
   lambd = 0.5    # rate parameter λ
   ```

2. Run the script:

   ```bash
   python exponential.py
   ```

3. The script will plot the distribution of  `size` independent samples drawn from an Exponential distribution with rate λ, and will print the first 10 values.

## Results
For uniform distribution with `size = 1000000` and `seed = 42` we get the first 10 samples are
` [0.5956383284647018, 0.16517476551234722, 0.8672130780760199, 0.03482430358417332, 0.7587849267292768, 0.68738634721376, 0.8567734786774963, 0.004554843530058861, 0.4132854558993131, 0.19961059978231788]
` and the overall plot of all the samples is:
![image](https://github.com/user-attachments/assets/9cbaf064-c132-432b-be12-a402c31ed6e5)

For exponential distribution with `size = 10000` and `seed = 50` we get the first 10 samples are
 `[0.27888165, 0.02613312, 0.43769495, 0.337598, 0.31227626, 0.21062028, 0.4327722,2 0.03584634, 0.0009148,9 0.15579776]` and the overall plot of all the samples is:
![image](https://github.com/user-attachments/assets/33fe6265-ad6f-47fe-aa74-80237d68ec10)



# Black-Scholes
A proof of concept of the Black Scholes Model. We calculate the drift rate and volatility of an underlying asset, using its call and input option prices.

Black Scholes is one of the most important concepts in modern financial history. It assumes that instruments such as stock shares follow a lognormal distribution of prices. The asset S follows a geometric brownian motion which satisfies the following stochastic differential equation:

$$dS_t = \mu S_t dt + \sigma S_t dW_t$$

where &mu; represents the drift rate of growth of the asset, &sigma; represents the volatility of returns, and W<sub>t</sub> denotes a Weiner process (one dimensional Brownian motion). Under Ito's lemma, the above SDE has the analytic solution:

$$dS_t = S_0 \ exp ((\mu - \frac{\sigma^2}{2})t + \sigma \sqrt t Z )$$

Here S<sub>t</sub> is the spot price of the asset at a time t and Z is a standard normal random variable.  A European option may be exercised only at the expiration date of the option. On this date, the seller is obligated to sell the underlying stock to the buyer at the strike price K. Hence, at time t = 0, the call and input option prices can be found as:

$$\displaylines{C_0 =\frac{1}{N} \sum_{i}^{N} max(S_T - K, 0) \\\ P_0 =\frac{1}{N} \sum_{i}^{N} max(K - S_T, 0)}$$

The drift rate &mu; and volatility &sigma; are initialised with random values. The call and input option prices corresponding to the values are then calculated using the initial spot price S<sub>0</sub>, strike price K, call C and input P option prices that are already known to us. Now, utilising the Nelder-Mead method, we minimise the error in these option prices, thus obtaining very good estimates for the parameters drift rate and volatility. 

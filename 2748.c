#include <stdio.h>

int	main()
{
	int	i, input;

	scanf ("%d", &input);
	long long dp[input];
	dp[0] = 0;
	dp[1] = 1;
	i = 1;
	while (++i <= input)
		dp[i] = dp[i - 2] + dp[i - 1];
	printf ("%lld", dp[input]);
}

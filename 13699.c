#include <stdio.h>

int	main()
{
	int	n, i, j;
	long long arr[36] = { 0 };

	scanf ("%d", &n);
	arr[0] = 1;
	arr[1] = 1;
	arr[2] = 2;
	i = 3;
	if (n < 3)
	{
		printf("%lld", arr[n]);
		return (0);
	}
	while (i <= n)
	{
		j = 0;
		while (j < i)
		{
			arr[i] += arr[j] * arr[i - 1 - j];
			j++;
		}
		i++;
	}
	printf ("%lld", arr[n]);
}

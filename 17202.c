#include <stdio.h>

int	main()
{
	char A[9], B[9];
	int	res[16];
	int	i, lim;

	scanf("%s", A);
	scanf("%s", B);
	i = 0;
	while (i < 8)
	{
		res[2 * i] = A[i] - '0';
		res[(2 * i) + 1] = B[i] - '0';
		i++;
	}
	lim = 0;
	while (lim < 14)
	{
		i = 0;
		while (i < 15 - lim)
		{
			res[i] += res[i + 1];
			res[i] %= 10;
			i++;
		}
		lim++;
	}
	printf ("%d%d", res[0] % 10, res[1] % 10);
}

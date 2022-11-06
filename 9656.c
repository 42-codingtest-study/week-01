#include <stdio.h>

int	main()
{
	int	i = 0, n;

	scanf ("%d", &n);
	//생각해보니까 홀수면 상근이가 지고 짝수면 창영이가 이김 근데 디피 문젠데 이렇게 해결하는게 맞나...
	if (n % 2)
		printf("CY");
	else
		printf("SK");
}

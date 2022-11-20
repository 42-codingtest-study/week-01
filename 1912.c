#include <stdio.h>

int main()
{
	int n, i = 0, minus = 0;
	long long sum = 0, max_sum = -100000;
	scanf("%d", &n);
	long long arr[n];
	int minus_max = -100000;

	while (i < n)
	{
		scanf("%lld", &arr[i]);//다 담음
		sum += arr[i];
		if(sum > max_sum)
			max_sum = sum; //max sum을 저장
		if (sum < 0)
			sum = 0; //만약 sum 이 음수가 되었을 경우 sum 을 0으로 초기화
		i++;
	}
	i = 0;
	while (i < n)
	{
		if(arr[i] >= 0)
			minus = 1; //모든 수가 음수이면 0
		i++;
	}
	if (!minus) //모든 수가 음수인 경우 그 중 가장 큰 수가 max_sum 이 됨
	{
		i = 0;
		while (i < n)
		{
			if (arr[i] > minus_max)
				minus_max = arr[i];
			i++;
		}
		max_sum = minus_max;
	}
	printf("%lld", max_sum);
}

#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

int output_m[101][101];
int L[102];
int sum[101];

int main()
{
	int test_num;
	cin >> test_num;
	for (int t = 0; t < test_num; t++)
	{
		int full_length,pos_num;
		scanf("%d%d",&full_length,&pos_num);

		for (int i = 1; i <= pos_num; i++)
		{
			scanf("%d",&L[i]);

		}
		L[pos_num+1]=full_length;
		
		//solve
		for (int i = 1; i < pos_num+1; i++)
		{
			for (int left = 1; left<= pos_num+1-i; left++)
			{
				int tmp = left + i;

				output_m[left][tmp] = INT_MAX;

				for (int mid = left; mid < tmp; mid++)
				{
					output_m[left][tmp] = min(output_m[left][tmp], output_m[left][mid] + output_m[mid + 1][tmp] + L[tmp] - L[left-1]);
				}
			}
		}
		cout << output_m[1][pos_num+1] << endl;

	}
	return 0;
}

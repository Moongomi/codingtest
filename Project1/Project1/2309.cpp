#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int arr[9];
	int n, result = 0;
	bool check = false;

	for (int i = 0; i < 9; i++)
	{
		cin >> arr[i];
		result += arr[i];
	}
	sort(arr, arr + 9);

	for (int i = 0; i < 9; i++)
	{
		for (int j = i + 1; j < 9; j++)
		{
			if ((result - arr[i] - arr[j]) == 100)
			{
				for(int out = 0; out < 9; out++)
					if(out != i && out != j)
						cout << arr[out] << endl;
				return 0;
			}

		}
	}
	
	return 0;

}
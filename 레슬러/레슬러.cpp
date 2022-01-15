#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
   int N = 0;
   int a[10001][2];
   cin >> N;
   vector<pair<int, int>> b(N);
   
   for (int i = 0; i < N; i++) {
	  cin >> a[i][0] >> a[i][1];
      b[i].second = i+1;
   }

   for (int i = 0; i < N-1; i++) {
      for (int j = i + 1; j < N; j++) {
         int scoreA = 0;
         int scoreB = 0;
         scoreA = a[i][0] + a[i][1] * a[j][0];
         scoreB = a[j][0] + a[j][1] * a[i][0];
         if (scoreA > scoreB) {
            b[i].first++;
         }
         else {
            b[j].first++;
         }

      }
   }
   sort(b.begin(), b.end(), greater<pair<int, int>>());
   for (int i = 0; i < N ; i++) {
      cout << b[i].second << "\n";
   }

}
#include<iostream>
#include<algorithm>
#include<list>
#include<map>
#include<vector>
#include<cstdio>
#include<climits>
#include<cmath>
#include<cstring>
#include<cassert>

using namespace std;

long long pow0(int K, int C) {
    long long res = 1;
    for (int i = 1; i <= C; ++i)
        res *= K;
    return res;
}

int main(){
	ios::sync_with_stdio(false);
	int T;
    cin>>T;
    for (int t = 1; t <= T; ++t) {
        int k, c, s;
        cin>>k>>c>>s;
        printf("Case #%d: ", t);
        
        if (s*c < k) {
          cout<<"IMPOSSIBLE"<<endl;
          continue;
        }
        
        for (int i = 0; i < k; i += c) {
          // every time we can check c positions.
          long long cur = 0; // cur is the position (offset 0)
          int amt = 0; // amt is the layer
          for (int j = i; j < i + c && j < k; j++) {
            cur = cur * k + j; // not the same offset for each group
            amt++;
          }
          while (amt < c) {
            cur *= k;
            amt++;
          }
          cout<<cur+1<<" ";
        }
        cout<<endl;
    }
	return 0;
}

/*
int main(){
	ios::sync_with_stdio(false);
	int T;
    cin>>T;
    for (int t = 1; t <= T; ++t) {
        int K, C, S;
        cin>>K>>C>>S;
        printf("Case #%d: ", t);
        if (K == 1) {
            printf("1\n");
            continue;
        }
        
        if (C == 1) {
            for (int i = 1; i <= K; ++i)
                printf((i == K) ? "%d\n" : "%d ", i);
            continue;
        }
        
        long long C1 = pow0(K, C - 1);
        for (int i = 1; i <= K; ++i) {
            long long C0 = (C1 - 1) / (K - 1) * (i - K);
            printf((i == K) ? "%lld\n" : "%lld ", C1 * i + C0);
        }
    }
	return 0;
}*/

/*
a_1 = i;
a_{n+1} = (a_n - 1) * K + i;
*/

#include<iostream>
#include<algorithm>
#include<list>
#include<map>
#include<vector>
#include<cstdio>
#include<climits>
#include<cmath>
#include<cstring>

using namespace std;

int main(){
	ios::sync_with_stdio(false);
	int T;
    cin>>T;
    for (int t = 1; t <= T; ++t) {
        string S;
        cin>>S;
        int count = 1;
        char last;
        for (int i = 0; i < S.length(); ++i) {
            if (i == 0) {
                last = S[0];
                continue;
            }
            if (S[i] != last) {
                last = S[i];
                count++;
            }
        }
        if (S[S.length() - 1] == '+')
            count--;
        printf("Case #%d: %d\n", t, count);
    }
	return 0;
}
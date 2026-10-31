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

bool met[10];

void compute_digit(long long N) {
    while (N) {
        met[N % 10] = true;
        N /= 10;
    }
}

bool check() {
    for (int i = 0; i < 10; ++i) 
        if (!met[i])
            return false;
    return true;
}

int get_number(int N) {
    int N0 = N;
    while(!check()) {
        compute_digit(N);
        N += N0;
    }
    return N - N0;
}

int main(){
	ios::sync_with_stdio(false);
	int T;
    cin>>T;
    for (int t = 1; t <= T; ++t) {
        cout<<"Case #"<<t<<": ";
        int N;
        cin>>N;
        memset(met, false, sizeof met);
        if (N == 0)
            cout<<"INSOMNIA"<<endl;
        else 
            cout<<get_number(N)<<endl;
    }
	return 0;
}
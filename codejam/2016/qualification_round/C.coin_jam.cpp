#include <iostream>
#include <algorithm>
#include <list>
#include <map>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <cmath>
#include <cstring>
#include <cassert>

using namespace std;

long long power[11][16];

int N, J;

void init() {
    for (int i = 2; i <= 10; ++i) {
        power[i][0] = 1;
        for (int j = 1; j < N; ++j) {
            // power[i][j] = i ** j;
            power[i][j] = power[i][j-1] * i;
        }
    }   
}

long long get_divisor(long long num) {
    for (long long i = 2; i <= sqrt(num); ++i) {
        if (num % i == 0)
            return i;
    }
    return -1;
}

bool verify(long long num, vector<long long> &factor) {
    int bit[16];
    
    for (int i = 0; i < N; ++i) {
        // bit[i] = a_i, given num = a_{N-1}...a_{N};
        bit[i] = num & 1;
        num >>= 1;
    }
    
    for (int i = 2; i <= 10; ++i) {
        long long temp = 0;
        for (int j = 0; j < N; ++j)
            temp += bit[j] * power[i][j];
        // temp is the number in base i;
        long long divisor = get_divisor(temp);
        if (divisor != -1) {
            factor.push_back(divisor);
        } else {
            return false;
        }
    }
    assert(factor.size() == 9);
    return true;
}

int main(){
	ios::sync_with_stdio(false);

    int T;
    cin>>T;
    for (int t = 1; t <= T; ++t) {
        cout<<"Case #"<<t<<":"<<endl;
        cin>>N>>J;
        init();
        // enumerate
        long long start = (1<<(N-1)) + 1;
        long long end = (1<<N)-1;
        int count = 0;
        vector<long long> result;
        vector<vector<long long> > factor;
        
        while(count < J && start <= end) {
            vector<long long> temp;
            if (verify(start, temp)) {
                result.push_back(start);
                factor.push_back(temp);
                count ++;
            }
            start += 2; // last bit is 1.
        }
        
        for (int i = 0; i < J; ++i) {
            int bit[16];
            long long num = result[i];
            for (int i = 0; i < N; ++i) {
                // bit[i] = a_i, given num = a_{N-1}...a_{N};
                bit[i] = num & 1;
                num >>= 1;
            }
            for (int i = N - 1; i >= 0; --i)
                cout<<bit[i];
            
            for (int j = 0; j < 9; ++j) 
                cout<<" "<<factor[i][j];
            cout<<endl;
        }
    }
	return 0;
}
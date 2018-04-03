#include <iostream>

using namespace std;

int suma(int n);
int main(){
	cout<<suma(50)<<endl;
	cout<<suma(100)<<endl;
	return 0;
}
int suma(int n){
	int sum;
	int i;
	sum = 0;
	i=1;
	for(i=1; i<=n; i++){
		sum = sum + i;
	}
	return sum;
}

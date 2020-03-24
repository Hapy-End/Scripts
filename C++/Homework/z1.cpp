#include <iostream>
#include <cmath>
using namespace std;

// Вспомогательные функции
void print7(int arr[7][7]){
    for (int i = 0; i < 7; i++){
        for (int j = 0; j < 7; j++)
            cout << arr[i][j] << " ";
        cout << endl;
    }
}

void print5(int arr[5][5]){
    for (int i = 0; i < 5; i++){
        for (int j = 0; j < 5; j++)
            cout << arr[i][j] << " ";
        cout << endl;
    }
}

int irand(int a, int b){
    return a + rand() % (b - a + 1);
}

int fact(int a){
    if (a <= 1) return 1;
    return fact(a-1) * a;
}

// Задания
void z1(){
    // ...
}

void z16(){
    // ...
}

void z22(){
    // ...
}

void z2(){
    int A[10] = {1,2,5,8,3,2,1,4,6,1}, B[10], b, k = 0;
    for (int i = 0; i < 10; i++)
    {
        b = 1;
        for (int j = 0; j < k; j++){
            if (A[i]==B[j]){
                b = 0;
                break;
            }
        }
        if (b == 1){
            B[k++] = A[i];
        }
    }
    cout << k;
}

void z3(){
    int A[5][5];
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            A[i][j] = i * 5 + j;
        }
    }
    print5(A);
}

void z4(){
    int A[5][5], n = 5;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if ( i + 1 >= j && i - 1 <= j) A[i][j] = 1;
            else A[i][j] = 0;
        }
    }
    print5(A);
}

void z5(){
    int A[7][7], n = 7;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == 0 || j == 0 || i == n-1 || j == n-1 || 
               (i >= 2 && i <= n-1-2 && j >= 2 && j <= n-1-2 && (i != n/2 || j != n/2)))
            A[i][j] = 1;
            else A[i][j] = 0;
        }
    }
    print7(A);
}

void z6(){
    int A[5][5], n = 5;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == n/2 || j == n/2) A[i][j] = 1;
            else A[i][j] = 0;
        }
    }
    print5(A);
}

void z7(){
    int A[5][5], n = 5;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == j || j == n - i - 1) A[i][j] = 1;
            else A[i][j] = 0;
        }
    }
    print5(A);
}

void z8(){
    int A[5][5], n = 5;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i > j && j > n-i-1 || i < j && j < n-i-1 ) A[i][j] = 0;
            else A[i][j] = 1;
        }
    }
    print5(A);
}

void z9(){
    int A[5][5], n = 5, m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (j == 0){
                if ((i+j) % 2 == 0) A[i][j] = 1;
                else A[i][j] = 0;
            } else
            {
                m = 0;
                for (int k = 0; k < j; k++)
                {
                    m += A[i][k];
                }
                if (m == 0) A[i][j] = 1;
                else A[i][j] = m;
            }
        }
    }
    print5(A);
}

void z10(){
    int A[5][5], n = 5;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if ((i+j)%2==0) A[i][j] = 1;
            else A[i][j] = 0;
        }
    }
    print5(A);
}

void z11(){
    int A[7][7], n = 7;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == 0 || i == n - 1 || i == j + 1 && i < n/2 || i == n - j && i < n/2
            || i == j - 1 && i >= n/2 || i == n - j - 2 && i >= n/2) A[i][j] = 1;
            else A[i][j] = 0;
        }
    }
    print7(A);
}

void z12(){
    int A[7][7], n = 7, m = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (m == 0) A[j][i] = i * n + j + 1;
            else A[j][i] = i * n + n - j; 
        }
        if (m == 0) m = 1; else m = 0;
    }
    print7(A);
}

void z13(){
    int A[7][7], n = 7, m = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == 0 || j == n-1) A[i][j] = i+j+1;
            else if (i == n - 1 || i == j + 1 && i < n/2 || i == n - j && i < n/2
            || i == j - 1 && i >= n/2 || i == n - j - 2 && i >= n/2) A[i][j] = 1;
            else A[i][j] = 0;
        }
    }
    print7(A);
}

void z14(){
    const int n = 10;
    int A[n] = {0,0,7,8,1,0,1,0,8,0}, c = 0, b;
    for (int i = 0; i < n; i++)
    {
        if (A[i] == 0) c++;
        else {
            b = A[i-c];
            A[i-c] = A[i];
            A[i] = b;
        }
    }
    for (int i = 0; i < n; i++)
    {
        cout << A[i] << " ";
    }
    cout << endl;
}

void z15(){
    int A[10][10] = {{1,1,0,1,0,1,0,0,0,1},
                     {1,1,0,0,0,0,0,1,1,0},
                     {0,0,0,0,0,0,1,1,1,0},
                     {0,0,1,1,0,0,0,0,0,0},
                     {1,0,1,1,0,1,1,0,1,0},
                     {0,0,0,0,0,1,1,0,1,0},
                     {0,0,0,0,0,0,0,0,1,0},
                     {0,0,0,0,0,0,0,0,0,0},
                     {1,1,0,1,0,1,0,0,0,1},
                     {1,1,0,0,0,0,0,1,1,0}}, c = 0,n,i1,i2,j1,j2;
    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            if (i != 9 && j != 9 && A[i][j] == 1 && A[i+1][j] == 1 && A[i][j+1] == 1 && A[i+1][j+1] == 1){
                c++;
                n = 0;
                if (i == 0) i1 = 0;
                else i1 = i-1;
                if (j == 0) j1 = 0;
                else j1 = j-1;
                if (i == 8) i2 = 9;
                else i2 = i+2;
                if (j == 8) j2 = 9;
                else j2 = j+2;
                for (int k = i1; k <= i2; k++)
                {
                    for (int m = j1; m <= j2; m++)
                    {
                        if (A[k][m] == 1) n++;
                    }
                    if (n > 4){
                        c--;
                        break;
                    }
                }
            }
        }
    }
    cout << c;
}

void z17(){
    double e = 0.001, x = 1, sum = 0, psum = 0;
    for (int i = 0;;i++){
        sum += (double) pow(-1,i) * (x / (2 * i + 1));
        if (abs(sum-psum)<=e) break;
        psum = sum;
    }
    cout << sum;
}

void z18(){
    double e = 0.001, x = 4, sum = 0, psum = 0;
    for (int n = 1;;n++){
        sum += (double) pow(x+1,3) / fact(4*n);
        if (abs(sum-psum)<=e) break;
        psum = sum;
    }
    cout << sum;
}

void z19(){
    double e = 0.00001, sum = 0, psum = 0;
    for (int n = 1;;n++){
        sum += (double) 1 / (n * (n+1)*(n+2));
        if (abs(sum-psum)<=e) break;
        psum = sum;
    }
    cout << sum;
}

void z20(){
    double e = 0.001, x = 1, sum = 0, psum = 0;
    for (int n = 1;;n++){
        sum += (double) pow(n*x,n) / fact(2*n+1);
        if (abs(sum-psum)<=e) break;
        psum = sum;
    }
    cout << sum;
}

void z21(){
    const int N = 7;
    int A[N][N], B[N][N], k = 4, m = -1;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            A[i][j] = irand(10,50);
            B[i][j] = irand(10,50);
            cout << A[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
    print7(B);
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            for (int c = 0; c < N; c++)
            {
                if (A[i][j] == B[c][k]){
                    m = i;
                    break;
                }
            }
            if (m >= 0) break;
        }
        if (m >= 0) break;
    }
    cout << m;
}

void z23(){
    const int N = 8;
    int A[N][N], b;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            A[i][j] = irand(10,50);
            cout << A[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
    for (int i = 0; i < N/2; i++)
    {
        b = A[i][N-i-1];
        A[i][N-i-1] = A[N-i-1][i];
        A[N-i-1][i] = b;
    }
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cout << A[i][j] << " ";
        }
        cout << endl;
    }
}

void z24(){
    const int N = 10, M = 6;
    int A[N][M], max, s = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            A[i][j] = irand(0,20);
            cout << A[i][j] << " ";
        }
        cout << endl;
    }
    for (int i = 0; i < M; i++)
    {
        max = A[0][i];
        for (int j = 0; j < N; j++)
        {
            if (max < A[j][i]) max = A[j][i];
        }
        s *= max;
    }
    cout << s;
}

void z25(){
    int A[6][6], s = 0;
    for (int i = 0; i < 6; i++)
    {
        for (int j = 0; j < 6; j++)
        {
            A[i][j] = irand(10,20);
            cout << A[i][j] << " ";
        }
        cout << endl;
    }
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 6; j++)
        {
            s += A[i*2+1][j]*A[j][i*2];
        }
    }
    cout << s;
}

void z26(){
    const int N = 10;
    int A[N], B[N], C[N], c, k = 0;
    for (int i = 0; i < N; i++)
    {
        A[i] = irand(0,10);
        cout << A[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < N; i++)
    {
        c = 0;
        for (int j = 0; j < N; j++)
        {
            if (A[i] == B[j]){
                C[j]++;
                c = 1;
                break;
            }
        }
        if (c == 0){
            B[k] = A[i];
            C[k++]= 1;
        }
    }
    c = 0;
    for (int i = 0; i < k; i++)
    {
        if (C[c] < C[i]) c = i;
    }
    cout << B[c] << " - " << C[c];
}

int main(){
    z21();
}
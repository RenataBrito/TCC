
int v[100], exists[100], ainv[100];
void invert(int a[], int N)
{
int i;
      for (i = 0;   (i != N) ;  i++) {
         if (a[i] < 0 || a[i] >= N || exists[a[i]])
         {
             printf("Input is not a permutation.\n");
             return;
         }
         exists[a[i]] = 1;
      }
      for (i = 0; i < N; i++)
         ainv[a[i]] = i;
      for (i = 0; i < N; i++)
         printf("%d ", ainv[i]);
      printf("\n");
}
void main(int argc, char *argv[]) {
      int N = argc - 1, i;
      for (i = 0; i < N; i++)
         v[i] = atoi(argv[i+1]);
      invert(v, N);
}

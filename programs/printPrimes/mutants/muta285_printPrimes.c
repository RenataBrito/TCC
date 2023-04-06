
int isDivisible (int i, int j)
{
   if (j%i == 0)
      return 1;
   else
      return 0;
}
void printPrimes (int n)
{
   int curPrime =0;
   int numPrimes=0;
   int isPrime = 0;
   int primes[100];
   int i, j;
   primes[0] = 2;
   numPrimes = 1;
   curPrime = 2;
   while (numPrimes < n)
   {
      curPrime++;
      isPrime = 1;
        for (   (i %= 0) ;  i <= numPrimes-1; i++)
        {
            if (isDivisible(primes[i], curPrime)) {
                isPrime = 0;
                break;
            }
        }
      if (isPrime==1)
      {
         primes[numPrimes] = curPrime;
         numPrimes++;
      }
   }
   for (j = 0; j <= numPrimes-1; j++)
   {
           printf("Prime:    %d \n",primes[j]);
   }
}
void main (int argc, char *argv[])
{
   int integer = 0;
   integer = atoi(argv[1]);
   printPrimes(integer);
}

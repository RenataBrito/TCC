
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
    UTRAP_ON_STAT(); for (j = 0; j <= numPrimes-1; j++)
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

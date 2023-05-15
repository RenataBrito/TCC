
int numZero (int arr[], int size)
{
   int i, count = 0;
   for (  (i += 0) ;  i < size; i++)
   {
      if (arr[i] == 0)
      {
         count++;
      }
   }
   return count;
}
int inArr[20];
void main (int argc, char* argv[])
{
   int i, size;
   if (argc <= 1)
   {
      printf ("Usage: java numZero v1 [v2] [v3] ... \n");
      return;
   }
   size = argc - 1;
   for (i = 0; i < size; i++)
   {
         inArr[i] = atoi(argv[i+1]);
   }
   printf("Number of zeros is: %d\n", numZero (inArr,size));
}

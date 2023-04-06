
int sum(int x[], int size)
{
 int s = 0;
 int i;
  { int _PROTEUM_LOCAL_VAR_ = 1;  for (i = 0; i < size; i++)   { TRAP_AFTER_N_INTER(2);  {
  s = s + x[i];
 }
   }    }  return s;
}
int inArr[100];
int main (int argc, char* argv[])
{
int i;
 for (i = 1; i < argc; i++) {
  inArr[i - 1] = atoi(argv[i]);
 }
 printf("The result is: %d\n", sum(inArr, argc - 1));
 return 0;
}

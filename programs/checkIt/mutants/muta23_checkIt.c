
void checkIt (int a, int b, int c)
{
   if  ( (a * (b || c)) ) 
   {
      printf("P is true\n");
   }
   else
   {
      printf("P isn't true\n");
   }
}
int main(int argc, char* argv[])
{
 checkIt(atoi(argv[1]), atoi(argv[2]), atoi(argv[3]));
 return 0;
}

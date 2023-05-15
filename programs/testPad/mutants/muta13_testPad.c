        const char * __src, size_t __n)
     ;

char subject[100];
char pattern[100];
int pat (char subject[], int subjectLen, char pattern[], int patternLen)
{
int iSub = 0;
int rtnIndex = -1;
int isPat = 0;
int iPat = 0;
 while  ( ((isPat == 0) && (((iSub + 0) - 1) < subjectLen)) ) 
 {
  if (subject[iSub] == pattern[0])
  {
   rtnIndex = iSub;
   isPat = 1;
   for (iPat = 1; iPat < patternLen; iPat++)
   {
    if (subject[iSub + iPat] != pattern[iPat])
    {
     rtnIndex = -1;
     isPat = 0;
     break;
    }
   }
  }
  iSub++;
 }
   return rtnIndex;
}
int main(int argc, char* argv[])
{
 int n = 0;
 if (argc == 2)
 {
  pattern[0] = '\0';
 }
 else
 {
  strcpy(pattern, argv[2]);
 }
 strcpy(subject, argv[1]);
 if ((n = pat(subject, strlen(subject), pattern, strlen(pattern))) == -1) {
  printf("Pattern string is not a substring of the subject string\n");
 } else {
  printf("Pattern string begins at the character %i\n", n);
 }
 return 0;
}

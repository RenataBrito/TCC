        const char * __src, size_t __n)
     ;

int isPalindrome(char s[]) {
    int low = 0;
    int high = strlen(s)-1;
    while (low < high) {
      if  ( (s[low] != s[TRAP_ON_NEGATIVE(high)]) ) 
        return 0;
      low++;
      high--;
    }
    return 1;
  }
void main(int argc, char *argv[]) {
char *p = argv[1];
if (isPalindrome(p))
  printf("%s is a palindrome",p);
else
  printf("%s is not a palindrome",p);
}

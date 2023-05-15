        const char * __src, size_t __n)
     ;

int isPalindrome(char s[]) {
    int low = 0;
    int high = strlen(s)-1;
     { int _PROTEUM_LOCAL_VAR_ = 1;  while (low < high)   { FALSE_AFTER_N_INTER(2);  {
      if (s[low] != s[high])
        return 0;
      low++;
      high--;
    }
      }    }  return 1;
  }
void main(int argc, char *argv[]) {
char *p = argv[1];
if (isPalindrome(p))
  printf("%s is a palindrome",p);
else
  printf("%s is not a palindrome",p);
}

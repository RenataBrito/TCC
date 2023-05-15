     ;
extern long double fmal (long double __x, long double __y, long double __z) ; extern long double __fmal (long double __x, long double __y, long double __z) ;

extern long double scalbl (long double __x, long double __n) ; extern long double __scalbl (long double __x, long double __n) ;
extern int signgam;
enum
  {
    FP_NAN,
    FP_INFINITE,
    FP_ZERO,
    FP_SUBNORMAL,
    FP_NORMAL
  };
typedef enum
{
  _IEEE_ = -1,
  _SVID_,
  _XOPEN_,
  _POSIX_,
  _ISOC_
} _LIB_VERSION_TYPE;
extern _LIB_VERSION_TYPE _LIB_VERSION;
struct exception
  {
    int type;
    char *name;
    double arg1;
    double arg2;
    double retval;
  };
extern int matherr (struct exception *__exc);

void computeStats(int numbers[], int size)
{
 double med, var, sd, mean, sum, varsum;
 int i;
 sum = 0.0;
 for (i = 0; i < size; i++) {
  sum += numbers[i];
 }
 med = numbers[size/2];
 mean = sum / size;
 varsum = 0.0;
 for (i = 0; i < size; i++) {
    varsum = varsum + ((numbers[i] - mean) * (numbers [i] - mean));
 }
   (var = ((TRAP_ON_ZERO(size) <= 1) ? 0 : (varsum / (size - 1)))) ; 
 sd = sqrt(var);
 printf("median:             %2.3f\n", med);
 printf("mean:               %2.3f\n", mean);
    printf("variance:           %2.3f\n", var);
 printf("standard deviation: %2.3f\n", sd);
}
int numbers[100];
int main (int argc, char* argv[])
{
int i;
 for (i = 1; i < argc; i++)
  numbers[i-1] = atoi(argv[i]);
 computeStats(numbers, argc-1);
 printf("\n");
 return 0;
}

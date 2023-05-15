
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

double Phi2(double, double, double);
double phi01(double);
double PhiInverse(double);
double Phi201(double);
double phi(double, double, double);
double PhiInverse02(double, double, double, double);
double phi01(double x) {
    return exp(-x*x / 2) / sqrt(2 * 3.14159265358979323846);
}
double phi(double x, double mu, double sigma) {
    return phi01((x - mu) / sigma) / sigma;
}
double Phi201(double z) {
    double sum = 0.0, term = z;
    int i;
    if (z < -8.0) return 0.0;
    if (z > 8.0) return 1.0;
    for ( i = 3; sum + term != sum; i += 2){
        sum = sum + term;
        term = term * z * z / i;
    }
    return 0.5 + sum * phi01(z);
}
double Phi2(double z, double mu, double sigma) {
    return Phi201((z - mu) / sigma);
}
double PhiInverse02(double y, double delta, double lo, double hi) {
    double mid = lo + (hi - lo) / 2;
    if (hi - lo < delta) return mid;
    if  ( (Phi201(mid) >= y) )  return PhiInverse02(y, delta, lo, mid);
    else return PhiInverse02(y, delta, mid, hi);
}
double PhiInverse(double y) {
    return PhiInverse02(y, .00000001, -8, 8);
}
void main(int argc, char *argv[]) {
    if ( strcmp("-", argv[1]) == 0 )
    {
        driver(atoi(argv[2]), argc, argv);
    }
    else
    {
        driver(0, argc, argv);
    }
}

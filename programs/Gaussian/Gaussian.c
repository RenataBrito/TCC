
/*************************************************************************
 *  Compilation:  javac Gaussian.java
 *  Execution:    java Gaussian x mu sigma
 *
 *  Function to compute the Gaussian pdf (probability density function)
 *  and the Gaussian cdf (cumulative density function)
 *
 *  % java Gaussian 820 1019 209
 *  0.17050966869132111
 *
 *  % java Gaussian 1500 1019 209
 *  0.9893164837383883
 *
 *  % java Gaussian 1500 1025 231
 *  0.9801220907365489
 *
 *  The approximation is accurate to absolute error less than 8 * 10^(-16).
 *  Reference: Evaluating the Normal Distribution by George Marsaglia.
 *  http://www.jstatsoft.org/v11/a04/paper
 *
 *************************************************************************/
#include <stdio.h>
#include <math.h>

double Phi2(double, double, double);
double phi01(double);
double PhiInverse(double);
double Phi201(double);
double phi(double, double, double);
double PhiInverse02(double, double, double, double);


/* return phi(x) = standard Gaussian pdf */
double phi01(double x) {
    return exp(-x*x / 2) / sqrt(2 * M_PI);
}

/* return phi(x, mu, signma) = Gaussian pdf with mean mu and stddev sigma */
double phi(double x, double mu, double sigma) {
    return phi01((x - mu) / sigma) / sigma;
}

/* return Phi(z) = standard Gaussian cdf using Taylor approximation */
double Phi201(double z) {
    double sum = 0.0, term = z;
    int i;
    
    if (z < -8.0) return 0.0;
    if (z >  8.0) return 1.0;
	

    for ( i = 3; sum + term != sum; i += 2){
        sum  = sum + term;
        term = term * z * z / i;
    }
    return 0.5 + sum * phi01(z);
}

/* return Phi(z, mu, sigma) = Gaussian cdf with mean mu and stddev sigma */
double Phi2(double z, double mu, double sigma) {
    return Phi201((z - mu) / sigma);
} 

 

/* bisection search */
double PhiInverse02(double y, double delta, double lo, double hi) {
    double mid = lo + (hi - lo) / 2;
    if (hi - lo < delta) return mid;
    if (Phi201(mid) > y) return PhiInverse02(y, delta, lo, mid);
    else              return PhiInverse02(y, delta, mid, hi);
}


/* Compute z such that Phi(z) = y via bisection search */
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


///* test client */
//void main(int argc, char *argv[]) {
//    /*
//	double z     = Double.parseDouble(args[0]);
//    double mu    = Double.parseDouble(args[1]);
//    double sigma = Double.parseDouble(args[2]);
//	*/
//	double z,mu,sigma;
//	printf("input z!\n");
//	scanf("%lf",&z);
//	printf("input mu!\n");
//	scanf("%lf",&mu);
//	printf("input sigma!\n");
//	scanf("%lf",&sigma);
//
//    printf("%lf \n",Phi202(z, mu, sigma));
//    double y = Phi201(z);
//    printf("%lf",PhiInverse01(y));
//}
//

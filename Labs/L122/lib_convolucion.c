//Lab 12
//Natalia Cristina Escudero Lay 
//20223377

extern void convolucionar_vector_asm_float_simd(float *xn,float *hk, float *yn,long long N,long long K); 
extern void convolucionar_vector_asm_float(float *xn,float *hk, float *yn,long long N,long long K); 

void convolucionar_vector_c_float(float *xn,float *hk, float *yn,long long N,long long K){
    for (int n = 0; n<N; n++){
        for (int k = 0; k<K; k++){
            if (n - k >= 0){
                yn[n] = yn[n] + xn[n-k]*hk[k]; 
            }
        }
    }
}